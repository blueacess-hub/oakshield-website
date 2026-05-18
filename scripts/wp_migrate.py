#!/usr/bin/env python3
"""
WP Migration Script — pushes mockup HTML into WordPress as page content.

For each mockup page:
  1. Read HTML
  2. Extract body content
  3. Rewrite asset URLs → uploaded WP media URLs
  4. Rewrite inter-page links → WP permalinks
  5. Prepend Tailwind CDN + fonts + SHARED_CSS (since WP <head> doesn't have them)
  6. POST as wp:html block content
"""
import json, os, re, sys, requests
from requests.auth import HTTPBasicAuth

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

cfg = json.load(open(".wp_credentials.json"))
site = cfg["site_url"].rstrip("/")
auth = HTTPBasicAuth(cfg["username"], cfg["app_password"].replace(" ", ""))
media = json.load(open(".wp_media_urls.json"))

# URL replacements (asset paths)
# Mockup uses ../assets/generated/X.png (from mockup/) or ../../assets/generated/X.png (from mockup/markets/)
asset_map = {}
for local, url in media.items():
    name = os.path.basename(local)
    # All possible relative path variants in mockup HTML
    asset_map[f"../assets/generated/{name}"] = url
    asset_map[f"../../assets/generated/{name}"] = url
    asset_map[f"../assets/brand/{name}"] = url
    asset_map[f"../../assets/brand/{name}"] = url

# Page link map: mockup-relative → WP permalink
# Will be filled after page creation
PAGE_LINKS = {
    "index.html": "/",
    "../index.html": "/",
    "services.html": "/services/",
    "../services.html": "/services/",
    "company.html": "/company/",
    "../company.html": "/company/",
    "contact.html": "/contact/",
    "../contact.html": "/contact/",
    "markets/data-centers.html": "/markets/data-centers/",
    "markets/hospitality.html": "/markets/hospitality/",
    "markets/cold-storage.html": "/markets/cold-storage/",
    "markets/big-box-retail.html": "/markets/big-box-retail/",
    "markets/industrial.html": "/markets/industrial/",
    "../markets/data-centers.html": "/markets/data-centers/",
    "../markets/hospitality.html": "/markets/hospitality/",
    "../markets/cold-storage.html": "/markets/cold-storage/",
    "../markets/big-box-retail.html": "/markets/big-box-retail/",
    "../markets/industrial.html": "/markets/industrial/",
}

# Wrapper CSS — injected at top of every page content
WRAPPER_CSS = """
<!-- wp:html -->
<style id="oak-shield-reset">
/* Hide all WP block theme chrome — page content owns full presentation */
header.wp-block-template-part,
footer.wp-block-template-part,
.wp-site-blocks > header,
.wp-site-blocks > footer,
.wp-block-template-part { display: none !important; }

/* Nuke ALL margin/padding on WP block theme wrappers (top + bottom + sides) */
html, body { margin: 0 !important; padding: 0 !important; }
body.admin-bar { padding-top: 0 !important; margin-top: 0 !important; }
.wp-site-blocks,
.wp-site-blocks > *,
.wp-block-group,
.wp-block-post-content,
.entry-content,
.is-layout-flow,
.is-layout-constrained {
  max-width: none !important;
  width: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
}
main,
main.wp-block-group,
main.is-layout-flow {
  margin: 0 !important;
  padding: 0 !important;
  margin-block-start: 0 !important;
  padding-block-start: 0 !important;
  margin-top: 0 !important;
  padding-top: 0 !important;
}
.has-global-padding,
.has-global-padding > * {
  padding: 0 !important;
  margin-block-start: 0 !important;
  padding-block-start: 0 !important;
}

/* Children of WP layout wrappers: full width + zero ALL margins (incl. logical block) */
.is-layout-constrained > *,
.is-layout-flow > *,
.entry-content > *,
.wp-block-post-content > *,
.wp-site-blocks > * {
  max-width: none !important;
  width: auto !important;
  margin: 0 !important;
  margin-block-start: 0 !important;
  margin-block-end: 0 !important;
  margin-inline-start: 0 !important;
  margin-inline-end: 0 !important;
}
/* WP injects 1.2rem margin-block-start on first/subsequent children — kill all of it */
:where(.wp-site-blocks) > *,
:where(.is-layout-flow) > *,
:where(.is-layout-constrained) > * {
  margin-block-start: 0 !important;
  margin-block-end: 0 !important;
}

/* WP admin bar (only shows for logged-in users) — push our content below it on mobile so it doesn't overlap */
@media screen and (max-width: 782px) {
  body.admin-bar #wpadminbar { position: fixed !important; }
}

/* Allow our own sections to define their own layout */
.alignfull { margin: 0 !important; max-width: none !important; }
</style>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Manrope:wght@600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<!-- /wp:html -->

"""


def extract_body(html_text: str) -> str:
    """Pull everything between <body...> and </body>."""
    m = re.search(r"<body[^>]*>(.*?)</body>", html_text, re.DOTALL | re.IGNORECASE)
    if not m:
        raise RuntimeError("No <body> found")
    return m.group(1)


def extract_head_styles(html_text: str) -> str:
    """Pull <style>...</style> from <head> so we can inline them."""
    m = re.search(r"<head[^>]*>(.*?)</head>", html_text, re.DOTALL | re.IGNORECASE)
    if not m:
        return ""
    head = m.group(1)
    styles = re.findall(r"<style[^>]*>.*?</style>", head, re.DOTALL | re.IGNORECASE)
    return "\n".join(styles)


def extract_head_schema(html_text: str) -> str:
    """Pull all <script type=application/ld+json> blocks from anywhere."""
    return "\n".join(re.findall(r'<script type="application/ld\+json">.*?</script>', html_text, re.DOTALL | re.IGNORECASE))


def rewrite_urls(content: str) -> str:
    """Replace asset paths with WP media URLs, and inter-page links with WP permalinks.

    IMPORTANT: replace LONGEST patterns first to avoid partial-prefix replacement bugs
    (e.g. `../../assets/X.png` must be replaced before `../assets/X.png`).
    """
    # Asset replacements — longest first
    for local_path in sorted(asset_map.keys(), key=len, reverse=True):
        content = content.replace(local_path, asset_map[local_path])
    # Page link replacements — longest first
    for mockup_link in sorted(PAGE_LINKS.keys(), key=len, reverse=True):
        wp_link = PAGE_LINKS[mockup_link]
        content = content.replace(f'href="{mockup_link}"', f'href="{wp_link}"')
        content = content.replace(f"href='{mockup_link}'", f"href='{wp_link}'")
    return content


def build_page_content(html_path: str) -> str:
    with open(html_path) as f:
        html = f.read()
    body = extract_body(html)
    head_styles = extract_head_styles(html)
    schema = extract_head_schema(html)

    # Rewrite all URLs
    body = rewrite_urls(body)
    head_styles = rewrite_urls(head_styles)
    schema = rewrite_urls(schema)

    # Strip the schema from body (it's in <head> originally but if extracted to body, dedupe)
    body = re.sub(r'<script type="application/ld\+json">.*?</script>', "", body, flags=re.DOTALL | re.IGNORECASE)

    # Wrap into wp:html block
    inner = head_styles + "\n" + body + "\n" + schema
    page_content = WRAPPER_CSS + "<!-- wp:html -->\n" + inner + "\n<!-- /wp:html -->"
    return page_content


def get_page(slug: str):
    r = requests.get(f"{site}/wp-json/wp/v2/pages?slug={slug}&context=edit", auth=auth, timeout=15)
    r.raise_for_status()
    data = r.json()
    return data[0] if data else None


def update_page(page_id: int, title: str, content: str, slug: str = None, parent: int = None, template: str = "page-no-title"):
    body = {"title": title, "content": content, "status": "publish", "template": template}
    if slug: body["slug"] = slug
    if parent is not None: body["parent"] = parent
    r = requests.post(f"{site}/wp-json/wp/v2/pages/{page_id}", auth=auth, json=body, timeout=30)
    r.raise_for_status()
    return r.json()


def create_page(title: str, slug: str, content: str, parent: int = 0, template: str = "page-no-title"):
    body = {"title": title, "slug": slug, "content": content, "status": "publish", "parent": parent, "template": template}
    r = requests.post(f"{site}/wp-json/wp/v2/pages", auth=auth, json=body, timeout=30)
    r.raise_for_status()
    return r.json()


def main():
    print("Build & push page content")
    print("=" * 60)

    # Step 1: Home page
    content = build_page_content("mockup/index.html")
    p = update_page(10, "Oak Shield Service — Texas MEP Contractor", content, slug="home")
    print(f"✓ Updated home (ID {p['id']})  content len: {len(content):,}")

    # Step 2: Services
    content = build_page_content("mockup/services.html")
    p = update_page(12, "Services", content, slug="services")
    print(f"✓ Updated services (ID {p['id']})  content len: {len(content):,}")

    # Step 3: Company
    content = build_page_content("mockup/company.html")
    p = update_page(16, "Company", content, slug="company")
    print(f"✓ Updated company (ID {p['id']})  content len: {len(content):,}")

    # Step 4: Contact
    content = build_page_content("mockup/contact.html")
    p = update_page(22, "Contact", content, slug="contact")
    print(f"✓ Updated contact (ID {p['id']})  content len: {len(content):,}")

    # Step 5: Repurpose Projects → Markets parent
    markets_parent_content = '<!-- wp:html --><meta http-equiv="refresh" content="0; url=/markets/data-centers/"><!-- /wp:html -->'
    p = update_page(14, "Markets", markets_parent_content, slug="markets")
    print(f"✓ Repurposed Projects (ID {p['id']}) → Markets parent")

    # Step 6: Create 5 Markets pages
    markets = [
        ("data-centers", "Data Centers"),
        ("hospitality", "Hospitality"),
        ("cold-storage", "Cold Storage"),
        ("big-box-retail", "Big-Box Retail"),
        ("industrial", "Industrial"),
    ]
    for slug, title in markets:
        # Check if already exists
        existing = get_page(slug)
        content = build_page_content(f"mockup/markets/{slug}.html")
        if existing:
            p = update_page(existing["id"], title, content, slug=slug, parent=14)
            print(f"✓ Updated /markets/{slug}/ (ID {p['id']})  content len: {len(content):,}")
        else:
            p = create_page(title, slug, content, parent=14)
            print(f"✓ Created /markets/{slug}/ (ID {p['id']})  content len: {len(content):,}")


if __name__ == "__main__":
    main()

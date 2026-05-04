#!/usr/bin/env python3
"""Generate all Oak Shield static HTML pages.
Usage: python3 _build_pages.py
Outputs: services.html, projects.html, company.html, contact.html, markets/*.html
"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _partials import (
    head, announcement_bar, header, breadcrumb, page_hero,
    cta_band, footer, schema_local_business,
)

ROOT = os.path.dirname(os.path.abspath(__file__))


def write(path: str, content: str) -> None:
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full) or '.', exist_ok=True)
    with open(full, 'w') as f:
        f.write(content)
    print(f"  ✓ {path}  ({len(content):,} bytes)")


# ════════════════════════════════════════════════════════════════════════════
# SERVICES PAGE
# ════════════════════════════════════════════════════════════════════════════
def build_services():
    body = head(
        title="Commercial & Industrial MEP Services in Texas | Oak Shield Service",
        description="Self-performed commercial HVAC, industrial refrigeration, electrical and plumbing for Texas projects. Single point of accountability across all four trades.",
        canonical="https://oakshieldservice.com/services.html",
    ) + announcement_bar() + header(active="services") + breadcrumb([
        ("Home", "index.html"), ("Services", "")
    ]) + page_hero(
        eyebrow="// Services · Self-Performed MEP",
        title_html='Four trades. One responsibility chain.<br><span class="underline-safety">Mechanical, Electrical, Refrigeration &amp; Plumbing.</span>',
        subtitle="GCs and owners across Texas trust Oak Shield because all four trades flow through one estimating desk, one project manager, and one safety program — eliminating finger-pointing on RFIs, schedule slips and inspection holds.",
        image_path="../assets/generated/hero_mep_corridor.png",
        image_alt="Industrial MEP corridor — Oak Shield Service self-performed scope",
    )

    # Trade cards (deeper than home page)
    trades = [
        ("hvac", "01", "HVAC", "Commercial & Industrial",
         "Mechanical scope on new construction and retrofits across data centers, hospitality, cold-storage facilities and big-box retail. We own the airside from first equipment cut sheet to inspection sign-off.",
         [
            "Air distribution &amp; ductwork (sheetmetal trade-coordinated)",
            "Packaged rooftop units &amp; split systems",
            "VRF / VRV multi-zone systems",
            "Air handlers &amp; mechanical room build-outs",
            "Hydronic piping (chilled &amp; hot water)",
            "Test &amp; balance coordination",
            "Equipment setting &amp; rigging",
            "Mechanical retrofits in active facilities",
         ],
         "Costco Business Center · Stafford TX",
         "Equipment setting, ductwork, RTU coordination on a national-prototype big-box facility.",
         "project_costco_rooftop.png", "markets/big-box-retail.html"),

        ("refrigeration", "02", "Refrigeration & Cold Storage", "Food-grade & Industrial",
         "Walk-in coolers, freezers, process refrigeration and temperature-controlled storage built to food-grade and industrial code. We coordinate insulation, vapor barrier and refrigeration piping as one engineered system — not three uncoordinated subs.",
         [
            "Walk-in coolers &amp; freezers (custom &amp; modular)",
            "Process refrigeration piping",
            "Refrigeration insulation &amp; vapor barrier coordination",
            "Glycol &amp; secondary loop systems",
            "Compressor racks &amp; mechanical equipment rooms",
            "Blast freezing &amp; flash chill applications",
            "Temperature mapping &amp; commissioning",
            "Energy recovery (heat reclaim, condenser water, desuperheater integration)",
         ],
         "OCM Mushroom Cold Storage · Texas",
         "Industrial cold-storage facility refrigeration: walk-ins, piping, insulation and full system commissioning.",
         "project_ocm_coldstorage.png", "markets/cold-storage.html"),

        ("electrical", "03", "Electrical", "Mission-Critical · Distribution · Controls",
         "Power distribution, equipment connections, control wiring, low-voltage and mission-critical systems for data centers, manufacturing and large commercial. Self-perform from utility tie-in down to terminal device.",
         [
            "Medium- &amp; low-voltage distribution",
            "Mission-critical UPS &amp; generator integration",
            "Switchgear &amp; PDU installation",
            "Equipment power &amp; controls connections",
            "Cable tray / conduit infrastructure",
            "Lighting &amp; lighting controls",
            "Fire alarm &amp; life-safety systems coordination",
            "Inspection-driven energization sequencing",
         ],
         "NVIDIA Data Center · Dallas Area",
         "Mission-critical electrical subcontractor: power distribution, equipment connections, full system coordination.",
         "project_nvidia_dc.png", "markets/data-centers.html"),

        ("plumbing", "04", "Plumbing", "Commercial & Process",
         "Domestic water, sanitary, storm, and process plumbing as part of integrated MEP delivery. We own coordination handoffs with mechanical, electrical and structural to avoid clash-detection rework.",
         [
            "Domestic hot &amp; cold water distribution",
            "Sanitary &amp; storm drainage",
            "Backflow prevention (BPAT-certified testing) &amp; water treatment",
            "Process plumbing for industrial &amp; food-grade",
            "Medical / lab gas (where applicable)",
            "Fixture trim &amp; final connections",
            "Riser coordination through multi-story builds",
            "Pre-fab assemblies for schedule compression",
         ],
         "Blossom Hotel Houston · Houston TX",
         "Full-service hotel MEP: integrated mechanical, electrical and plumbing across guest rooms, kitchen and back-of-house.",
         "project_blossom_hotel.png", "markets/hospitality.html"),
    ]

    for slug, num, title, kicker, intro, scope, sig_title, sig_desc, sig_img, sig_link in trades:
        body += f"""
<section id="{slug}" class="paper-bg py-20 lg:py-28 border-b border-line/10 relative overflow-hidden">
  <div class="absolute right-0 top-0 -mt-8 mr-4 section-num pointer-events-none select-none">{num}</div>
  <div class="relative max-w-7xl mx-auto px-6">
    <div class="grid lg:grid-cols-12 gap-10">
      <div class="lg:col-span-5">
        <div class="text-xs uppercase tracking-[0.2em] safety font-bold mb-3">// {kicker}</div>
        <h2 class="display text-4xl lg:text-5xl font-extrabold leading-[1.04] mb-6">{title}</h2>
        <p class="text-base text-ink/70 leading-relaxed mb-8">{intro}</p>
        <a href="markets/data-centers.html" class="inline-flex items-center gap-2 text-sm font-bold safety border-b-2 border-current pb-1">
          See Markets We Serve
          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </a>
      </div>
      <div class="lg:col-span-7">
        <div class="bg-white border border-line/15 p-8 lg:p-10">
          <div class="text-[11px] safety font-bold uppercase tracking-[0.2em] mb-5">Self-Performed Scope</div>
          <ul class="grid sm:grid-cols-2 gap-x-6 gap-y-3 text-sm text-ink/80">
""" + "".join(f'            <li class="flex items-start gap-2 leading-relaxed"><span class="safety mt-1">▸</span><span>{s}</span></li>\n' for s in scope) + f"""          </ul>
          <div class="mt-7 pt-5 border-t border-line/15 flex items-center justify-between text-sm">
            <a href="{sig_link}" class="font-bold safety border-b border-current pb-0.5">See {kicker} projects &rarr;</a>
            <span class="text-xs text-ink/45 font-mono">{sig_title}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

    # Integrated MEP highlight
    body += """
<section class="ink-bg text-white py-24 relative overflow-hidden">
  <div class="absolute inset-0 grid-bg opacity-40"></div>
  <div class="relative max-w-7xl mx-auto px-6 grid lg:grid-cols-12 gap-12 items-center">
    <div class="lg:col-span-5">
      <div class="text-xs uppercase tracking-[0.2em] safety font-bold mb-4">// Integrated MEP</div>
      <h2 class="display text-4xl lg:text-5xl font-extrabold leading-tight">
        Why GCs combine all four<br>
        <span class="underline-safety">scopes under one contract.</span>
      </h2>
      <p class="mt-6 text-white/75 leading-relaxed">
        Treating MEP as one coordinated package — instead of four siloed subs — collapses the trade-stack RFI loop and shortens commissioning by weeks on complex projects. Owners get a single warranty desk, a single coordination meeting, and a single point of accountability.
      </p>
    </div>
    <div class="lg:col-span-7 grid sm:grid-cols-2 gap-px paper-bg/5 border border-line">
      <div class="ink2-bg p-7"><div class="text-3xl safety mb-3">→</div><h3 class="text-lg font-extrabold mb-2">One Estimating Desk</h3><p class="text-sm text-white/65 leading-relaxed">Cross-trade scope gaps caught at pricing, not at field discovery.</p></div>
      <div class="ink2-bg p-7"><div class="text-3xl safety mb-3">→</div><h3 class="text-lg font-extrabold mb-2">One Schedule</h3><p class="text-sm text-white/65 leading-relaxed">We sequence MEP internally — GC sees a single tied-out trade plan.</p></div>
      <div class="ink2-bg p-7"><div class="text-3xl safety mb-3">→</div><h3 class="text-lg font-extrabold mb-2">One Safety Program</h3><p class="text-sm text-white/65 leading-relaxed">Same site rules, same toolbox talks, same EMR for all four trades.</p></div>
      <div class="ink2-bg p-7"><div class="text-3xl safety mb-3">→</div><h3 class="text-lg font-extrabold mb-2">One Closeout</h3><p class="text-sm text-white/65 leading-relaxed">Unified O&amp;M binder, commissioning handoff and warranty contact.</p></div>
    </div>
  </div>
</section>
"""

    body += cta_band() + footer()
    write("services.html", body)


# ════════════════════════════════════════════════════════════════════════════
# PROJECTS PAGE (deep)
# ════════════════════════════════════════════════════════════════════════════
def build_projects():
    body = head(
        title="Featured Projects | Oak Shield Service — Texas MEP Contractor",
        description="Mission-critical data center electrical, big-box retail HVAC, full hotel MEP, and food-grade cold storage refrigeration. Real Texas builds with real GCs.",
        canonical="https://oakshieldservice.com/projects.html",
    ) + announcement_bar() + header(active="projects") + breadcrumb([
        ("Home", "index.html"), ("Projects", "")
    ]) + page_hero(
        eyebrow="// Projects · Featured Builds",
        title_html='Real scope. Real GCs.<br><span class="underline-safety">Real inspections passed.</span>',
        subtitle="Selected references demonstrating the project complexity, code rigor and multi-trade coordination Oak Shield routinely delivers across Texas commercial and industrial work.",
        image_path="assets/generated/project_nvidia_dc.png",
        image_alt="Featured projects across Texas commercial and industrial MEP",
    )

    cases = [
        ("project_nvidia_dc.png", "Mission-Critical Electrical", "Dallas, TX",
         "NVIDIA Data Center", "AI / HPC Hyperscale Facility",
         "Electrical subcontractor for a hyperscale data center supporting AI / HPC workloads. Scope included power distribution, mechanical equipment connections, and inspection-coordinated energization sequencing — built to mission-critical reliability standards.",
         [("Location", "Dallas Area, TX"), ("Client", "Hyperscale AI Operator"), ("GC", "[Confidential]"), ("Oak Shield Role", "Electrical Subcontractor")],
         ["Power distribution &amp; equipment connections", "Mechanical equipment electrical scope", "System coordination across phases", "Inspection-driven energization"],
         "markets/data-centers.html"),

        ("project_costco_rooftop.png", "HVAC", "Stafford, TX",
         "Costco Business Center", "Big-Box Retail / Warehouse Club",
         "HVAC subcontractor on a large-scale national prototype retail facility. Equipment setting, ductwork installation and multi-trade coordination during a fast-paced commercial build — built to Costco's national construction standards.",
         [("Location", "Stafford, TX"), ("Client", "Costco Wholesale"), ("Format", "National Prototype Build"), ("Oak Shield Role", "HVAC Subcontractor")],
         ["Rooftop unit setting &amp; rigging", "Ductwork &amp; air distribution", "Refrigerated case lineup coordination", "Trade-stack scheduling"],
         "markets/big-box-retail.html"),

        ("project_blossom_hotel.png", "Full MEP", "Houston, TX",
         "Blossom Hotel Houston", "Full-Service Hotel Development",
         "Full-discipline MEP on a full-service hotel development. Integrated mechanical, electrical and plumbing scope across guest tower, public spaces, kitchen and back-of-house. Single-point-of-accountability across all four trades.",
         [("Location", "Houston, TX"), ("Client", "Blossom Hotel Owner"), ("Vertical", "Full-Service Hotel"), ("Oak Shield Role", "MEP Contractor (All Trades)")],
         ["Mechanical: chilled water plant + AHU + VRF guest rooms", "Electrical: distribution + lighting + life-safety", "Plumbing: domestic + sanitary + kitchen / laundry", "Multi-trade coordination &amp; commissioning"],
         "markets/hospitality.html"),

        ("project_ocm_coldstorage.png", "Refrigeration", "Texas",
         "OCM Mushroom Cold Storage", "Food-Grade Industrial Refrigeration",
         "Refrigeration contractor on an industrial food processing facility. Walk-in coolers and freezers, refrigeration piping and insulation, with integrated controls and commissioning for temperature-controlled production environments.",
         [("Location", "Texas"), ("Client", "OCM Mushroom"), ("Vertical", "Food-Grade Industrial F&amp;B"), ("Oak Shield Role", "Refrigeration Contractor")],
         ["Walk-in cooler &amp; freezer construction", "Refrigeration piping &amp; insulation", "System integration &amp; controls", "Commissioning &amp; commissioning support"],
         "markets/cold-storage.html"),
    ]

    body += '<section class="paper-bg py-16">\n  <div class="max-w-7xl mx-auto px-6 space-y-16">\n'
    for i, (img, chip, loc, name, vert, desc, kvs, scope, link) in enumerate(cases):
        flip = i % 2 == 1
        body += f"""
    <article class="grid lg:grid-cols-12 gap-10 items-center {'' if not flip else 'lg:[direction:rtl]'}">
      <div class="lg:col-span-7 {'' if not flip else 'lg:[direction:ltr]'}">
        <div class="aspect-[16/10] overflow-hidden border border-line/15">
          <img src="assets/generated/{img}" alt="{name} — {vert}" class="w-full h-full object-cover"/>
        </div>
      </div>
      <div class="lg:col-span-5 {'' if not flip else 'lg:[direction:ltr]'}">
        <div class="flex items-center gap-3 mb-4">
          <span class="chip ink-bg text-white">{chip}</span>
          <span class="text-xs font-mono text-ink/40">{loc}</span>
        </div>
        <h2 class="display text-3xl lg:text-4xl font-extrabold leading-tight mb-2">{name}</h2>
        <div class="text-sm safety font-bold uppercase tracking-wider mb-5">{vert}</div>
        <p class="text-base text-ink/70 leading-relaxed mb-7">{desc}</p>
        <div class="grid grid-cols-2 gap-4 mb-7">
""" + "".join(f'          <div><div class="text-[10px] uppercase tracking-[0.18em] text-ink/45 mb-1">{k}</div><div class="text-sm font-extrabold">{v}</div></div>\n' for k, v in kvs) + f"""        </div>
        <ul class="space-y-1.5 text-sm text-ink/70 mb-7 border-t border-line/15 pt-5">
""" + "".join(f'          <li class="flex gap-2"><span class="safety mt-1">▸</span><span>{s}</span></li>\n' for s in scope) + f"""        </ul>
        <a href="{link}" class="inline-flex items-center gap-2 text-sm font-bold safety border-b-2 border-current pb-1">
          Explore this market vertical
          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </a>
      </div>
    </article>
"""
    body += '  </div>\n</section>\n'

    # Adjacent project types
    body += """
<section class="paper2-bg py-20">
  <div class="max-w-7xl mx-auto px-6">
    <div class="text-xs uppercase tracking-[0.2em] safety font-bold mb-4">// Beyond the Featured Four</div>
    <h2 class="display text-3xl lg:text-4xl font-extrabold leading-tight mb-10">Adjacent project types we are qualified for.</h2>
    <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-px paper-bg border border-line/15">
      <div class="paper2-bg p-7"><div class="text-[10px] safety font-bold uppercase tracking-[0.2em] mb-3">Hyperscale</div><div class="text-lg font-extrabold mb-2">AI / HPC Data Centers</div><p class="text-sm text-ink/65 leading-relaxed">Mission-critical electrical &amp; mechanical scope for Texas hyperscale build-outs.</p></div>
      <div class="paper2-bg p-7"><div class="text-[10px] safety font-bold uppercase tracking-[0.2em] mb-3">National Retail</div><div class="text-lg font-extrabold mb-2">Big-Box &amp; Grocery Rollouts</div><p class="text-sm text-ink/65 leading-relaxed">Multi-site HVAC and refrigeration on national prototype builds across Texas.</p></div>
      <div class="paper2-bg p-7"><div class="text-[10px] safety font-bold uppercase tracking-[0.2em] mb-3">Hospitality</div><div class="text-lg font-extrabold mb-2">Full-Service Hotel MEP</div><p class="text-sm text-ink/65 leading-relaxed">New-build and renovation MEP for hotel developments in Houston, Austin, San Antonio.</p></div>
      <div class="paper2-bg p-7"><div class="text-[10px] safety font-bold uppercase tracking-[0.2em] mb-3">Cold Chain</div><div class="text-lg font-extrabold mb-2">Food-Grade &amp; Pharma</div><p class="text-sm text-ink/65 leading-relaxed">Walk-in cooler/freezer, process refrigeration, and food-grade build standards.</p></div>
    </div>
  </div>
</section>
"""

    body += cta_band() + footer()
    write("projects.html", body)


# ════════════════════════════════════════════════════════════════════════════
# COMPANY PAGE
# ════════════════════════════════════════════════════════════════════════════
def build_company():
    body = head(
        title="About Oak Shield Service | Texas-Based MEP Contractor",
        description="Houston-based commercial & industrial MEP contractor. Self-performed HVAC, refrigeration, electrical and plumbing. Licensed in Texas, insured and bonded.",
        canonical="https://oakshieldservice.com/company.html",
    ) + announcement_bar() + header(active="company") + breadcrumb([
        ("Home", "index.html"), ("Company", "")
    ]) + page_hero(
        eyebrow="// Company · About Oak Shield",
        title_html='Texas-rooted.<br><span class="underline-safety">Built to win complex jobs.</span>',
        subtitle="Oak Shield Service was founded to give general contractors and owners a self-performing MEP partner that owns the full commitment chain — estimating through commissioning — without finger-pointing across four uncoordinated subs.",
        image_path="../assets/generated/market_industrial.png",
        image_alt="Oak Shield Service — Houston-based industrial MEP contractor",
    )

    body += """
<!-- STORY + KEY FACTS -->
<section class="paper-bg py-24">
  <div class="max-w-7xl mx-auto px-6 grid lg:grid-cols-12 gap-12">
    <div class="lg:col-span-7">
      <div class="text-xs uppercase tracking-[0.2em] safety font-bold mb-4">// Our Story</div>
      <h2 class="display text-3xl lg:text-4xl font-extrabold leading-tight mb-6">
        Why we built a single-point-of-accountability MEP shop.
      </h2>
      <div class="space-y-5 text-base text-ink/75 leading-relaxed">
        <p>
          The biggest source of cost and schedule risk on commercial and industrial projects isn&rsquo;t the work itself — it&rsquo;s the seams between the trades. RFIs that bounce between mechanical and electrical, refrigeration scope that gets re-designed once insulation arrives, plumbing risers that conflict with ductwork after sheetmetal is hung.
        </p>
        <p>
          Oak Shield was built to close those seams. We self-perform all four MEP disciplines under one estimating desk, one project manager, and one safety program. GCs get fewer subs to manage, owners get one warranty contact, and inspectors get one coordination story instead of four.
        </p>
        <p>
          We&rsquo;re Texas-based and Texas-licensed. We work where our crews can drive home — Houston, Dallas, Austin, San Antonio, and the I-10 / I-35 / I-45 build corridors connecting them. No travel mark-ups, no per-diem hidden in the bid sheet.
        </p>
      </div>
    </div>
    <div class="lg:col-span-5">
      <div class="ink-bg text-white p-8 lg:p-10">
        <div class="text-xs uppercase tracking-[0.2em] safety font-bold mb-6">// Quick Facts</div>
        <dl class="space-y-5 text-sm">
          <div class="flex justify-between gap-6 pb-4 border-b border-line"><dt class="text-white/55">Headquarters</dt><dd class="text-white font-bold text-right">Houston, TX</dd></div>
          <div class="flex justify-between gap-6 pb-4 border-b border-line"><dt class="text-white/55">Service Area</dt><dd class="text-white font-bold text-right">Texas Statewide</dd></div>
          <div class="flex justify-between gap-6 pb-4 border-b border-line"><dt class="text-white/55">Self-Performed Trades</dt><dd class="text-white font-bold text-right">HVAC · Refrig · Electrical · Plumbing</dd></div>
          <div class="flex justify-between gap-6 pb-4 border-b border-line"><dt class="text-white/55">Client Mix</dt><dd class="text-white font-bold text-right">GC / Owner / Design Teams</dd></div>
          <div class="flex justify-between gap-6"><dt class="text-white/55">Verticals</dt><dd class="text-white font-bold text-right">Data Center · Hospitality · Cold Storage · Retail · Industrial</dd></div>
        </dl>
      </div>
    </div>
  </div>
</section>

<!-- TRUST / COMPLIANCE -->
<section class="ink-bg text-white py-24 relative overflow-hidden">
  <div class="absolute inset-0 grid-bg opacity-40"></div>
  <div class="relative max-w-7xl mx-auto px-6">
    <div class="grid lg:grid-cols-12 gap-10 mb-12">
      <div class="lg:col-span-5">
        <div class="text-xs uppercase tracking-[0.2em] safety font-bold mb-4">// Compliance &amp; Safety</div>
        <h2 class="display text-3xl lg:text-4xl font-extrabold leading-tight">
          Licensed, insured, bonded —<br>
          <span class="underline-safety">prequalification-ready.</span>
        </h2>
      </div>
      <div class="lg:col-span-6 lg:col-start-7 flex items-end">
        <p class="text-white/70 leading-relaxed">
          We maintain the credentials and safety record GCs require to bring us onto enterprise and mission-critical work. Specific certificate documents available on request as part of prequalification.
        </p>
      </div>
    </div>

    <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-px paper-bg/5 border border-line">
      <div class="ink2-bg p-7"><div class="text-[10px] uppercase tracking-[0.2em] safety font-bold mb-3">Texas Licensing</div><div class="text-2xl font-extrabold mb-1">TACL &amp; TECL</div><div class="text-xs text-white/55">HVAC + Electrical Master · numbers on prequal</div></div>
      <div class="ink2-bg p-7"><div class="text-[10px] uppercase tracking-[0.2em] safety font-bold mb-3">Insurance</div><div class="text-2xl font-extrabold mb-1">GL · WC · Auto</div><div class="text-xs text-white/55">Certificates issued per project requirements</div></div>
      <div class="ink2-bg p-7"><div class="text-[10px] uppercase tracking-[0.2em] safety font-bold mb-3">Bonding</div><div class="text-2xl font-extrabold mb-1">Surety-backed</div><div class="text-xs text-white/55">Single &amp; aggregate capacity on request</div></div>
      <div class="ink2-bg p-7"><div class="text-[10px] uppercase tracking-[0.2em] safety font-bold mb-3">Prequalification</div><div class="text-2xl font-extrabold mb-1">Ready</div><div class="text-xs text-white/55">ISNetworld &middot; Avetta &middot; Veriforce capable</div></div>
    </div>
    <p class="mt-5 text-xs text-white/40 leading-relaxed">Full prequalification package — license numbers, COI, EMR detail, bonding capacity, safety program, and project references — available via the Capability Statement (instant) or Prequalification Package (within 1 business day).</p>

    <div class="mt-10 ink2-bg border border-line p-7 lg:p-8 grid lg:grid-cols-12 gap-6 items-center">
      <div class="lg:col-span-8">
        <div class="text-xs uppercase tracking-[0.2em] safety font-bold mb-2">// Capability Statement</div>
        <h3 class="text-2xl font-extrabold">Download our full Capability Statement (PDF)</h3>
        <p class="text-sm text-white/65 mt-2">Includes scope of self-performed trades, project references, license numbers, insurance limits, and bonding capacity. Sent on request to qualified GCs and owners.</p>
      </div>
      <div class="lg:col-span-4 flex justify-start lg:justify-end">
        <a href="contact.html#capability" class="btn-primary">
          Request Capability PDF
          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </a>
      </div>
    </div>
  </div>
</section>
"""

    body += cta_band() + footer()
    write("company.html", body)


# ════════════════════════════════════════════════════════════════════════════
# CONTACT PAGE (RFP form)
# ════════════════════════════════════════════════════════════════════════════
def build_contact():
    body = head(
        title="Contact & RFP Submission | Oak Shield Service Texas MEP",
        description="Submit your project inquiry or RFP to Oak Shield Service. Houston-based commercial & industrial MEP contractor. We respond to qualified bids within one business day.",
        canonical="https://oakshieldservice.com/contact.html",
    ) + announcement_bar() + header(active="contact") + breadcrumb([
        ("Home", "index.html"), ("Contact", "")
    ])

    body += """
<!-- HERO + RFP FORM -->
<section class="ink-bg text-white py-20 lg:py-28 relative overflow-hidden">
  <div class="absolute inset-0 grid-bg opacity-50"></div>
  <div class="absolute inset-0">
    <img src="../assets/generated/hero_mep_corridor.png" alt="" class="w-full h-full object-cover opacity-15"/>
    <div class="absolute inset-0 bg-gradient-to-r from-[#0B1220] via-[#0B1220]/90 to-[#0B1220]/60"></div>
  </div>
  <div class="relative max-w-7xl mx-auto px-6 grid lg:grid-cols-12 gap-12">
    <!-- Left: pitch + facts -->
    <div class="lg:col-span-5">
      <div class="text-xs uppercase tracking-[0.2em] safety font-bold mb-4">// Project Inquiry</div>
      <h1 class="display text-4xl lg:text-5xl font-extrabold leading-[1.04] mb-6">
        Send us scope.<br>
        <span class="underline-safety">We'll respond in one business day.</span>
      </h1>
      <p class="text-white/75 leading-relaxed mb-10">
        Use this form for project bids, prequalification submissions, or to request our Capability Statement. For quick scope discussions, call us directly.
      </p>

      <div class="space-y-5 mb-10">
        <a href="tel:+17138150552" class="block ink2-bg border border-line p-5 hover:border-safety transition-colors group">
          <div class="text-[10px] uppercase tracking-[0.2em] safety font-bold mb-1">// Direct Line</div>
          <div class="text-2xl font-extrabold group-hover:safety transition-colors">713-815-0552</div>
          <div class="text-xs text-white/55 mt-1">Estimating desk · weekdays 7 AM – 6 PM CT</div>
        </a>
        <a href="mailto:info@oakshieldservice.com" class="block ink2-bg border border-line p-5 hover:border-safety transition-colors group">
          <div class="text-[10px] uppercase tracking-[0.2em] safety font-bold mb-1">// Email</div>
          <div class="text-base font-extrabold group-hover:safety transition-colors break-all">info@oakshieldservice.com</div>
          <div class="text-xs text-white/55 mt-1">Attach drawings, specs, RFI logs as PDF</div>
        </a>
      </div>

      <div class="border-t border-line pt-6">
        <div class="text-[10px] uppercase tracking-[0.2em] safety font-bold mb-3">Service Area</div>
        <div class="text-sm text-white/85 font-bold mb-1">Texas Statewide</div>
        <div class="text-xs text-white/55 leading-relaxed">Headquartered in Houston · Active crews across Houston, Dallas, Austin, San Antonio &amp; the build corridors between.</div>
      </div>
    </div>

    <!-- Right: RFP form -->
    <div class="lg:col-span-7">
      <form id="rfp-form" class="ink2-bg border border-line p-8 lg:p-10 space-y-6" method="post" action="#">
        <div class="text-xs uppercase tracking-[0.2em] safety font-bold mb-2">// RFP Form</div>
        <h2 class="display text-2xl font-extrabold mb-1">Project Inquiry &amp; Capability Request</h2>
        <p class="text-sm text-white/55 mb-6">Required fields marked *. We treat all submissions as confidential.</p>

        <div class="grid sm:grid-cols-2 gap-5">
          <div>
            <label class="field-label">Full Name *</label>
            <input class="field-input" type="text" name="name" required>
          </div>
          <div>
            <label class="field-label">Company *</label>
            <input class="field-input" type="text" name="company" required>
          </div>
          <div>
            <label class="field-label">Role *</label>
            <select class="field-select" name="role" required>
              <option value="">Select your role…</option>
              <option>General Contractor — PM / Estimator</option>
              <option>Owner / Developer</option>
              <option>Design Team / Engineer</option>
              <option>Other</option>
            </select>
          </div>
          <div>
            <label class="field-label">Email *</label>
            <input class="field-input" type="email" name="email" required>
          </div>
          <div>
            <label class="field-label">Phone</label>
            <input class="field-input" type="tel" name="phone">
          </div>
          <div>
            <label class="field-label">Project Location</label>
            <input class="field-input" type="text" name="location" placeholder="City, TX">
          </div>
        </div>

        <div>
          <label class="field-label">Project Type *</label>
          <select class="field-select" name="project_type" required>
            <option value="">Select project type…</option>
            <option>Data Center (AI / HPC / Colo)</option>
            <option>Hospitality / Hotel</option>
            <option>Cold Storage / Refrigeration</option>
            <option>Big-Box Retail / Warehouse Club</option>
            <option>Industrial / Manufacturing / Process</option>
            <option>Other Commercial</option>
          </select>
        </div>

        <div>
          <label class="field-label">Scope Needed *</label>
          <div class="grid sm:grid-cols-2 gap-2 text-sm text-white/85">
            <label class="flex items-center gap-2 ink-bg border border-line p-3 hover:border-safety/60 cursor-pointer"><input type="checkbox" name="scope" value="hvac" class="accent-orange-500"> HVAC</label>
            <label class="flex items-center gap-2 ink-bg border border-line p-3 hover:border-safety/60 cursor-pointer"><input type="checkbox" name="scope" value="refrigeration" class="accent-orange-500"> Refrigeration</label>
            <label class="flex items-center gap-2 ink-bg border border-line p-3 hover:border-safety/60 cursor-pointer"><input type="checkbox" name="scope" value="electrical" class="accent-orange-500"> Electrical</label>
            <label class="flex items-center gap-2 ink-bg border border-line p-3 hover:border-safety/60 cursor-pointer"><input type="checkbox" name="scope" value="plumbing" class="accent-orange-500"> Plumbing</label>
            <label class="flex items-center gap-2 ink-bg border border-line p-3 hover:border-safety/60 cursor-pointer sm:col-span-2"><input type="checkbox" name="scope" value="full_mep" class="accent-orange-500"> Full integrated MEP (all four)</label>
          </div>
        </div>

        <div>
          <label class="field-label">Project Description *</label>
          <textarea class="field-textarea" name="description" rows="5" placeholder="Brief scope, square footage, target schedule, GC name (if applicable), and any relevant project standards or codes." required></textarea>
        </div>

        <div>
          <label class="field-label">Documents (Optional)</label>
          <input class="field-input" type="file" name="documents" multiple accept=".pdf,.dwg,.zip,.docx,.xlsx">
          <p class="text-[11px] text-white/40 mt-2">PDF / DWG / ZIP / DOCX / XLSX accepted. For large files, send via email.</p>
        </div>

        <div class="flex items-start gap-3 pt-2">
          <input type="checkbox" id="confirm" name="confirm_authority" required class="mt-1 accent-orange-500">
          <label for="confirm" class="text-xs text-white/65 leading-relaxed">
            I confirm I have authority to share this project information and authorize Oak Shield Service to contact me regarding this inquiry. *
          </label>
        </div>

        <div class="flex flex-col sm:flex-row gap-4 pt-2">
          <button type="submit" class="btn-primary justify-center">
            Submit Inquiry
            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </button>
          <a href="#capability" class="btn-ghost text-white justify-center"><span>Request Capability Statement Only</span></a>
        </div>

        <p class="text-[11px] text-white/40 pt-3 leading-relaxed">
          By submitting this form, you acknowledge that Oak Shield Service may contact you about your project. Your information is not shared with third parties.
        </p>
      </form>
    </div>
  </div>
</section>

<!-- CAPABILITY STATEMENT REQUEST (anchor) -->
<section id="capability" class="paper-bg py-20">
  <div class="max-w-7xl mx-auto px-6 grid lg:grid-cols-12 gap-12 items-center">
    <div class="lg:col-span-7">
      <div class="text-xs uppercase tracking-[0.2em] safety font-bold mb-4">// Capability Statement</div>
      <h2 class="display text-3xl lg:text-4xl font-extrabold leading-tight mb-5">
        One PDF. All the prequalification facts.
      </h2>
      <p class="text-base text-ink/70 leading-relaxed mb-6">
        Our Capability Statement is the single document you'll need to evaluate Oak Shield as a prequalified subcontractor. It includes our self-performed scope by trade, four signature project references, current license numbers, insurance limits, bonding capacity, and safety program highlights.
      </p>
      <ul class="space-y-2 text-sm text-ink/75 mb-8">
        <li class="flex gap-2"><span class="safety mt-1">▸</span><span>Scope by trade (HVAC, refrigeration, electrical, plumbing)</span></li>
        <li class="flex gap-2"><span class="safety mt-1">▸</span><span>Project references with role, vertical and scope notes</span></li>
        <li class="flex gap-2"><span class="safety mt-1">▸</span><span>License numbers (TACL / TECL) and insurance certificate summary</span></li>
        <li class="flex gap-2"><span class="safety mt-1">▸</span><span>Bonding capacity (single &amp; aggregate)</span></li>
        <li class="flex gap-2"><span class="safety mt-1">▸</span><span>Safety program &amp; prequalification platform compatibility</span></li>
      </ul>
    </div>
    <div class="lg:col-span-5">
      <div class="ink-bg text-white p-7 lg:p-8">
        <div class="text-xs uppercase tracking-[0.2em] safety font-bold mb-4">// Quick Request</div>
        <p class="text-sm text-white/75 mb-5">Email the Capability PDF to a single recipient — no full RFP needed.</p>
        <form class="space-y-4">
          <input class="field-input" type="text" name="cap_company" placeholder="Company *" required>
          <input class="field-input" type="email" name="cap_email" placeholder="Email *" required>
          <select class="field-select" name="cap_role">
            <option value="">Your role…</option>
            <option>General Contractor</option>
            <option>Owner / Developer</option>
            <option>Design Team</option>
            <option>Other</option>
          </select>
          <button type="submit" class="btn-primary w-full justify-center">Send Capability PDF</button>
        </form>
      </div>
    </div>
  </div>
</section>

<!-- OFFICE HOURS + MAP STRIP -->
<section class="ink-bg text-white py-16 border-t border-line">
  <div class="max-w-7xl mx-auto px-6 grid md:grid-cols-3 gap-px paper-bg/5 border border-line">
    <div class="ink2-bg p-7">
      <div class="text-xs uppercase tracking-[0.2em] safety font-bold mb-3">Office Hours</div>
      <div class="text-base font-bold mb-2">Mon – Fri · 7 AM – 6 PM CT</div>
      <p class="text-sm text-white/55">For urgent project coordination after hours, contact your assigned PM directly.</p>
    </div>
    <div class="ink2-bg p-7">
      <div class="text-xs uppercase tracking-[0.2em] safety font-bold mb-3">Headquarters</div>
      <div class="text-base font-bold mb-2">Houston, TX</div>
      <p class="text-sm text-white/55">Specific street address &amp; mailing details provided on request as part of prequalification.</p>
    </div>
    <div class="ink2-bg p-7">
      <div class="text-xs uppercase tracking-[0.2em] safety font-bold mb-3">Crew Coverage</div>
      <div class="text-base font-bold mb-2">Texas Statewide</div>
      <p class="text-sm text-white/55">Houston (HQ) · Dallas/Fort Worth · Austin · San Antonio + I-10, I-35, I-45 corridors. For projects outside these markets, ask us about partnered execution.</p>
    </div>
  </div>
</section>
"""

    body += footer()
    write("contact.html", body)


# ════════════════════════════════════════════════════════════════════════════
# MARKETS — SHARED RENDERER
# ════════════════════════════════════════════════════════════════════════════
def build_market_page(slug: str, market_name: str, hero_image: str, hero_alt: str,
                       title_h1: str, hero_subtitle: str,
                       intro_paragraph: str,
                       core_scope: list[str],
                       sig_image: str, sig_title: str, sig_loc: str,
                       sig_role: str, sig_vert: str, sig_desc: str, sig_bullets: list[str],
                       adjacent_chips: list[str],
                       seo_keywords: list[str],
                       faqs: list[tuple[str, str]],
                       meta_title: str, meta_desc: str):
    body = head(
        title=meta_title, description=meta_desc,
        canonical=f"https://oakshieldservice.com/markets/{slug}.html",
        og_image=f"../../assets/generated/{hero_image}",
        base_path="../",
    ) + announcement_bar() + header(active="markets", base="../") + breadcrumb([
        ("Home", "../index.html"), ("Markets", f"../markets/{slug}.html"), (market_name, "")
    ])

    # Hero
    body += f"""
<section class="relative ink-bg text-white overflow-hidden">
  <div class="absolute inset-0">
    <img src="../../assets/generated/{hero_image}" alt="{hero_alt}" class="w-full h-full object-cover opacity-50"/>
    <div class="absolute inset-0 bg-gradient-to-r from-[#0B1220] via-[#0B1220]/85 to-transparent"></div>
    <div class="absolute inset-0 grid-bg opacity-40"></div>
  </div>
  <div class="relative max-w-7xl mx-auto px-6 py-20 lg:py-32">
    <div class="max-w-3xl">
      <div class="flex items-center gap-3 mb-5">
        <span class="chip safety-bg text-white">Market · {market_name}</span>
        <span class="chip border border-white/20 text-white/70">Houston · DFW · Austin · SA</span>
      </div>
      <h1 class="display text-4xl lg:text-6xl font-extrabold leading-[1.04]">{title_h1}</h1>
      <p class="mt-6 text-base lg:text-lg text-white/75 leading-relaxed max-w-2xl">{hero_subtitle}</p>
      <div class="mt-9 flex flex-wrap gap-4">
        <a href="../contact.html" class="btn-primary">Discuss Your {market_name} Project<svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg></a>
        <a href="../contact.html#capability" class="btn-ghost text-white"><span>Request Capability PDF</span></a>
      </div>
    </div>
  </div>
</section>
"""

    # Why Oak Shield narrative (centered, no Texas map)
    body += f"""
<section class="paper-bg py-20 lg:py-24">
  <div class="max-w-3xl mx-auto px-6">
    <div class="text-xs uppercase tracking-[0.2em] safety font-bold mb-4 text-center">// Why Oak Shield for {market_name}</div>
    <p class="text-lg lg:text-xl text-ink/80 leading-[1.7] text-center font-light">{intro_paragraph}</p>
    <div class="mt-10 flex justify-center">
      <a href="../services.html" class="text-sm font-bold safety border-b-2 border-current pb-1">See our self-performed scope &rarr;</a>
    </div>
  </div>
</section>
"""

    # Project reference — left image, right text card (rolled back to prior layout)
    body += f"""
<section class="ink-bg text-white py-20 lg:py-24 relative overflow-hidden">
  <div class="absolute inset-0 grid-bg opacity-40"></div>
  <div class="relative max-w-7xl mx-auto px-6">
    <div class="text-xs uppercase tracking-[0.2em] safety font-bold mb-4">// Project Reference · {market_name}</div>
    <div class="grid lg:grid-cols-12 gap-10 items-center">
      <div class="lg:col-span-7">
        <div class="aspect-[16/10] overflow-hidden border border-line">
          <img src="../../assets/generated/{sig_image}" alt="{sig_title}" class="w-full h-full object-cover"/>
        </div>
      </div>
      <div class="lg:col-span-5">
        <h2 class="display text-3xl lg:text-4xl font-extrabold leading-tight mb-2">{sig_title}</h2>
        <div class="text-sm text-white/55 mb-1 font-mono">{sig_loc}</div>
        <div class="text-sm safety font-bold uppercase tracking-wider mb-5">{sig_vert}</div>
        <p class="text-base text-white/75 leading-relaxed mb-7">{sig_desc}</p>
        <div class="grid grid-cols-2 gap-5 mb-7">
          <div><div class="text-[10px] uppercase tracking-[0.18em] text-white/45 mb-1">Role</div><div class="text-sm font-extrabold">{sig_role}</div></div>
          <div><div class="text-[10px] uppercase tracking-[0.18em] text-white/45 mb-1">Vertical</div><div class="text-sm font-extrabold">{sig_vert}</div></div>
        </div>
        <ul class="space-y-2 text-sm text-white/75 border-t border-line pt-5">
""" + "".join(f'          <li class="flex gap-2"><span class="safety mt-1">▸</span><span>{s}</span></li>\n' for s in sig_bullets) + f"""        </ul>
      </div>
    </div>
  </div>
</section>
"""

    # Adjacent Builds section removed (was cluttering subpages with chip list)

    # FAQs (accordion)
    body += """
<section class="paper-bg py-20">
  <div class="max-w-7xl mx-auto px-6 grid lg:grid-cols-12 gap-10">
    <div class="lg:col-span-4">
      <div class="text-xs uppercase tracking-[0.2em] safety font-bold mb-4">// FAQ</div>
      <h2 class="display text-3xl lg:text-4xl font-extrabold leading-tight">Common questions from """ + f"{market_name.lower()}" + """ GCs and owners.</h2>
    </div>
    <div class="lg:col-span-8 space-y-3">
"""
    for q, a in faqs[:3]:  # only top 3 to keep page lean
        body += f"""      <details class="bg-white border border-line/15 group">
        <summary class="flex items-center justify-between p-6 cursor-pointer">
          <span class="text-base font-extrabold pr-4">{q}</span>
          <svg class="w-5 h-5 safety transition-transform group-open:rotate-45 flex-shrink-0" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"/></svg>
        </summary>
        <div class="px-6 pb-6 text-sm text-ink/70 leading-relaxed border-t border-line/15 pt-5">{a}</div>
      </details>
"""
    body += """    </div>
  </div>
</section>
"""

    # FAQ Schema
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs[:3]
        ],
    }
    import json
    body += f'\n<script type="application/ld+json">{json.dumps(faq_schema, indent=2)}</script>\n'

    body += cta_band(base="../") + footer(base="../")
    write(f"markets/{slug}.html", body)


# ════════════════════════════════════════════════════════════════════════════
# 5 MARKETS DEFINITIONS
# ════════════════════════════════════════════════════════════════════════════
def build_data_centers():
    build_market_page(
        slug="data-centers",
        market_name="Data Centers",
        hero_image="market_data_center.png",
        hero_alt="Hyperscale data center exterior in Texas at sunset — outdoor chillers, transformer yard and substation",
        title_h1='Mission-critical electrical &amp; mechanical for <span class="underline-safety">Texas data centers.</span>',
        hero_subtitle="Texas is the new center of gravity for AI / HPC build-outs — from Stargate Abilene to Meta and Google expansions across DFW. Oak Shield delivers self-performed mission-critical electrical and mechanical scope for hyperscale, colo, and edge data center facilities.",
        intro_paragraph="Mission-critical builds don&rsquo;t reward marketing — they reward partners who&rsquo;ve passed the inspections and sequenced live energization at scale. Our NVIDIA-supporting build in Dallas is that experience. We bring it to new hyperscale and colo work across Texas, with one trade partner for power distribution and mechanical integration instead of two finger-pointing subs.",
        core_scope=[
            "Medium- &amp; low-voltage power distribution",
            "PDU / RPP installation &amp; integration",
            "Generator &amp; UPS connection scope",
            "Mechanical equipment electrical (chiller, AHU, CRAH)",
            "Cable tray &amp; conduit infrastructure",
            "Switchgear setting &amp; interconnect",
            "BMS / EPMS coordination &amp; final terminations",
            "Mission-critical commissioning support",
        ],
        sig_image="project_nvidia_dc.png",
        sig_title="NVIDIA Data Center · Dallas",
        sig_loc="Dallas Area, TX · Phase 02",
        sig_role="Electrical Subcontractor",
        sig_vert="AI / HPC Hyperscale Data Center",
        sig_desc="Self-performed electrical scope including power distribution, mechanical equipment connections, and inspection-driven energization sequencing on a hyperscale facility supporting AI and HPC workloads.",
        sig_bullets=[
            "Power distribution &amp; equipment electrical scope",
            "System coordination across construction phases",
            "Mission-critical energization sequencing",
            "Mechanical &amp; cooling equipment connection",
        ],
        adjacent_chips=[
            "Hyperscale AI / HPC", "Stargate Abilene-class", "xAI Colossus-class", "Meta Texas DCs",
            "Google Texas DCs", "Colo / Multi-tenant", "Edge data center / micro-DC",
            "Crypto / mining facility", "Pharma research compute", "University HPC",
        ],
        seo_keywords=[
            "data center electrical contractor texas", "data center electrical contractor dallas",
            "data center mep contractor texas", "hyperscale electrical subcontractor",
            "ai data center electrical texas", "mission critical electrical contractor",
            "power distribution data center", "switchgear installation dallas",
            "data center commissioning electrical", "colo facility electrical texas",
        ],
        faqs=[
            ("Do you perform mission-critical electrical for AI / hyperscale data centers?",
             "Yes. Our Dallas-area NVIDIA-supporting build was a hyperscale-class electrical scope: power distribution, equipment connections, and inspection-coordinated energization. We extend that capability across new AI / HPC, colo, and edge data center work throughout Texas."),
            ("Can you self-perform both mechanical and electrical at the same DC site?",
             "Yes — that's a core reason GCs and owners hire us. Combining mechanical (CRAH, AHU, chiller integration) and electrical (PDU, switchgear, generator interconnect) under one trade partner collapses the multi-trade RFI loop and shortens commissioning."),
            ("Are you prequalified on major data center GCs and platforms?",
             "We carry the licenses, insurance limits, and safety program needed for prequalification on enterprise data center GCs. Specific platform compatibility (ISNetworld, Avetta, Veriforce) and certificate documents available on request as part of prequalification."),
            ("Where in Texas can you support data center builds?",
             "Statewide. We staff active crews across Houston, Dallas / Fort Worth, Austin, San Antonio, and the Abilene / DFW build corridors where AI hyperscale activity is concentrated."),
        ],
        meta_title="Data Center Electrical Contractor in Texas | Oak Shield Service",
        meta_desc="Mission-critical electrical & mechanical for AI, HPC, hyperscale and colo data centers across Texas. NVIDIA Dallas data center subcontractor. Power distribution, equipment connections, system coordination.",
    )


def build_hospitality():
    build_market_page(
        slug="hospitality",
        market_name="Hospitality",
        hero_image="market_hospitality.png",
        hero_alt="Hotel mechanical penthouse overlooking Houston skyline at dusk — chilled water plant and color-coded MEP piping",
        title_h1='Full MEP for <span class="underline-safety">Texas hotels and hospitality builds.</span>',
        hero_subtitle="From flagship downtown hotels to mid-scale select-service builds, hospitality projects demand integrated mechanical, electrical and plumbing executed under guest-facing schedule pressure. Oak Shield self-performs all four trades — single point of accountability from kickoff to final guest-room punch.",
        intro_paragraph="Hospitality schedules don&rsquo;t slip without missing a stabilized opening date. Oak Shield runs all four MEP trades under one PM — guest-tower risers, kitchen plumbing, life-safety, BMS integration — so the GC manages one warranty desk instead of four. Blossom Hotel Houston is the working template.",
        core_scope=[
            "Guest tower mechanical (VRF / fan-coil / chilled water)",
            "Public-space air handlers &amp; energy recovery",
            "Kitchen &amp; laundry process plumbing",
            "Domestic water systems &amp; recirculation",
            "Sanitary &amp; storm risers across multi-story stacks",
            "Electrical distribution + lighting + life-safety",
            "Pool / spa equipment electrical &amp; controls",
            "Final commissioning &amp; punch coordination",
        ],
        sig_image="project_blossom_hotel.png",
        sig_title="Blossom Hotel Houston",
        sig_loc="Houston, TX",
        sig_role="MEP Contractor (Full Scope)",
        sig_vert="Full-Service Hotel Development",
        sig_desc="Integrated mechanical, electrical and plumbing across guest tower, public spaces, kitchen and back-of-house. Single-point-of-accountability through construction sequencing and commissioning.",
        sig_bullets=[
            "Mechanical: chilled water plant + AHU + guest-room VRF",
            "Electrical: distribution, lighting, life-safety integration",
            "Plumbing: domestic + sanitary + kitchen / laundry process",
            "Multi-trade coordination &amp; commissioning",
        ],
        adjacent_chips=[
            "Marriott full-service", "Hilton flagship", "IHG mid-scale", "Hyatt boutique",
            "Resort / spa / convention", "Limited-service select-service", "Extended-stay",
            "Boutique &amp; lifestyle hotels", "Hotel renovation / re-flag",
        ],
        seo_keywords=[
            "hotel mep contractor houston", "hospitality mep contractor texas",
            "hotel hvac contractor houston", "commercial hotel plumbing contractor",
            "hotel electrical contractor texas", "full mep contractor hospitality",
            "hotel renovation mep texas", "luxury hotel mep contractor",
            "select service hotel hvac", "boutique hotel mechanical contractor",
        ],
        faqs=[
            ("Do you self-perform all four MEP trades on hotel projects?",
             "Yes. That's specifically why Oak Shield works well on hospitality — guest-tower coordination needs one point of accountability across mechanical, electrical and plumbing. Refrigeration enters the conversation on kitchen and back-of-house scope."),
            ("Can you keep schedule with a stabilized hotel opening date?",
             "Yes. Hospitality schedules can't slip without missing reservation windows. We sequence MEP to inspectors and to final guest-room punch — not to ourselves. We pre-fab plumbing risers and electrical assemblies where it compresses schedule."),
            ("What hotel verticals are within your scope?",
             "Full-service hotels (our Blossom Hotel template), select-service, extended-stay, and renovation / re-flag. Other formats — boutique, resort, convention — through our hospitality experience and partner network. Scope to your project format."),
            ("Where in Texas do you support hotel builds?",
             "Statewide — Houston, Dallas, Austin, San Antonio and the I-35 / I-10 corridors where hotel development activity is concentrated."),
            ("Do you handle kitchen and laundry equipment connections?",
             "Yes. Kitchen and laundry are some of the most demanding scopes in hotel MEP — process plumbing, exhaust hoods, electrical / gas connections and life-safety. We self-perform the plumbing and electrical and coordinate refrigeration."),
        ],
        meta_title="Hotel MEP Contractor in Houston & Texas | Oak Shield Service",
        meta_desc="Full-service hotel MEP contractor in Texas — mechanical, electrical, plumbing, refrigeration. Houston Blossom Hotel reference. Marriott, Hilton, IHG, Hyatt brand-standard build experience.",
    )


def build_cold_storage():
    build_market_page(
        slug="cold-storage",
        market_name="Cold Storage",
        hero_image="market_cold_storage.png",
        hero_alt="Industrial cold storage warehouse aisle with overhead refrigeration coils and arctic blue lighting in Texas",
        title_h1='Food-grade refrigeration &amp; <span class="underline-safety">cold storage build-outs in Texas.</span>',
        hero_subtitle="Texas port-driven cold-chain demand keeps growing — Houston, Laredo and Dallas distribution hubs feed both domestic supply chains and cross-border trade. Oak Shield delivers food-grade walk-in coolers, freezers, process refrigeration and integrated cold-storage MEP for industrial, 3PL and food production facilities.",
        intro_paragraph="Refrigeration projects fail at the seams between insulation, piping, and structural — not on any single trade. We deliver cold storage as one engineered package, not three uncoordinated subs. OCM Mushroom is the working reference: walk-ins, piping, insulation, controls and commissioning under one self-performed scope.",
        core_scope=[
            "Walk-in cooler &amp; freezer construction (custom &amp; modular)",
            "Refrigeration piping (suction, liquid, hot gas)",
            "Vapor barrier &amp; insulation coordination",
            "Compressor rack &amp; mechanical equipment rooms",
            "Glycol / secondary loop systems",
            "Process refrigeration &amp; blast freezing",
            "Refrigeration controls &amp; monitoring",
            "Commissioning &amp; temperature mapping",
        ],
        sig_image="project_ocm_coldstorage.png",
        sig_title="OCM Mushroom Cold Storage Facility",
        sig_loc="Texas",
        sig_role="Refrigeration Contractor",
        sig_vert="Food-Grade Industrial Refrigeration",
        sig_desc="Industrial food processing facility refrigeration: walk-in coolers and freezers, refrigeration piping and insulation, with full system integration and commissioning for temperature-controlled production environments.",
        sig_bullets=[
            "Walk-in cooler &amp; freezer construction",
            "Refrigeration piping &amp; insulation coordination",
            "System integration &amp; controls",
            "Food-grade commissioning &amp; temperature validation",
        ],
        adjacent_chips=[
            "3PL cold distribution centers", "Meat &amp; seafood processing", "Dairy &amp; frozen dessert",
            "Pharma &amp; vaccine cold chain", "Beverage / brewery", "Produce &amp; floral",
            "Mushroom / food production", "Restaurant central kitchens", "Cross-border export prep",
        ],
        seo_keywords=[
            "cold storage contractor texas", "food grade cold storage contractor texas",
            "industrial refrigeration contractor houston", "walk in freezer installation houston",
            "ammonia refrigeration contractor texas", "blast freezer contractor texas",
            "process refrigeration contractor texas", "3pl cold storage builder texas",
            "pharma cold storage contractor", "refrigeration piping installer texas",
        ],
        faqs=[
            ("Do you handle food-grade walk-in cooler and freezer build-outs?",
             "Yes — that's exactly the OCM Mushroom scope. Food-grade construction means tight insulation / vapor barrier coordination, sanitary-finish materials, and commissioning to temperature mapping requirements. We self-perform that scope under one contract."),
            ("Can you do ammonia refrigeration as well as freon / HFC?",
             "We routinely deliver freon / HFC / HFO refrigeration on industrial cold storage. For ammonia (anhydrous) systems we carry the qualifications and partner with specialized refrigerant licensing where required. Tell us what your refrigerant strategy is and we'll map a clean execution plan."),
            ("Can you sequence cold-storage scope inside an active food production facility?",
             "Yes. Production-facility refrigeration retrofits demand strict downtime windows, sanitation rules and FDA / USDA inspection awareness. We sequence to production calendars and sanitation requirements."),
            ("Where in Texas do you cover for cold storage work?",
             "Statewide. Cold-chain demand concentrates around Houston (port), Dallas (distribution), Laredo (cross-border) and the I-10 / I-35 corridors. We staff active crews accordingly."),
        ],
        meta_title="Cold Storage Refrigeration Contractor in Texas | Oak Shield Service",
        meta_desc="Food-grade walk-in coolers, freezers, process refrigeration and cold-storage MEP across Texas. OCM Mushroom reference build. Industrial 3PL cold-chain, pharma and food processing experience.",
    )


def build_big_box():
    build_market_page(
        slug="big-box-retail",
        market_name="Big-Box Retail",
        hero_image="market_big_box.png",
        hero_alt="Aerial view of big-box retail rooftop in Texas with grid of commercial RTU HVAC packaged units at golden hour",
        title_h1='HVAC &amp; refrigeration for <span class="underline-safety">national-prototype retail builds.</span>',
        hero_subtitle="National retail brands run on prototype standards — same RTU schedule, same refrigerated case lineup, same commissioning checklist on every build. Oak Shield delivers HVAC and refrigeration to those exact standards across Texas big-box retail and warehouse-club facilities.",
        intro_paragraph="National retail brands run on prototype standards — same RTU schedule, same case lineups, same closeout binder on every store. The GC wants no surprises; corporate construction wants the same documentation they got on the last fifteen openings. Oak Shield&rsquo;s Costco Business Center build in Stafford was executed to that exact standard.",
        core_scope=[
            "Rooftop unit setting &amp; rigging",
            "Ductwork, registers &amp; air balancing",
            "Refrigerated case lineups &amp; rack systems",
            "Walk-in coolers / freezers (back-of-house)",
            "Make-up air units &amp; exhaust",
            "Mechanical room build-out",
            "Trade-stack scheduling for fast-track schedules",
            "Prototype-document closeout package",
        ],
        sig_image="project_costco_rooftop.png",
        sig_title="Costco Business Center · Stafford",
        sig_loc="Stafford, TX",
        sig_role="HVAC Subcontractor",
        sig_vert="Big-Box Warehouse-Club Retail",
        sig_desc="Equipment setting, ductwork installation and multi-trade coordination on a large-scale national prototype facility — built to Costco&rsquo;s national construction standards and inspection sequencing.",
        sig_bullets=[
            "Rooftop unit setting &amp; rigging",
            "Ductwork &amp; air distribution",
            "Refrigerated case lineup coordination",
            "National prototype documentation closeout",
        ],
        adjacent_chips=[
            "Walmart / Sam&rsquo;s Club", "Target / Super Target", "HEB / HEB plus!", "Home Depot / Lowe&rsquo;s",
            "Costco / BJ&rsquo;s", "Best Buy", "Multi-site rollout programs", "Grocer remodels", "Warehouse club refresh",
        ],
        seo_keywords=[
            "commercial hvac contractor stafford texas", "big box hvac contractor texas",
            "warehouse club hvac contractor", "national prototype hvac contractor texas",
            "retail rooftop unit contractor texas", "refrigerated case installation texas",
            "grocer hvac contractor houston", "multi site retail hvac contractor",
            "costco hvac subcontractor texas", "walmart prototype hvac contractor",
        ],
        faqs=[
            ("Do you build to national-prototype standards?",
             "Yes. Big-box and warehouse-club brands run on tight prototype documents — same RTU schedule, same case lineups, same closeout binder across every build. Oak Shield&rsquo;s Costco scope was executed to that exact standard."),
            ("Can you self-perform both HVAC and refrigeration at retail sites?",
             "Yes. Most big-box and grocery-format retail needs both — comfort cooling RTUs plus refrigerated case lineups. Combining the two scopes under one trade partner collapses commissioning timeline."),
            ("Are you set up for multi-site retail rollouts?",
             "Yes. We&rsquo;ve built around the cadence multi-site programs need: staged crews, prototype documentation, and a single PM who knows the brand standard across stores."),
            ("Where in Texas do you cover for big-box retail?",
             "Statewide. Big-box build activity concentrates around the major metros — Houston, Dallas / Fort Worth, Austin, San Antonio — but we follow GC programs into smaller markets along the I-35 / I-10 / I-45 corridors."),
            ("What about grocer / supermarket builds and remodels?",
             "Grocery is squarely in scope — refrigerated case lineups, walk-ins, RTUs and process exhaust. Both ground-up new builds and live-store remodels (with the night-work and store-impact rules that come with them)."),
        ],
        meta_title="Big-Box Retail HVAC Contractor in Texas | Oak Shield Service",
        meta_desc="National prototype HVAC and refrigeration for big-box retail and warehouse-club builds across Texas. Costco Business Center Stafford TX reference. Walmart, Sam's, HEB, Target prototype experience.",
    )


def build_industrial():
    build_market_page(
        slug="industrial",
        market_name="Industrial",
        hero_image="market_industrial.png",
        hero_alt="Industrial process plant interior in Texas with stainless steel piping, cable trays and overhead MEP coordination zone",
        title_h1='Process &amp; manufacturing MEP — <span class="underline-safety">built for live facilities.</span>',
        hero_subtitle="Manufacturing, process and industrial builds put MEP under hard rules: production schedules can&rsquo;t slip, downtime windows are short, and inspectors are watching. Oak Shield delivers self-performed mechanical, electrical, refrigeration and plumbing for industrial Texas — sequencing scope around production, not against it.",
        intro_paragraph="Industrial owners don&rsquo;t need another trade partner who blows production schedules with field surprises. They need MEP sequenced to outage windows, inspections, and sanitation requirements — with one PM authorized to call cross-trade decisions in real time. That&rsquo;s how we work.",
        core_scope=[
            "Process exhaust &amp; ventilation",
            "High-amp power distribution &amp; transformers",
            "Compressed air &amp; process gas piping",
            "Chiller &amp; boiler integration",
            "Equipment power &amp; controls connections",
            "Plant retrofit &amp; tie-in",
            "Process plumbing &amp; backflow",
            "Outage-window sequencing",
        ],
        sig_image="market_industrial.png",
        sig_title="Process &amp; Manufacturing MEP",
        sig_loc="Texas Statewide · GC Partner Pipeline",
        sig_role="Self-Performed MEP Contractor",
        sig_vert="Industrial Manufacturing &amp; Process",
        sig_desc="Multi-trade MEP for active manufacturing and process facilities — engineered to operate alongside production schedules with strict downtime, sanitation and inspection windows.",
        sig_bullets=[
            "Process piping &amp; high-tonnage scope",
            "24 / 7 production-aware sequencing",
            "High-amp electrical distribution",
            "Plant retrofit &amp; tie-in coordination",
        ],
        adjacent_chips=[
            "Food &amp; beverage processing", "Battery / EV manufacturing", "Aerospace assembly",
            "Oil &amp; gas downstream", "Chemical &amp; petrochem", "Plastics / polymer", "Pharma manufacturing",
            "Semiconductor support facilities", "Automotive plants", "Industrial laundry &amp; commissary",
        ],
        seo_keywords=[
            "industrial mep contractor texas", "process piping contractor texas",
            "manufacturing electrical contractor houston", "industrial hvac contractor texas",
            "industrial plumbing contractor texas", "plant retrofit mep contractor",
            "ev battery plant electrical texas", "aerospace mep contractor texas",
            "petrochem electrical contractor texas", "industrial process refrigeration texas",
        ],
        faqs=[
            ("Can you sequence MEP scope inside an active production facility?",
             "Yes — that&rsquo;s the core of industrial work. We sequence to production calendars, downtime windows and inspection requirements. Pre-fab assemblies are used aggressively to compress field time."),
            ("Do you self-perform all four MEP trades on industrial sites?",
             "Yes. Industrial owners specifically benefit from a single point of accountability across mechanical, electrical, plumbing and refrigeration — fewer contracts to manage, fewer warranty contacts, faster commissioning."),
            ("What industrial verticals are in scope?",
             "Demonstrated capabilities: food &amp; beverage processing, industrial cold storage. Approached through our 4-trade self-perform model: battery / EV facilities, manufacturing retrofit, plastics, pharma support facilities. Tell us your vertical and we&rsquo;ll map fit honestly — including referring you elsewhere if it&rsquo;s outside our core capability."),
            ("Can you handle process piping and high-amp electrical at the same site?",
             "Yes. That combination is common on manufacturing and process work — we self-perform the process piping and the electrical distribution under one trade partner."),
            ("Where in Texas do you support industrial work?",
             "Statewide. Industrial activity concentrates around Houston (petrochem, port, manufacturing), Dallas (advanced manufacturing, EV, aerospace), Austin (semiconductor / EV) and San Antonio (food / industrial). We staff crews accordingly."),
        ],
        meta_title="Industrial MEP Contractor in Texas | Oak Shield Service",
        meta_desc="Process and manufacturing MEP across Texas — HVAC, electrical, plumbing, refrigeration. Battery / EV, aerospace, petrochem, food & beverage, semiconductor support. Production-aware sequencing.",
    )


# ════════════════════════════════════════════════════════════════════════════
# RUN
# ════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("Building static pages…\n")
    build_services()
    build_company()
    build_contact()
    print()
    build_data_centers()
    build_hospitality()
    build_cold_storage()
    build_big_box()
    build_industrial()
    print("\nDone.")

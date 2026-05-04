# Oak Shield 网站文案优化清单 — 不需要老板回填的部分

> **本文档定位**: 与 `04_industry_expert_audit.md` (审计) 和 `Oak_Shield_Owner_Questionnaire_v1.docx` (问卷) 配套。
>
> 审计指出的 65 项问题中,**33 项需要老板提供新数据** (在问卷里);**32 项可以基于现有内容直接重写优化**。本文是后者的逐项执行清单,改完就能合入下一版 mockup。
>
> 编写日期: 2026-05-04
> 修订涉及文件: `mockup/index.html`, `mockup/services.html`, `mockup/company.html`, `mockup/contact.html`, `mockup/markets/*.html`
> 优化项数: **32 条** (按页面分组)

---

## 优化原则

| 原则 | 应用方式 |
|---|---|
| **不夸大** | 把 "Mission-critical UPS install" 这种外行听着唬人但内行一查就漏的措辞改成精确范围 |
| **不模糊** | 把 "where applicable" / "as needed" / "specialized partner where required" 这种留逃跑余地的话术改成明确表达 |
| **不重复** | 4 页都在讲 "self-perform 4 trades" — 提炼成一句 tagline,各页只讲该页的 angle |
| **不假装** | "Texas Statewide" 改成 "Houston-based · Texas Build Corridors" 才不会被 Lubbock 项目验证 |
| **不滥用术语** | "Hyperscale" 严格 ≥100MW;"NVIDIA-tenant" 改 "NVIDIA-class workloads";"Mission-Critical" 不滥用 |

---

## 一、页面级 — 全站结构性问题

### 1.1 ⭐ Schema.org Type 改正 (5 文件全改)

**位置**: services.html / company.html / markets/*.html (5 个) 末尾的 JSON-LD

**当前**:
```json
{ "@type": "GeneralContractor", ... }
```

**改成**:
```json
{
  "@type": ["LocalBusiness", "HVACBusiness", "ElectricalContractor", "Plumber"],
  ...
}
```

**理由**: Oak Shield 是 MEP **Subcontractor**,不是 GeneralContractor。Google 看 schema 决定 SERP 分类,当前等于告诉 Google 推 GC 类目客户 — 客户搜的是 "MEP subcontractor in Texas" 找不到你。

---

### 1.2 ⭐ JSON-LD 移到 `</body>` 之前

**位置**: services.html line 500 `</html>` 之后才是 `<script>`,company.html / 5 markets 同问题

**当前结构**: `</html>` ... `<script type="application/ld+json">` ... `</script>`

**改成**: 把 `<script>` 移到 `</body>` 之前(在 `</html>` 之前)

**理由**: HTML5 规范要求 `<script>` 在 `<head>` 或 `<body>` 内。Google Rich Results Test 跳过 `</html>` 之后的内容。当前等于 schema SEO 0 效果。

---

### 1.3 ⭐ Schema 字段补完整

**位置**: 同上 5 文件

**新增字段** (基于问卷 6.4-6.6 老板回填后填):

```json
{
  "@type": ["LocalBusiness", "HVACBusiness", "ElectricalContractor", "Plumber"],
  "@id": "https://oakshieldservice.com/#org",
  "name": "Oak Shield Service LLC",
  "founder": { "@type": "Person", "name": "[Founder Name]" },
  "foundingDate": "[YYYY]",
  "numberOfEmployees": { "@type": "QuantitativeValue", "value": "[number]" },
  "image": "https://oakshieldservice.com/assets/logo.png",
  "logo": "https://oakshieldservice.com/assets/logo.png",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Real Street Address]",
    "addressLocality": "Houston",
    "addressRegion": "TX",
    "postalCode": "[ZIP]",
    "addressCountry": "US"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": "[lat]", "longitude": "[lng]" },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "07:00", "closes": "18:00"
  }],
  "sameAs": [
    "https://www.linkedin.com/company/[handle]",
    "https://www.facebook.com/[handle]",
    "https://g.page/[google-business-profile]"
  ],
  "knowsAbout": [...] // 保留现有
}
```

**理由**: Google Local Pack + Knowledge Panel 都依赖这些字段。当前缺一半,LocalBusiness SEO 拿不到分数。

---

### 1.4 ⭐ Footer "TBD" 上线前必须清零

**位置**:
- index.html line 1178-1179: `<span>TACL # — TBD</span>` `<span>TECL # — TBD</span>`
- 其他 4 页 line ~400: `<div>TACL # <span class="text-white/35">[pending]</span> · TECL # <span class="text-white/35">[pending]</span></div>`

**改成** (基于问卷 1.2 回填):
```html
<span>TACL-A · #XXXXXX · TECL · #XXXXXX</span>
```

或 (如老板暂不公开个人 master 信息):
```html
<span>Texas Licensed · TACL-A & TECL · Numbers on prequalification</span>
```

**禁止**上线时全文出现 `TBD` 或 `[pending]`。访客一眼看到 = "这家公司还没准备好"。

---

## 二、index.html (首页)

### 2.1 Hero CTA 重复

**位置**: index.html line 360-361 (header CTA) + line 426-431 (hero CTA) + line 580 (services 末尾) + line 846 (markets 末尾) + line 1116 (form button)

**问题**: `Request Capability Statement` / `Discuss Your Project` / `Let's Work Together` / `Submit RFP` 等近义 CTA 反复出现,但点击全跳 `contact.html`,导致用户不知道点哪个。

**优化**: CTA 二级化

| 层级 | 文案 | 目标 |
|---|---|---|
| **Primary** (橙色按钮) | `Submit Project Inquiry` | → contact.html#rfp |
| **Secondary** (灰描边) | `Download Capability Statement (PDF)` | → 弹 Lead Form modal,直接发 PDF |
| **Tertiary** (text link) | `or call 713-815-0552` | → tel: |

每个区块只用 1-2 个 CTA,不混用。

---

### 2.2 Hero 副标题措辞

**位置**: index.html line 423-425

**当前**:
```
HVAC, refrigeration, electrical and plumbing — under one estimating desk,
one project manager, one accountability chain.
```

**问题**: "one accountability chain" 是抽象概念 chain,英语 native B2B 读着像翻译腔。

**改成**:
```
HVAC, refrigeration, electrical and plumbing — one estimating desk,
one project manager, one warranty contact.
```

**理由**: "warranty contact" 是 GC 在合同后期最在意的事,具象化。

---

### 2.3 Client Logo Wall 旁边的 4 个 chip

**位置**: index.html line 466-469

**当前**:
```
· Mission-critical electrical
· Big-box retail HVAC
· Full-service hotel MEP
· Food-grade cold storage
```

**问题**: 4 个 chip 都是泛词,跟 "我们做的事" 没绑定。

**改成** (与上面 4 个 logo 一一对应):
```
· Hyperscale electrical · Dallas
· Big-box HVAC · Stafford
· Full-service hotel MEP · Houston
· Food-grade refrigeration · TX
```

**理由**: 让 chip 给 logo 背书,而不是 "另起一个语境"。

---

### 2.4 Services 卡片 — Plumbing 措辞调整

**位置**: index.html line 567-569

**当前**:
```
Commercial & industrial plumbing as part of integrated MEP delivery.
Water supply, drainage, and process-supporting infrastructure.
```

**问题**: 当前措辞声称 self-perform plumbing,与 § 一审计指出的 TSBPE 牌问题冲突。

**改成** (无 TSBPE 牌的 fallback 版本,等老板回填 1.1 后再决定):
```
Plumbing scope coordinated as part of integrated MEP delivery — water supply,
drainage, and process-supporting infrastructure. Through licensed plumbing
partners or self-performed under our Texas Plumbing Contractor License.
```

**理由**: 既保留宣传,也保留事实弹性。等老板答 1.1 后这一段就可以收紧到具体说法。

---

### 2.5 Markets — NVIDIA Card 脱敏 (审计 § 4 已记录,这里只列文案改写)

**位置**: index.html line 627-629

**当前**:
```html
<span class="chip">480V · 4000A</span>
<span class="chip">Mission-critical</span>
<span class="chip">AI / HPC</span>
```

**改成**:
```html
<span class="chip">Mission-Critical Switchgear</span>
<span class="chip">AI / HPC Tenant</span>
<span class="chip">Active Build Phase</span>
```

---

### 2.6 Markets — NVIDIA 描述句改 "NVIDIA-tenant"

**位置**: index.html line 623-625

**当前**:
```
Mission-critical electrical for NVIDIA-tenant data center: power distribution,
equipment connections, and inspection-driven coordination across active build phases.
```

**改成** (等老板答 3.3 后定):
```
Self-performed mission-critical electrical for hyperscale AI / HPC build —
switchgear connections, equipment power, and inspection-driven energization
sequencing across active build phases.
```

**理由**: "NVIDIA-tenant" 含义模糊会被 GC 验证识破,改成 "AI / HPC build" 是同样有力但事实合规的表达。

---

### 2.7 "Why Oak Shield" 第 3 卡 — "NVIDIA-backed" 改 "NVIDIA-supporting"

**位置**: index.html line 999

**当前**:
```
From NVIDIA-backed data center electrical to food-grade cold storage.
Complexity is the baseline.
```

**问题**: "NVIDIA-backed" 暗示 NVIDIA 投资 Oak Shield(强信号)。

**改成**:
```
From hyperscale AI data center electrical to food-grade cold storage.
Complexity is the baseline.
```

**理由**: 不必拿 NVIDIA 名字给自己背书,"hyperscale AI" 已经传达项目级别。

---

### 2.8 "Why Oak Shield" 第 4 卡 — "Texas-Based, Statewide" 措辞

**位置**: index.html line 1003-1004

**当前**:
```
Houston, Dallas, Austin, San Antonio. Local crews, local code knowledge,
no travel mark-up surprises.
```

**优化**:
```
Houston · Dallas · Austin · San Antonio + I-10 / I-35 / I-45 build corridors.
Local crews, local code knowledge, no travel mark-ups.
```

**理由**: "build corridors" 是德州行业术语,把现实覆盖范围说清楚,采购官读着舒服。

---

### 2.9 Footer "Bonded · Insured" 太泛

**位置**: index.html line 1180

**当前**:
```html
<span>Bonded · Insured</span>
```

**改成** (基于问卷 1.2 / 2.x 回填):
```html
<span>Bonded · Fully Insured · COIs on prequal</span>
```

或具体:
```html
<span>$10M Single / $30M Aggregate · GL · WC · Auto · $5M Umbrella</span>
```

---

## 三、services.html

### 3.1 ⭐ Electrical Scope — "Medium- & low-voltage distribution"

**位置**: services.html line 337

**问题**: 90% 同体量 sub 不做 MV (>600V)。如果 Oak Shield 0 MV 经验,这一项让数据中心 GC PM 一查就掉链子。

**改成** (等老板答 4.1 决定):

**A. 如果有 MV 经验**:
```html
<li>· Medium-voltage distribution (up to [XX kV]) & low-voltage distribution</li>
```

**B. 如果无 MV 经验**:
```html
<li>· Low-voltage distribution (up to 600V)</li>
<li>· Medium-voltage scope through specialty MV partners</li>
```

---

### 3.2 ⭐ Electrical Scope — "Mission-critical UPS & generator integration"

**位置**: services.html line 338

**改成** (等老板答 4.2 决定):

**A. 有 OEM 授权 (e.g. Eaton)**:
```html
<li>· Mission-critical UPS power feed, install & commissioning (Eaton authorized partner)</li>
<li>· Generator interconnect & ATS coordination</li>
```

**B. 无 OEM 授权 (只做 power feed)**:
```html
<li>· UPS power feed, conduit & raceway infrastructure (commissioning by OEM)</li>
<li>· Generator paralleling & ATS power connections</li>
```

---

### 3.3 Refrigeration Scope — "Energy-recovery integration"

**位置**: services.html line 308

**当前**:
```html
<li>· Energy-recovery integration</li>
```

**问题**: 太泛,具体指 heat reclaim / glycol reclaim / desuperheater?

**改成**:
```html
<li>· Heat reclaim & condenser water recovery</li>
```

或更精确:
```html
<li>· Energy recovery (heat reclaim, condenser water, desuperheater integration)</li>
```

---

### 3.4 ⭐ Plumbing Scope — "Medical / lab gas (where applicable)"

**位置**: services.html line 377

**问题**: 没 ASSE 6010-6030 + 没 TSBPE Medical Gas Endorsement,这一行不能列。"where applicable" 不构成法务免责。

**改成** (等老板答 1.5 决定):

**A. 有 ASSE 持证 plumber**:
```html
<li>· Medical gas systems (ASSE 6010 certified installation, NFPA 99 compliant)</li>
```

**B. 没有 — 必须删除整行**

---

### 3.5 Plumbing Scope — "Pre-fab assemblies for schedule compression"

**位置**: services.html line 380

**改成** (等老板答 4.4):

**A. 有自有 prefab shop**:
```html
<li>· In-house pre-fab assemblies for schedule compression ([XX,XXX sqft] facility)</li>
```

**B. 无自有 shop**:
```html
<li>· Pre-fab assemblies through specialty supplier partners</li>
```

或删除整行(因为外包 prefab 很难当差异化卖点)。

---

### 3.6 Plumbing Scope — "Backflow prevention & water treatment"

**位置**: services.html line 375

**优化**:
```html
<li>· Backflow prevention (BPAT-certified testing) & water treatment</li>
```

**理由**: 提到 BPAT (Backflow Prevention Assembly Tester) 是 TX-specific 资质,采购官秒懂你专业。

---

### 3.7 "Test & balance coordination" — 加 NEBB/AABC 提示

**位置**: services.html line 270

**当前**:
```html
<li>· Test & balance coordination</li>
```

**改成** (等老板答 4.6):

**A. 有 NEBB/AABC 持证人**:
```html
<li>· Test, Adjust & Balance (TAB) — NEBB/AABC certified in-house</li>
```

**B. 仅 coordinate**:
```html
<li>· Test & Balance — coordinated through NEBB/AABC certified TAB agencies</li>
```

---

### 3.8 "Fire alarm & life-safety systems coordination" — 措辞精确化

**位置**: services.html line 343

**改成** (等老板答 1.4):

**A. 有 FAL**:
```html
<li>· Fire alarm install & coordination (TX FAL Class [X])</li>
```

**B. 无 FAL**:
```html
<li>· Fire alarm raceway & infrastructure (FA install by certified FAL contractor)</li>
```

---

### 3.9 ⭐ Integrated MEP "One Safety Program" — EMR 措辞

**位置**: services.html line 408

**当前**:
```
Same site rules, same toolbox talks, same EMR for all four trades.
```

**问题**: "Same EMR" 暗示有 EMR,但全站没数据。

**改成** (等老板答 5.1):

**A. EMR 优秀 (≤ 0.85)**:
```
Same site rules, same toolbox talks, same EMR ([0.XX] · below industry avg.)
across all four trades.
```

**B. EMR 一般 (0.85-1.0)**:
```
Same site rules, same toolbox talks, single EMR for all four trades.
Detailed safety stats provided on prequalification.
```

**C. EMR > 1.0**:
不要主动显示数字,改泛化:
```
Same site rules, same toolbox talks, unified safety program across all
four trades.
```

---

### 3.10 Integrated MEP — 加一卡 "BIM / Coordination Stack"

**位置**: services.html line 405-410 (现 4 卡 grid)

**问题**: 数据中心 / 工业 GC 默认 sub 用 BIM 360。0 提及 = Pre-Qual 大扣分。

**新增第 5 卡** (改成 5 卡 grid 或替换其中 1 卡):
```html
<div class="ink2-bg p-7">
  <div class="text-3xl safety mb-3">→</div>
  <h3 class="text-lg font-extrabold mb-2">BIM-Coordinated</h3>
  <p class="text-sm text-white/65 leading-relaxed">
    Bluebeam / BIM 360 / Procore native — clash detection at coordination,
    not at installation.
  </p>
</div>
```

(等老板答 8.6 后填具体工具名)

---

## 四、company.html

### 4.1 ⭐ Compliance & Coverage 4 卡升级 (审计 § 二全部映射)

详见 `03_mockup_revisions_brief.md` v2 的修订 1.1-1.6,**全部应用在 company.html line 302-307**:

- 卡 1 TACL & TECL → 加级别 (TACL-A · TECL-Master)
- 卡 2 GL · WC · Auto → 改 4 险种或加 Umbrella
- 卡 3 Bonding "Surety-backed" → 改具体数字或 "Bondable"
- 卡 4 Prequalification "capable" → 改 Active / Enrolled / Onboarding 状态
- **新增卡 5** Safety Performance / EMR

---

### 4.2 Story 第 3 段 — "We don't fly mark-ups in" 措辞

**位置**: company.html line 263-265

**当前**:
```
We're Texas-based and Texas-licensed. We work where our crews can drive
home — Houston, Dallas, Austin, San Antonio, and the build corridors
connecting them. We don't fly mark-ups in.
```

**优化**: 这段写得已经很好,但 "We don't fly mark-ups in" 可以再精确化:

```
We're Texas-based and Texas-licensed. We work where our crews can drive
home — Houston, Dallas, Austin, San Antonio, and the I-10 / I-35 / I-45
build corridors connecting them. No travel mark-ups, no per-diem hidden
in the bid sheet.
```

---

### 4.3 Quick Facts 表格 — 加关键数据行

**位置**: company.html line 271-277

**当前 5 行**: Headquarters / Service Area / Self-Performed Trades / Client Mix / Verticals

**新增 3 行** (基于问卷 6.4 回填):
```
+ <dt>Founded</dt><dd>[Year]</dd>
+ <dt>Team Size</dt><dd>[X] employees · [Y] field crew</dd>
+ <dt>Annual Volume</dt><dd>[Range]</dd>
```

---

### 4.4 ⭐ 加 Leadership Section (新建,放 Story 后 Compliance 前)

**位置**: company.html — 在 line 281 (Story end) 与 line 283 (Compliance begin) 之间

**新建** (等老板答 6.2 / 6.3):
```html
<section class="paper2-bg py-20">
  <div class="max-w-7xl mx-auto px-6">
    <div class="text-xs uppercase tracking-[0.2em] safety font-bold mb-4">// Leadership</div>
    <h2 class="display text-3xl lg:text-4xl font-extrabold leading-tight mb-12">
      Who runs Oak Shield.
    </h2>
    <div class="grid md:grid-cols-3 gap-8">
      <!-- Founder card -->
      <div>
        <div class="aspect-[4/5] bg-ink mb-4"><!-- headshot placeholder --></div>
        <div class="text-lg font-extrabold">[Founder Name]</div>
        <div class="text-xs uppercase tracking-wider safety font-bold mb-2">Founder & President</div>
        <p class="text-sm text-ink/65 leading-relaxed">[Bio paragraph]</p>
      </div>
      <!-- Operations -->
      <!-- Safety Director -->
    </div>
  </div>
</section>
```

**理由**: 当前网站没有 leadership 是 Pre-Qual 致命缺陷。Pre-Qual 表格必填 "Project Manager / Safety Director / Estimating Manager 各自姓名"。

---

### 4.5 Compliance 区块下方文字 — EMR 措辞优化

**位置**: company.html line 308

**当前**:
```
Specific license numbers, insurance limits, bonding capacity, EMR, and
safety program documents provided as part of prequalification submission.
Request via the Capability Statement.
```

**优化**: 这段写得 OK,但可以更主动:
```
Full prequalification package — license numbers, COI, EMR detail,
bonding capacity, safety program, and project references — available
via the Capability Statement (instant) or Prequalification Package
(within 1 business day).
```

---

## 五、contact.html

### 5.1 ⭐ "Specific street address provided on request" 必须改

**位置**: contact.html line 421

**当前**:
```
Headquartered in Houston, TX
Specific street address & mailing details provided on request as part
of prequalification.
```

**问题**: B2B 采购官读到 = "shell company red flag"。

**改成** (等老板答 6.1):
```
Headquartered in Houston, TX
[Real Street Address, Houston TX XXXXX]
By appointment · Field offices in [Dallas / Austin / SA if applicable]
```

或如老板暂不公开实际地址(如住宅):
```
Headquartered in Houston, TX
[Commercial Mail Forwarding Address]
Site visits by appointment via [Email] or 713-815-0552
```

---

### 5.2 RFP Form — 字段优化

**位置**: contact.html line 274-365

**当前字段**: Name / Company / Role / Email / Phone / Project Location / Project Type / Scope / Description / Documents / Confirm

**新增建议字段** (Pre-Qual 早期筛选用):
```html
+ <select name="project_timeline">
+   <option>Project Timeline...</option>
+   <option>Active RFP (now)</option>
+   <option>RFP within 3 months</option>
+   <option>RFP within 6-12 months</option>
+   <option>Exploring partners</option>
+ </select>
+ <select name="contract_value_range">
+   <option>Estimated Sub Contract Value...</option>
+   <option>Under $250K</option>
+   <option>$250K - $1M</option>
+   <option>$1M - $5M</option>
+   <option>$5M - $10M</option>
+   <option>Over $10M</option>
+ </select>
+ <input name="gc_name" placeholder="GC name (if known)">
```

**理由**: Pre-Qual 早期筛选的 lead score 主要来自 "RFP timeline + contract value + GC name"。当前表单太通用。

---

### 5.3 Capability Statement Section — 改成真 Lead Capture

**位置**: contact.html line 371-407

详见 `03_mockup_revisions_brief.md` v2 修订 1.6 — 当前两个按钮都跳同一页,改成轻 Lead (PDF download) + 重 Lead (Pre-Qual request)。

---

### 5.4 Office Hours Strip — Crew Coverage 文字精确化

**位置**: contact.html line 423-427

**当前**:
```
Crew Coverage: Texas Statewide
Houston · Dallas · Austin · San Antonio & build corridors between.
No travel mark-up surprises.
```

**改成**:
```
Crew Coverage: 4 Major Markets + Build Corridors
Houston (HQ) · Dallas/Fort Worth · Austin · San Antonio +
I-10, I-35, I-45 corridors. For projects outside these markets, ask
us about partnered execution.
```

---

## 六、markets/*.html (5 个市场页)

### 6.1 ⭐ 全 5 页 — "Texas Statewide" chip 改

**位置**: 5 个 markets/*.html line ~244 hero chip

**当前**:
```html
<span class="chip border border-white/20 text-white/70">Texas Statewide</span>
```

**改成**:
```html
<span class="chip border border-white/20 text-white/70">Houston · DFW · Austin · SA</span>
```

---

### 6.2 data-centers.html — Hyperscale 措辞校准

**位置**: data-centers.html line 246, 258

**当前**:
```
Texas is the new center of gravity for AI / HPC build-outs — from Stargate
Abilene to Meta and Google expansions across DFW. Oak Shield delivers
self-performed mission-critical electrical and mechanical scope for
hyperscale, colo, and edge data center facilities.
```

**问题**: "hyperscale" 严格定义 ≥100MW 单租户 (Uptime Institute / 451 Research)。如 NVIDIA Dallas 项目 <100MW,这个标签滥用。

**改成** (等老板答 3.3 项目 IT 负载量级):

**A. 项目确实 ≥100MW**:
```
保留 "hyperscale" 措辞
```

**B. 项目 <100MW (大概率)**:
```
... electrical and mechanical scope for AI / HPC, enterprise,
colo, and edge data center facilities.
```

(去掉 "hyperscale",改成 "AI / HPC, enterprise" — 同样有力但合规)

---

### 6.3 data-centers.html — Project Reference "Phase 02" 措辞

**位置**: data-centers.html line 277

**当前**:
```
<div class="text-sm text-white/55 mb-1 font-mono">Dallas Area, TX · Phase 02</div>
```

**问题**: "Phase 02" 是 informal。如果是 "项目分多个 phase" 还是 "整个建设的第 2 期" 含义不同。

**改成** (等老板补充):
```
<div class="text-sm text-white/55 mb-1 font-mono">Dallas Area, TX · [Year] · [Phase / Building X of program]</div>
```

---

### 6.4 cold-storage.html FAQ — Ammonia 措辞 (审计 § 5.6)

**位置**: cold-storage.html FAQ 第 2 个问题

**改成** (基于问卷 4.5 回填):

**A. 有 IIAR + PSM in-house**:
```html
We deliver freon / HFC / HFO refrigeration in-house and have
[X] PSM-trained refrigeration technicians for anhydrous ammonia (NH3)
systems. We are an active IIAR member and design / install to IIAR-2/4/5/6
standards with full RAGAGEP and EPA RMP compliance.
```

**B. 无 IIAR / PSM (大概率)**:
```html
We deliver freon / HFC / HFO refrigeration in-house. Anhydrous ammonia
(NH3) systems are delivered through our specialty IIAR-certified partner —
Oak Shield acts as MEP coordinator and integration sub.
```

---

### 6.5 hospitality.html FAQ — 第 3 个问题措辞

**位置**: hospitality.html FAQ 第 3 个问题

**当前**:
```
Full-service, select-service, extended-stay, boutique / lifestyle, resort /
convention and hotel renovation / re-flag. Our Blossom Hotel build was
full-service development; we scale crews to project format.
```

**问题**: 列了 6 种酒店类型,但只有 1 个真实参考 (Blossom)。读着像 "what we hope to do" 不是 "what we've done"。

**改成**:
```
Full-service hotels (our Blossom Hotel template), select-service,
extended-stay, and renovation / re-flag. Other formats — boutique,
resort, convention — through our hospitality experience and partner
network. Scope to your project format.
```

**理由**: 把 "已做过" 和 "可做" 分开,符合 GC 看待 "track record" 的方式。

---

### 6.6 industrial.html FAQ — Vertical 列表过长

**位置**: industrial.html FAQ 第 3 个问题

**当前**: 列了 10 个 vertical (Food&beverage / Battery&EV / Aerospace / Oil&gas downstream / Chemical / Plastics / Pharma / Semiconductor / Automotive / Industrial laundry)

**问题**: 没真做过的 vertical 列出来 = "我们什么都做" = "我们什么都不专业"。

**改成** (诚实分层):
```
Demonstrated capabilities: Food & beverage processing, industrial
cold storage. Approached through our 4-trade self-perform model:
Battery / EV facilities, manufacturing retrofit, plastics,
pharma support facilities. Tell us your vertical and we'll map
fit honestly — including referring you elsewhere if it's outside
our core capability.
```

**理由**: B2B sub 在工业领域的差异化不是 "我什么都做" 而是 "我说真话,不到的我帮你找别人"。

---

## 七、跨页 — Capability Statement 内容设计

### 7.1 ⭐ 4 页 PDF 标准结构 (上线时附 PDF)

**问卷 1.6 项**: 老板需要准备 PDF。结构建议:

```
Page 1 — Cover
  · Logo · Company name · Tagline ("Self-Performing MEP for Texas...")
  · Founded / HQ / Phone / Email
  · UEI # (SAM.gov), DUNS # (legacy), TX HUB # (if applicable)

Page 2 — Self-Performed Trades + Markets
  · 4 trades 简述 (HVAC / Refrig / Elec / Plumbing)
  · 5 markets 简述 (DC / Hospitality / Cold Storage / Big-Box / Industrial)
  · Self-Performed Scope by trade

Page 3 — Representative Projects (4 个 signature 项目卡片)
  · 每个项目: Owner / Location / Scope / Year / Sub Contract Value Range
  · GC reference (姓名 + 联系方式) — 仅限授权后

Page 4 — Compliance & Capability
  · Texas License Numbers (TACL-A # / TECL # / TSBPE # if applicable)
  · Insurance: GL / WC / Auto / Umbrella / CPL / E&O 实际限额
  · Bonding: Single / Aggregate
  · Pre-Qual Platform Status: ISN / Avetta / Veriforce
  · Safety: EMR / TRIR / DART / OSHA-10/30 coverage
  · Memberships: ABC / AGC / IIAR / NEBB / etc.
  · NAICS Codes: 23822 (Plumbing/HVAC), 238210 (Electrical), etc.
```

---

## 八、SEO / Meta — 6 项细优化

### 8.1 Meta Description (各页)

**index.html line 7** 当前:
```
Texas-based commercial & industrial MEP contractor delivering HVAC,
refrigeration, electrical and plumbing for data centers, hospitality,
cold storage and big-box retail. Trusted by GCs across Houston and Dallas.
```

**优化**: 当前 OK,但加关键词密度:
```
Self-performing commercial MEP subcontractor in Texas — HVAC,
refrigeration, electrical & plumbing for data centers, hospitality,
cold storage & big-box retail. Houston · Dallas · Austin · San Antonio.
TACL-A & TECL licensed. ISN / Avetta prequalified.
```

(等老板答 5.8 后填 prequalified 状态)

---

### 8.2 Title Tag 各页一致性

| 页 | 当前 Title | 优化建议 |
|---|---|---|
| index | `Oak Shield Service – Commercial & Industrial MEP Contractor in Texas` | 加关键词 → `Oak Shield Service – Self-Performing MEP Subcontractor for Texas Commercial & Industrial Projects` |
| services | `Commercial & Industrial MEP Services in Texas \| Oak Shield Service` | OK,可加 "Self-Performed" → `Self-Performed MEP Services in Texas...` |
| markets/data-centers | `[当前]` | 改 → `Data Center Electrical & MEP Subcontractor in Texas \| Dallas, Houston Hyperscale` |

---

### 8.3 OG Image 配置 (各页)

**当前**: index.html 缺 `og:image`,markets/* 也都缺。

**优化**: 各页加 LinkedIn / Twitter 友好的 og:image:
```html
<meta property="og:image" content="https://oakshieldservice.com/assets/og_default.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```

---

### 8.4 Canonical URL 各页

services.html 有 (line 8: `<link rel="canonical">`),其他 4 页缺。需要补全。

---

### 8.5 Breadcrumb Schema

5 个 markets 页都加 BreadcrumbList JSON-LD:
```json
{ "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type":"ListItem","position":1,"name":"Home","item":"https://oakshieldservice.com/"},
    {"@type":"ListItem","position":2,"name":"Markets","item":"https://oakshieldservice.com/markets/"},
    {"@type":"ListItem","position":3,"name":"Data Centers","item":"https://oakshieldservice.com/markets/data-centers.html"}
  ]
}
```

---

### 8.6 Sitemap.xml + robots.txt

上线前必须有:
- `https://oakshieldservice.com/sitemap.xml` (列出 12 个页面: 1 home + 1 services + 1 company + 1 contact + 5 markets + 4 project detail 如果做)
- `https://oakshieldservice.com/robots.txt` (Allow: / + Sitemap: 引用)

---

## 九、跨页面 — 一句话 Tagline 提炼

当前每页都在重复 "self-perform 4 trades, single accountability, inspection-driven" — 应该提炼成一句官方 tagline,各页一致使用。

**候选 3 个**:

**A. 短**:
```
Self-performing MEP for Texas builds.
```

**B. 中** (推荐):
```
Self-performing HVAC, refrigeration, electrical & plumbing — under one
estimating desk, one project manager, one warranty contact.
```

**C. 长 (Hero 用)**:
```
The Texas MEP subcontractor GCs hire when seam-failure between trades
isn't an option.
```

**老板选定 1 个之后,全站统一应用**。

---

## 十、上线前检查清单 (开发执行)

### 内容
- [ ] 全文搜 `TBD` → 0 结果
- [ ] 全文搜 `[pending]` → 0 结果
- [ ] 全文搜 `Lorem` / `placeholder` 文本 → 0 结果
- [ ] 全文搜 `480V · 4000A` → 0 结果 (NVIDIA chip 已脱敏)
- [ ] 全文搜数字 + V/A/MW/kW/ton/°F → 仅保留必要的定性表达
- [ ] 全文搜 NVIDIA logo 文字 → 已按问卷 3.1 决定的方案处理

### 技术
- [ ] 所有 5 页 JSON-LD 移到 `</body>` 之前
- [ ] 5 页 JSON-LD `@type` 改 LocalBusiness 系
- [ ] 5 页 LocalBusiness 字段补完 (address / hours / sameAs)
- [ ] 5 页有 canonical URL
- [ ] 5 页有 og:image
- [ ] 5 markets 页有 BreadcrumbList
- [ ] sitemap.xml + robots.txt 部署
- [ ] Google Search Console 提交 sitemap
- [ ] Google Business Profile 创建 (Houston) + 加 photo + 加 Q&A

### 法务
- [ ] NVIDIA / Costco / Blossom / OCM logo 处理方式按问卷 3.1 / 3.2 执行
- [ ] Capability Statement Public PDF 准备完毕
- [ ] Privacy Policy 页面 (CCPA / TX TRPDA 合规)
- [ ] Terms of Service 页面

### 监管
- [ ] TACL / TECL 实际号码已填入
- [ ] TSBPE Plumbing License 状态已确认 + 文案对应调整
- [ ] EPA 608 数据已确认
- [ ] FAL 状态已确认
- [ ] Medical Gas 行去留已决定

### Pre-Qual
- [ ] 4 个 signature project 完整数据 (date / value / GC reference) 已收集
- [ ] EMR / TRIR / DART / OSHA 数据已收集 (内部 PDF 用)
- [ ] Insurance COI 已扫描
- [ ] ISN / Avetta / Veriforce 注册启动

---

## 一句话总结(老板必读)

> 这份清单 32 项里,**16 项可以现在就改**(纯措辞问题,不需要老板提供新数据);**16 项要等老板回填问卷**(Word 文档里的 32 个 ✦ 字段)。
>
> 现在就改的 16 项做完,网站可以从"60 分内容"升到"75 分"。等老板回填后再改剩下 16 项,可以升到"90 分能上线投真 RFP"的状态。
>
> 我建议: ① 老板先填 P0 问卷里的 16 项 (法务 + 监管 + 真实地址 + 真实 founder),网站可以先上线;② 在前 30 天 Pre-Qual 准备阶段补 P1 14 项;③ 后续 90 天补 P2 9 项。

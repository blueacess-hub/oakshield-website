# Oak Shield 网站全站 — 资深 MEP 行业审计

**审计日期**: 2026-05-04
**审计范围**: 5 个核心页 (index / services / company / contact + 5 个 markets/*.html)
**视角**: 资深 MEP 行业人员 (B2B 采购官 + GC PM + MEP 工程师 + 承包商保险代理 + OSHA 安全官 + Texas 监管熟悉者)
**输出层级**: 7 大类 / 65 项发现 / 32 项老板必须回填的数据

---

## 一句话结论

> **网站把"我能做什么"说得很会卖,但把"我有没有资格做"说得不够,**而 B2B MEP 分包合同里第二件事比第一件事重要 10 倍。
>
> 当前最大风险有 3 个:
>
> 1. 🔴 **TX 法定资质链条不完整** — 自称自营 Plumbing 但全站零 TSBPE Master Plumber 信息(无照在 TX 干 plumbing = 触法)
> 2. 🔴 **NVIDIA / Costco logo 颜色还原度太高** — 商标侵权法务硬伤,采购官律师扫一眼就知道
> 3. 🔴 **Schema.org 标 GeneralContractor** — 你不是 GC,你是 MEP Sub,Google 会按 GC 推 SEO,RFP 找不到你
>
> 中风险还有 12 项,详见 § 二 - § 八。

---

## 二、Texas 法定资质 — 5 项硬伤

> Texas MEP 业务在 4 个不同监管体系下持牌,site 必须证明全链合规。当前缺 3 个、错 2 个。

### 2.1 🔴 缺 TSBPE Plumbing License(法律层面无法做 plumbing)

**事实**:
- TX 任何商业 plumbing 必须由 **TSBPE 颁发的 Plumbing Company License (M-XXXXX)** + 至少一名 **Master Plumber (M-XXXXX 个人)** 负责。
- 全站(index / services / company / contact / 5 个 markets)**100% 不提任何 plumbing license**。
- 但同时声称 "self-perform plumbing" 在每一页(services.html line 372-381 / index.html service card / 5 个 market FAQ)。

**采购官读到的信号**: "他没有 plumbing 牌但说自己干 plumbing → 要么撒谎要么转包,转包就不该说 self-perform。"

**老板必须答**:
- ✦ 2.1-A: Oak Shield 是否持有 TSBPE Plumbing Company License?号码?
- ✦ 2.1-B: 在职 Master Plumber 姓名 + M-XXXXX 个人号?
- ✦ 2.1-C: 如果都没有,plumbing scope 是不是其实通过分包合作伙伴?如是,**全站不能再说 "self-perform plumbing"**,要改 "plumbing through licensed partner subcontractor"。

---

### 2.2 🔴 错 "Electrical Master" 措辞 — TX TDLR 没有这个术语

**位置**: company.html line 303

**当前**: `TACL & TECL · HVAC + Electrical Master · numbers on prequal`

**错在**:
- TX TDLR 颁的是 **TECL (Texas Electrical Contractor License — 公司牌)**,需要在职 **Master Electrician** 担任 Designated Master。
- "Electrical Master" 在 TX 监管文档里**不存在**,标准说法是 "Master Electrician" (个人)或 "TECL Master license" (公司)。
- 业内人一看就觉得 "这家公司没真懂 TX 监管"。

**改成**: `TACL-A · TECL` 或 `TACL · TECL · Master Electrician on staff`

**老板必须答**:
- ✦ 2.2-A: TACL 是 Class A 还是 Class B?(A 无限容量 / B ≤25 ton)
- ✦ 2.2-B: Designated Master Electrician 姓名(可不公开但 Pre-Qual 要)
- ✦ 2.2-C: 实际 TACL # / TECL # (上线前必须填,footer 不能再 [pending])

---

### 2.3 🔴 缺 EPA Section 608 Universal Certification(refrigerant 强制)

**事实**:
- 任何 refrigerant 处理(回收/充注/服务)都要 EPA Clean Air Act Section 608 持证技工。
- 全站 0 提及 EPA 608。
- Refrigeration Service Partner / OCM Mushroom 项目都涉及 refrigerant,无 608 是违反 EPA 的。

**老板必须答**:
- ✦ 2.3: Refrigeration techs 是否都有 EPA 608 Universal?统计在职持证人数。

---

### 2.4 🟡 缺 / 不明 TX Fire Alarm License (FAL)

**位置**: services.html line 343 `Fire alarm & life-safety systems coordination`

**说明**:
- TX TDI (Texas Department of Insurance) 颁 **FAL (Fire Alarm License)**,无照不能 install/service fire alarm。
- "Coordination" 这个词避开了 install,**法律上 OK**。
- 但如果 Oak Shield 实际只做 raceway/conduit 给 FA 系统(不做 device install),应该明确改成 **"raceway & infrastructure for fire alarm (third-party FAL contractor)"** —— 这是 TX 标准做法,采购官一看就懂。
- 如果 Oak Shield **持有 FAL** 应该当卖点,不要藏。

**老板必须答**:
- ✦ 2.4: Oak Shield 是否持 FAL?如有,全文加上;如无,把 services.html 该行改成 "raceway & infrastructure" 措辞。

---

### 2.5 🔴 危险 — Medical Gas 声称 + 0 凭证

**位置**: services.html line 377 `Medical / lab gas (where applicable)`

**事实**:
- 医用气体(O2/N2O/Vacuum/Med Air)安装在 TX 必须:
  - **TSBPE Medical Gas Installer Endorsement** (Master Plumber 之上的额外背书)
  - **ASSE 6010** (Brazer) + **ASSE 6020** (Inspector) + **ASSE 6030** (Verifier) 系列证书
  - **NFPA 99** 合规知识
- "where applicable" 是免责,但风险点在于一个看似 "顺手的" 列举,会引来不实期待。
- 如果 Oak Shield 0 个 ASSE 6010/6020/6030 持证人 → 这一行**必须删除**,这是 medical gas 系统设计/施工的硬底线。

**老板必须答**:
- ✦ 2.5: Oak Shield 是否有任何 ASSE 6010-6030 持证 plumber?如无,services.html line 377 必须删掉。

---

## 三、保险与风险管理 — 5 项严重缺失

> 当前 company.html line 304 显示 `GL · WC · Auto`。这是**最小三件套**,任何严肃 B2B project 都不够。

### 3.1 🔴 缺 Umbrella / Excess Liability(数据中心 / 工业 / 政府硬卡门槛)

- 当前: 0 提及
- 行业最低: **$5M Aggregate**;数据中心 / Stargate 类型项目: **$10M-$25M**
- Pre-Qual 平台 (ISN / Avetta / Veriforce) 入门要求: $5M Umbrella
- 如果 Oak Shield 没有 Umbrella → **绝大多数 hyperscale / 工业 RFP 直接刷掉**,不会进 Pre-Qual。

**老板必须答**: ✦ 3.1: 当前 Umbrella 限额(或 "0 = 没有")。

---

### 3.2 🔴 缺 Pollution Liability — Refrigerant 处理强制项

- CGL 标准条款里有 **Pollution Exclusion**,refrigerant 泄漏 / 回收事故索赔不在 CGL 范围内。
- Refrigeration scope (你已经在 OCM Mushroom 干了)如果出现 R-410A/R-404A/HFO 大量泄漏导致客户停产,索赔无险可保。
- 行业标准: $1M-$5M Pollution Liability (Contractors Pollution Liability "CPL")。
- 同时如果做 ammonia (NH3) 系统,Pollution + 责任 + RMP (EPA Risk Management Plan) 都是硬要求。

**老板必须答**: ✦ 3.2: 是否持 Contractors Pollution Liability?限额?

---

### 3.3 🟠 缺 Professional Liability / E&O(design-assist 项目硬要求)

- Design-assist / design-build MEP scope 越来越多,GC 转风险给 sub。
- 行业标准: $1M-$2M E&O。
- 如果 Oak Shield 接 design-assist (例如帮 GC 优化 ducting / 重新选型 equipment),没 E&O 等于裸奔。

**老板必须答**: ✦ 3.3: 是否持 Professional Liability / E&O?

---

### 3.4 🟠 缺 Inland Marine Coverage

- 工具 / 临时设备在转运中(项目间运输)的盗损保险。
- 大件设备 (chiller / 变压器 / 大型 panel) 上保险必备。
- 行业标准: $250K-$1M Tool & Equipment Floater + In-Transit Coverage。

**老板必须答**: ✦ 3.4: 是否持 Inland Marine?限额?

---

### 3.5 🟡 缺 Builder's Risk 能力

- 通常 GC 提供 Builder's Risk,但 sub 应表明能 "join named insured" 或单独购买。
- 这是 Pre-Qual 表格里一个 sub-question。

**老板必须答**: ✦ 3.5: 是否能 join GC 的 Builder's Risk policy?

---

## 四、商标 / 法律风险 — 3 项必须立刻处理

### 4.1 🔴 NVIDIA "logo" 用了官方品牌色 #76B900 + 大写无衬线 wordmark

**位置**: index.html line 297, 452

**事实**:
- NVIDIA 官方品牌色 = `#76B900` (NVIDIA Green) — 商标受保护元素之一
- 当前 mockup `<span class="lg-nvidia">NVIDIA</span>` 用 Manrope 800 字重 + 0.05em 字距 + #76B900 — **是 NVIDIA wordmark trade dress 的高度近似复刻**
- HTML 注释 `placeholder, NOT actual NVIDIA logo` **不构成法律免责** (商标法看实际呈现,不看注释)
- NVIDIA brand guidelines 明确规定: "Do not use the NVIDIA logo or wordmark without prior written approval."
- 类似情况: 2018 年 Hummel 律师函给一家健身 startup 用了 "official orange" 颜色,胜诉。

**风险**: 收到 NVIDIA 律师函(品牌部门有专门 brand monitoring tools),可能强制下线。

**改成**: 改用脱敏文字标志(参见 brief 03 修订 3.1 三选一方案)。

**老板必须答**: ✦ 4.1: 是否拿到 NVIDIA 客户的 logo 使用书面授权?如未拿到,必须改。

---

### 4.2 🔴 Costco 同样问题 #E31837 红 + #005DAA 蓝 = 官方品牌色

**位置**: index.html line 299-300

**事实**: Costco 官方品牌色 = #E31837 (PMS 1797 C) 红 + #005DAA (PMS 286 C) 蓝。当前 mockup 1:1 还原。Costco brand guidelines 也明确禁止未授权使用。

**老板必须答**: ✦ 4.2: 是否拿到 Costco 客户的 logo 使用书面授权?

---

### 4.3 🟠 NVIDIA "tenant" 措辞模糊

**位置**: 多页出现,index.html line 624, data-centers.html line 246, etc.

**说明**: "NVIDIA-tenant data center" / "NVIDIA-supporting" / "NVIDIA-backed" 三个词在不同页面出现,**含义完全不同**:

| 措辞 | 含义 |
|------|------|
| **NVIDIA-tenant** | NVIDIA 是 tenant — NVIDIA 在租这个建筑或这个建筑里跑 NVIDIA 工作负载 |
| **NVIDIA-supporting** | NVIDIA 不是业主也不是 tenant,只是建筑里有 NVIDIA 硬件(95% 的"NVIDIA 数据中心")|
| **NVIDIA-backed** | NVIDIA 投资了这家公司或这个项目(语义最强) |

**业内现状**: Stargate (Abilene)、Microsoft / Meta / Google 的 AI 集群都是 *用了 NVIDIA H100/B200 硬件的数据中心*,但建筑业主和运营方都不是 NVIDIA 自己。Equinix / Oracle Cloud / CoreWeave / Lambda 才是真正的 colo + 物业运营方。

**采购官 Fact-Check**: 一个 GC PM 看到 "NVIDIA Data Center · Dallas" 会去 Google / LinkedIn / 471 Research 数据库查 — 找不到 NVIDIA 自有 Dallas DC,会怀疑你夸大事实。

**改成**: 明确写出真实业主 / GC,例如 "Hyperscale AI Tenant Build · Dallas · GC: [GC name]" 或 "AI / HPC Hyperscale Build supporting NVIDIA-class workloads"。

**老板必须答**:
- ✦ 4.3-A: Dallas 项目真实业主 / 运营方是谁?(NVIDIA / Oracle / CoreWeave / Equinix / 其他)
- ✦ 4.3-B: 真实 GC 名字是?
- ✦ 4.3-C: Oak Shield 实际持有的合同方 (PO 抬头) 是谁? (GC / EPC / NVIDIA 直签都不一样)

---

## 五、技术能力声明 — 6 项可能夸大

> 这一节是最敏感的:每条都不是"撒谎"是"边界模糊",采购官打电话验证时会暴露。

### 5.1 🟠 "Medium- & low-voltage distribution" — 容易被发现没真做过 MV

**位置**: services.html line 337

**事实**:
- TX 监管: MV (>600V to 35kV) 不需要单独 license,但需要专业培训 + IBEW NJATC 类高压课时 + 厂家 OEM 授权。
- 现实: 90% 的 TX MEP sub (含 $10M 级别) 不做 MV,会让给 Quanta / Faith Industries / Henkels & McCoy 等 MV 专项 EC。
- 数据中心场景: 业主 → utility → primary switchgear (MV) → 步降变压器 → LV 段开始才是 MEP sub 范围。Oak Shield 在 NVIDIA 项目作为 "Electrical Subcontractor",绝大概率是 LV-only。

**采购官风险**: 一个 hyperscale GC PM 会问 "你们最大做过的 MV 项目是 38kV 还是 15kV?" 你答不上来,后续机会归零。

**老板必须答**:
- ✦ 5.1-A: Oak Shield 实际是不是有 MV (>600V) 经验?最高电压级别?
- ✦ 5.1-B: 如果 0 MV 经验,services.html 该行删掉 "Medium-",只保留 "Low-voltage distribution"。

---

### 5.2 🟠 "Mission-critical UPS & generator integration" — UPS 通常 OEM 才做

**位置**: services.html line 338

**事实**:
- Hyperscale UPS (Eaton 9395 / Vertiv NXL / Schneider GVS) 安装通常需要 **OEM 厂家授权 service partner**。
- 没有 OEM 授权,不能给 UPS 上电 / commissioning。
- "Integration" 是个软词,可以是 conduit + power feed 到 UPS — OK,但 install 是另一回事。

**老板必须答**:
- ✦ 5.2-A: Oak Shield 是哪些 UPS 厂家的 authorized partner? (Eaton / Vertiv / Schneider / ABB)
- ✦ 5.2-B: 实际做的是 install + power feed 到 UPS,还是 commissioning UPS unit 本身?

---

### 5.3 🟠 "Switchgear & PDU installation" — Switchgear factory-tested 居多

**位置**: services.html line 339

**说明**: Hyperscale switchgear 和 PDU 现在大多是 **Power Module** (整体厂房成套交付),sub 做的是 set + connect,不做"installation" 含义里的内部装配。措辞 OK,但能力级别要清楚。

**老板必须答**: ✦ 5.3: 实际经验是 Power Module set + tie-in,还是 traditional stick-built switchgear 现场组装?(差异巨大)

---

### 5.4 🔴 "Pre-fab assemblies for schedule compression" — 自有 prefab shop?

**位置**: services.html line 380

**事实**:
- 真正的 prefab 需要 ~5,000 sqft 厂房 + ~$2M 设备 (rolling table / 焊接机 / overhead crane / CNC 切割) + 至少 5 个全职 fabricator。
- TX 大型 MEP (TDIndustries / Comfort Systems / Letsos) 都有 prefab,因为体量够。
- $500K-$5M 段的 sub 几乎没人有自有 prefab,都是外包给 PEMB 或 Modular 厂家。
- 业内人一看 "we pre-fab assemblies" 就会问 "你的 fab shop 在哪?多大?有多少在职 fabricator?"

**老板必须答**: ✦ 5.4: Oak Shield 是否有自有 prefab shop?如无,这一句必须改成 "we partner with prefab suppliers" 或删除。

---

### 5.5 🟠 "Test & balance coordination" — 不要写 perform,只写 coordinate

**位置**: services.html line 270

**事实**:
- TAB (Test, Adjust, Balance) 通常需要 **NEBB 或 AABC 认证** 的 specialist。
- Oak Shield 当前措辞 "T&B coordination" 是干净的(只 coordinate,不 perform),OK。
- 如果客户问 "你们能不能直接出 NEBB 认证报告?" 你诚实回答 "我们 coordinate 第三方 TAB agency,不直接出报告" 是 best practice。

**老板必须答**: ✦ 5.5: Oak Shield 是否有 NEBB / AABC 认证 TAB technician?(如有可作为差异化卖点)

---

### 5.6 🔴 Ammonia / NH3 refrigeration FAQ 措辞危险

**位置**: cold-storage.html FAQ 第二个问题

**当前**: `For ammonia (anhydrous) systems we carry the qualifications and partner with specialized refrigerant licensing where required.`

**问题**:
- "We carry the qualifications" 暗示 in-house 能力。
- Anhydrous NH3 系统监管极重: PSM (OSHA 1910.119) + RAGAGEP + IIAR Standards (IIAR-2/4/5/6) + EPA RMP (>10K lbs)。
- 一个出事故的 ammonia release 能搞死整家公司(Tyson Foods 2017 事故 = $2.3M OSHA fine + 1 死)。
- "partner with specialized refrigerant licensing" 是含糊的,真实情况要么是: ① PSM 持证 in-house refrig tech ② 整套外包给 IIAR member 公司。

**老板必须答**:
- ✦ 5.6-A: Oak Shield 是否有 IIAR member status?有 PSM-trained refrig tech?
- ✦ 5.6-B: 如果都没有,FAQ 改成 "We deliver freon / HFC / HFO refrigeration in-house. Anhydrous ammonia systems are delivered through our specialty IIAR-certified partner — Oak Shield acts as MEP coordinator."

---

## 六、B2B Pre-Qual 标准缺失 — 8 项必须补

> 这一节是 ISN / Avetta / Veriforce 表格上**会问**而你**没答**的字段。

| # | 项目 | 现状 | 老板必须提供 |
|---|------|------|------|
| 6.1 | **EMR (Experience Modification Rate)** 当前数字 | 0 | ✦ 6.1: 当前 EMR 数字 + 最近 5 年趋势 |
| 6.2 | **TRIR (Total Recordable Incident Rate)** | 0 | ✦ 6.2: 最近 3 年 TRIR + 行业 BLS NAICS 23822 平均对比 |
| 6.3 | **DART Rate (Days Away/Restricted/Transferred)** | 0 | ✦ 6.3: 最近 3 年 DART |
| 6.4 | **Lost Time Incident Rate** | 0 | ✦ 6.4: 最近 3 年 LTIR |
| 6.5 | **OSHA-10 / OSHA-30 覆盖率** | 0 | ✦ 6.5: 现场工人 OSHA-10 % / 管理层 OSHA-30 % |
| 6.6 | **Drug-Free Workplace Program** | 0 | ✦ 6.6: 是否有 written DFW 政策?Pre-employment + random + post-incident testing? |
| 6.7 | **Background Check Policy** | 0 | ✦ 6.7: 现场进入前 background check?7-year criminal?MVR? |
| 6.8 | **ISN / Avetta / Veriforce Active 状态** | 标 "capable" | ✦ 6.8: 各平台 Active / Pending / Not yet 状态 + 各自 Grade (A/B/C) |

---

## 七、Schema / SEO / 技术错误 — 4 项

### 7.1 🔴 JSON-LD `@type: GeneralContractor` 是错的

**位置**: services.html line 503-533, company.html line 413-444, 5 个 markets/*.html

**问题**:
- `GeneralContractor` (Schema.org/GeneralContractor) 是 Schema.org 定义的 **总包商**,负责整个项目交付。
- Oak Shield 是 **MEP Subcontractor**,负责 4 个 trade scope 中的工种交付。
- Google 看 schema 决定 SERP 分类。当前等于告诉 Google "我是 GC",会被 GC 类目 SEO 算法对待 — 这是错的市场。
- 真正想被找到的客户是 GC PM / Owner / MEP Engineer 找 "MEP subcontractor in Texas"。

**改成**(多类型组合):

```json
{
  "@context": "https://schema.org",
  "@type": ["LocalBusiness", "HVACBusiness", "ElectricalContractor", "Plumber"],
  "additionalType": "https://en.wikipedia.org/wiki/Subcontractor",
  ...
}
```

或更简单:

```json
{ "@type": "LocalBusiness", "knowsAbout": [...] }
```

**老板/开发**: 直接修。这是 SEO ROI 最大的一个改动。

---

### 7.2 🟠 JSON-LD 在 `</html>` 后面 — 无效 HTML 结构

**位置**: services.html line 500 (`</html>`) 后面 line 501 才开始 `<script>`,company.html 同问题,5 个 markets 同问题。

**说明**: HTML5 规范要求 `<script>` 在 `<head>` 或 `<body>` 内。Google Rich Results Test 会跳过 `</html>` 之后的内容。当前等于 schema 在 SERP 看不到。

**改成**: 把 JSON-LD `<script>` 移到 `<head>` 或 `</body>` 之前。

---

### 7.3 🟠 缺 LocalBusiness 关键字段

JSON-LD 当前缺:
- `priceRange`
- `openingHours` / `openingHoursSpecification`
- `areaServed` (有但只有 city,缺县级,德州 254 县要列出来主要的)
- `aggregateRating` (即使 0 评论也应该明确不写)
- `sameAs` (LinkedIn / Facebook / Yelp company profile URLs)
- `image` (logo URL)
- `founder` (founder name + role)
- `foundingDate`
- `numberOfEmployees`

**老板必须答**: ✦ 7.3: 公司 founding date + 当前员工数 + 主要 social profiles?

---

### 7.4 🟢 Hero 配色和"安全橙" Brand color

**位置**: 全站 `--safety: #E26B2C`

**说明**: 这个色调是 OSHA "Safety Orange" 的近似 (#FE6E00 是真正 OSHA),但在数字屏上显示偏暖偏品牌橙。问题不大但要注意:
- 真正的 OSHA Safety Orange 是反光色,不是显示色
- 用在 web 上做 brand 是 OK 的但**别在文案里说 "OSHA Safety Orange"** (会被 OSHA 较真)

---

## 八、可信度差距 — 6 项 "shell company smell"

> 这一节会触发采购官"这家公司不真实"的直觉。

### 8.1 🔴 没有 office 物理地址

**位置**: contact.html line 421 `Specific street address & mailing details provided on request as part of prequalification.`

**采购官读到**: "shell company red flag"。

**事实**:
- 任何严肃 B2B sub 的 footer + Contact + Google Business Profile + LinkedIn 都有物理地址。
- TSBPE / TDLR licensing 公开数据库 (publicaccount.tdlr.texas.gov) 有 license 持有人地址,搜得到。
- 不公开物理地址在 ISN / Avetta 评分会扣分。

**老板必须答**: ✦ 8.1: Oak Shield 实际办公地址(Houston 哪个区)?如果是住宅地址或租赁 P.O. Box,要尽快租 commercial co-working space 解决。

---

### 8.2 🔴 没有 founder / leadership

**位置**: company.html 整页 0 提及任何人名

**采购官读到**: "这家公司谁在管?"

**事实**: 行业惯例 company 页或 about 页要有:
- President / Founder 名字 + 简短履历
- VP of Operations 或 General Manager (项目交付负责人)
- Safety Director (Pre-Qual 必填字段)
- Estimating Manager (合同前阶段对接人)

**老板必须答**:
- ✦ 8.2-A: Founder 名字 + 简短履历 (10 年以上 MEP 行业,具体哪些 GC,哪些项目)
- ✦ 8.2-B: 当前管理层 (建议至少 3-5 个名字 + role)
- ✦ 8.2-C: 是否愿意加 leadership 头像?(B2B 网站标配)

---

### 8.3 🔴 4 个 Signature Project 全部没有完成日期

**位置**: index.html / 5 个 markets 项目卡片

**当前**: Costco/Blossom/OCM 完全没有日期; NVIDIA 写 "2026 · Active Phase Build"

**采购官读到**: "项目是 5 年前的还是去年的?公司还活着吗?"

**事实**: Pre-Qual 表单必填字段包括 "Date of Project Completion" + "Project Reference Phone & Email"。

**老板必须答**:
- ✦ 8.3-A: 4 个项目各自 start date + completion date (NVIDIA 是 ongoing 也要 start date)
- ✦ 8.3-B: 4 个项目各自 reference contact (GC PM 名字 + 电话 + 邮箱,Pre-Qual 会打电话验证)

---

### 8.4 🟠 4 个 Signature Project 全部没有合同金额

**问题**: Pre-Qual 标准字段包括:
- Total project value
- Oak Shield's contract value (sub portion)
- Largest project completed (in $)
- Average project size

**老板必须答**: ✦ 8.4: 4 个项目各自的 sub contract value 区间(可不公开具体数字,但 Pre-Qual PDF 必须有)

---

### 8.5 🟠 没有 customer testimonials

**说明**: 即使匿名 testimonial("Project Manager, Tier-1 General Contractor")也比 0 强。

**老板必须答**: ✦ 8.5: 4 个项目各自的 GC PM 是否愿意提供 1-2 句 testimonial?(可匿名)

---

### 8.6 🟠 没有 BIM / 协同软件 stack

**说明**: 数据中心 / 工业级别项目,GC 默认 sub 用 BIM 360 / Bluebeam Revu / Procore / Autodesk Construction Cloud。
**完全不提**让 GC PM 怀疑 "他们还在用 PDF 来回邮件吗?"

**老板必须答**: ✦ 8.6: 实际用的项目协同 stack(列出工具 + 谁负责)

---

## 九、地理覆盖宣称 vs. 现实

### 9.1 🟡 "Texas Statewide" 反复出现

**位置**: 几乎每页

**事实**:
- TX 700+ 英里南北跨度,300+ 英里东西。
- 单一 Houston 为基地的 MEP sub,要覆盖 El Paso / Lubbock / Amarillo / Marfa 项目,crew travel 成本会吃掉所有 margin。
- company.html line 264 有更诚实表达 "We work where our crews can drive home — Houston, Dallas, Austin, San Antonio, and the build corridors connecting them."

**采购官读到 "Statewide"**: "他们能在 Lubbock 干吗?如果中标了能不能调人?如果不能,'Statewide' 是 marketing 噪音。"

**改成**: 把 markets 页 + Hero 全部改成 "Major Texas Build Corridors" 或 "Houston · DFW · Austin · San Antonio + Build Corridors"。"Statewide" 仅用在 schema.org `areaServed`。

---

## 十、专业术语精确度修订

| 当前措辞 | 行业标准措辞 | 严重度 |
|---|---|---|
| `Surety-backed` | `Bonded` 或具体数字 | 🟠 |
| `Insurance: GL · WC · Auto` | 行业标准至少 4 项 (加 Umbrella) | 🔴 |
| `ISN/Avetta/Veriforce capable` | `Active / Enrolled / Onboarding-ready` | 🟠 |
| `TACL` (无级别) | `TACL-A` 或 `TACL-B` | 🟠 |
| `Electrical Master` | `TECL · Master Electrician on staff` | 🔴 |
| `NVIDIA-tenant data center` | `Hyperscale AI build (NVIDIA-class workloads)` | 🟠 |
| `chip 480V · 4000A` | `Mission-Critical Switchgear` | 🔴 |
| `Hyperscale` (随便用) | 严格定义 ≥100MW 单租户 | 🟢 |
| `Texas Statewide` (单一基地) | `Houston-based · Texas Build Corridors` | 🟡 |
| `Self-perform plumbing` (无照) | `Plumbing through licensed partner` 或补 TSBPE 牌 | 🔴 |
| `Medical / lab gas (where applicable)` (无 ASSE) | 删除整行 | 🔴 |
| `Pre-fab assemblies` (无自有 shop) | `Through prefab supplier partners` | 🟠 |
| `Medium- & low-voltage` (无 MV 经验) | `Low-voltage distribution` | 🟠 |
| `Mission-critical UPS install` (无 OEM 授权) | `UPS power feed & connection · OEM commissioning` | 🟠 |

---

## 十一、老板必须回填项汇总表(32 项)

| 编号 | 项目 | 紧急度 |
|---|---|---|
| 2.1-A | TSBPE Plumbing Company License # | 🔴 上线前必填 |
| 2.1-B | 在职 Master Plumber 名字 + 个人 M-XXXXX # | 🔴 |
| 2.1-C | Plumbing 实际是 self-perform 还是 partner? | 🔴 |
| 2.2-A | TACL 等级 (A / B) | 🔴 |
| 2.2-B | Designated Master Electrician 名字 | 🔴 |
| 2.2-C | TACL # / TECL # 实际号码 | 🔴 |
| 2.3 | EPA 608 Universal 持证 refrig tech 数 | 🔴 |
| 2.4 | TX FAL (Fire Alarm License) 状态 | 🟡 |
| 2.5 | ASSE 6010-6030 持证人(决定 medical gas 行去留) | 🔴 |
| 3.1 | Umbrella Liability 限额 | 🔴 |
| 3.2 | Contractors Pollution Liability 限额 | 🔴 |
| 3.3 | Professional Liability / E&O 限额 | 🟠 |
| 3.4 | Inland Marine 限额 | 🟠 |
| 3.5 | Builder's Risk 协作能力 | 🟡 |
| 4.1 | NVIDIA logo 使用授权状态 | 🔴 |
| 4.2 | Costco logo 使用授权状态 | 🔴 |
| 4.3-A | Dallas 项目真实业主 | 🔴 |
| 4.3-B | Dallas 项目真实 GC | 🔴 |
| 4.3-C | Oak Shield 合同抬头方 | 🔴 |
| 5.1-A | 实际 MV 经验 / 最高电压级别 | 🟠 |
| 5.1-B | 如无 MV,services.html 修改确认 | 🟠 |
| 5.2-A | UPS OEM 授权 (Eaton / Vertiv / Schneider / ABB?) | 🟠 |
| 5.2-B | UPS 实际工种(install vs. commissioning) | 🟠 |
| 5.3 | Switchgear 实际经验(Power Module vs. stick-built) | 🟠 |
| 5.4 | Prefab shop 是否自有 | 🟠 |
| 5.5 | NEBB / AABC TAB 认证人员 | 🟢 |
| 5.6-A | IIAR member status + PSM-trained refrig tech | 🔴 |
| 6.1-6.7 | 7 项 Pre-Qual 标准安全数据(EMR/TRIR/DART/LTIR/OSHA-10/30/DFW/BG check) | 🔴 |
| 6.8 | ISN/Avetta/Veriforce 各自状态 + Grade | 🔴 |
| 7.3 | 公司 founding date / 员工数 / social profiles | 🟠 |
| 8.1 | 实际办公地址 | 🔴 |
| 8.2-A | Founder 名字 + 履历 | 🔴 |
| 8.2-B | 管理层 3-5 人 + role | 🟠 |
| 8.2-C | 是否加 leadership 头像 | 🟢 |
| 8.3-A | 4 个项目各自起止日期 | 🔴 |
| 8.3-B | 4 个项目 GC PM reference 联系方式 | 🔴 |
| 8.4 | 4 个项目各自 sub contract value 区间 | 🟠 |
| 8.5 | 4 个项目 GC PM testimonials | 🟠 |
| 8.6 | BIM / 项目协同 stack | 🟠 |

---

## 十二、整改优先级路线图

### Phase 1 — 上线前 P0 (法务 + 监管硬伤,绝对不能上线带着错)

1. ✦ 4.1 / 4.2 — NVIDIA / Costco logo 改脱敏(法务 1 天)
2. ✦ 7.1 — JSON-LD type 改 LocalBusiness(开发 30 分钟)
3. ✦ 2.1 — Plumbing license 状态确认 + 全站 plumbing 措辞改正(法务 + 内容 1 周)
4. ✦ 2.5 — Medical gas 行删除(内容 30 分钟)
5. ✦ 2.2-C / 8.1 — Footer TBD 替换 + 物理地址公开(老板 1 天)

### Phase 2 — Pre-Qual 准备阶段 (1 个月内)

1. ✦ 6.1-6.8 — 7 项安全数据 + Pre-Qual 平台 Active 状态
2. ✦ 3.1 / 3.2 — Umbrella + Pollution Liability 投保
3. ✦ 8.3 / 8.4 — 4 个项目完整数据 (日期 / 金额 / reference)
4. ✦ 8.2 — Leadership 页 + founder 履历

### Phase 3 — 差异化优化 (3 个月内)

1. ✦ 5.x — 技术声明精确度修订
2. ✦ 8.5 — Customer testimonials 收集
3. ✦ 8.6 — BIM stack + 协同工具说明
4. ✦ 7.3 — Schema 完整字段补齐
5. ✦ 6.x — Insights / blog 内容(SEO)

---

## 十三、对老板的一句话总结

> 这个网站 mockup **设计层面是 95 分**(配色 / 字体 / 信息架构 / 视觉张力都到位),**内容层面是 60 分**(措辞会卖,但很多地方"超出了 Oak Shield 真实资质能担保的范围"),**监管 / 法务层面是 30 分**(Plumbing 牌 / Medical gas / NVIDIA 商标 / GeneralContractor schema 全是雷)。
>
> 现在的状态可以拿给朋友 / 投资人看,**但不能上线**也不能拿去投 NVIDIA / 数据中心级别的 RFP。一个有经验的 GC procurement 看完会做两个判断: ① 这家公司视觉做得真好 ② 但内容上感觉不够 ground truth,先不约见面。
>
> 老板回填上面 32 项数据后,我们才能进入 Phase 1 的可上线版本。**最优先 5 项要尽快确认**: Plumbing 牌、Master Electrician、EMR、Umbrella、办公地址。这 5 项缺一项,Pre-Qual 都过不了。

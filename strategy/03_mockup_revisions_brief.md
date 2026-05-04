# Mockup 修订 Brief — 给开发 / AI Agent 直接执行

> 文档用途：本文件是 **可执行修订单**，给老板拿去给代码（开发同学或 Cursor/Claude Code 等 AI Agent）按条目执行。每条修订都包含：① 定位锚点（用页面现有原文搜索）② 当前内容 ③ 改成什么 ④ 改的原因 ⑤ 老板需要回填的真实数据（如有）。
>
> 编写日期：2026-05-04（v1）
> **更新日期：2026-05-04 晚（v2 — 对齐 mockup 5/3 22:18 重建版本）**
> 修订涉及文件：`/oakshield_website/mockup/index.html`
> 修订总数：**3 大块共 9 条**（v2 新增 1 大块 2 条 + 状态对齐）

---

## v2 修订摘要 — 与当前 mockup 对账

mockup 自 5/3 重建后 Compliance 区块已从"4 张 Card"重构为"`<dl>` 表格"形式，旧文案（"Surety-backed" / "capable" / "GL · WC · Auto"）**已不存在**。但**新形式带来的问题**和**脱敏未完成的项目**仍待修复。

| 旧编号 | 内容 | 当前状态 |
|------|------|---------|
| 1.1 TACL/TECL 补级别 | 表格里现为 `[ TACL # — TBD ]` `[ TECL # — TBD ]` | 🟡 旧文案已删，新表格仍是 TBD，需在号码旁/下方加等级 |
| 1.2 Insurance 加 Umbrella | 现拆成 General Liability + Workers' Comp 两行 | 🔴 **回退** — 连 Auto 都没了，更别提 Umbrella |
| 1.3 Bonding 删 Surety-backed | 现为 `[ Single / Aggregate — TBD ]` | 🟢 旧问题已解，待填数字 |
| 1.4 Prequalification 改"capable" | **整行不存在** | 🔴 **缺失** — `<dl>` 表格里没有 Prequalification 这一行 |
| 1.5 新增 EMR 卡 | 现已有 `EMR (Safety) [ TBD ]` 一行 | 🟡 已加，待填 + 缺 OSHA-10/30 信息 |
| 1.6 Capability Statement 两段式 | 现有 `Request Capability Statement (PDF)` + `Prequalification Docs` 两个按钮 | 🟡 视觉上是两段式，但**两个按钮都跳 contact.html**，不是真 Lead Capture |
| 2.1 NVIDIA 删 480V/4000A | line 597 chip 仍为 `480V · 4000A` | 🔴 **未改** |
| Hero SVG 脱敏 | Hero 已改用静态图 `hero_datacenter_construction.png` | 🟢 SVG 动态文字消失，问题自动解决 |
| 2.2-2.5 其他项目 chip 脱敏 | Costco/Blossom/OCM/Industrial chips 全部为定性表达 | 🟢 全部已合规 |
| **新发现 3.1** | line 422 `<span class="lg-nvidia">NVIDIA</span>` 显示 NVIDIA 文字标志 | 🔴 **品牌授权风险** |
| **新发现 3.2** | Footer line 1203-1204 `TACL # — TBD` / `TECL # — TBD` 直接暴露 TBD 占位符 | 🟡 上线前必须填 |

---

## 修订 1 — Compliance & Coverage 表格（dl 结构升级 + 缺失行回填）

**问题定性**：5/3 重建版把 4 张 Card 改成 `<dl>` 6 行表格（HVAC License / Electrical License / GL / WC / Bonding / EMR），形式更轻但**缺 4 项关键信息**：①License 没等级 ②Insurance 缺 Auto + Umbrella ③整段 Prequalification 行不见了 ④EMR 缺工人 OSHA 覆盖率。

### 修订 1.1 — License 行补等级

**定位锚点**：

```
<dt class="text-white/55">HVAC License</dt>
<dd class="font-mono">[ TACL # — TBD ]</dd>
```

**改成**（推荐两行格式，号码 + 级别同时显示）：

```html
<div class="flex justify-between border-b border-line pb-3">
  <dt class="text-white/55">HVAC License</dt>
  <dd class="font-mono">TACL-A · [ # — TBD ]</dd>
</div>
<div class="flex justify-between border-b border-line pb-3">
  <dt class="text-white/55">Electrical License</dt>
  <dd class="font-mono">TECL-Master · [ # — TBD ]</dd>
</div>
```

**原因**：Texas TACL 分 A（无限容量）/ B（≤25 ton），TECL 分 Master / Journeyman。Pre-Qual 里只写号码不写等级，采购员要 google 才能确认，体验差。

**老板需回填**：

- ✦ 1.1-A：Oak Shield 实际持有的是 TACL-A 还是 TACL-B？
- ✦ 1.1-B：电气是 TECL-Master 还是 TECL-Journeyman？
- ✦ 1.1-C：实际 License 号码（届时统一替换 `[ # — TBD ]`）

**同步检查**：footer line 1203-1204 也是 `TACL # — TBD` `TECL # — TBD`，要同步改。

---

### 修订 1.2 — Insurance 必须补 Auto + Umbrella（v2 重要）

**定位锚点**：

```
<dt class="text-white/55">General Liability</dt>
<dd class="font-mono">[ Limits — TBD ]</dd>
...
<dt class="text-white/55">Workers' Comp</dt>
<dd class="font-mono">[ Carrier — TBD ]</dd>
```

**问题**：当前 dl 表只有 GL + WC 两行，**Auto 和 Umbrella 全消失**。任何商业 MEP 承包商都必须有 Commercial Auto Liability（皮卡 / 服务车），数据中心 / 工业 / 政府项目 100% 硬性要求 Umbrella ≥ $5M。

**改成**（4 行 + 1 行折叠备注，或 2 行紧凑式）：

**A. 完整 4 行版（推荐，视觉量级匹配 EMR / Bonding 行）**：

```html
<div class="flex justify-between border-b border-line pb-3">
  <dt class="text-white/55">General Liability</dt>
  <dd class="font-mono">[ $X M / occurrence — TBD ]</dd>
</div>
<div class="flex justify-between border-b border-line pb-3">
  <dt class="text-white/55">Workers' Comp</dt>
  <dd class="font-mono">[ Statutory · Carrier — TBD ]</dd>
</div>
<div class="flex justify-between border-b border-line pb-3">
  <dt class="text-white/55">Commercial Auto</dt>
  <dd class="font-mono">[ $X M CSL — TBD ]</dd>
</div>
<div class="flex justify-between border-b border-line pb-3">
  <dt class="text-white/55">Umbrella / Excess</dt>
  <dd class="font-mono">[ $X M aggregate — TBD ]</dd>
</div>
```

**B. 紧凑 2 行版（如果不想表格变太长）**：

```html
<div class="flex justify-between border-b border-line pb-3">
  <dt class="text-white/55">Liability Coverage</dt>
  <dd class="font-mono">GL · WC · Auto · Umbrella</dd>
</div>
<div class="flex justify-between border-b border-line pb-3">
  <dt class="text-white/55">Coverage Detail</dt>
  <dd class="font-mono">Limits provided on prequalification</dd>
</div>
```

**原因**：缺 Umbrella 在 Pre-Qual 阶段直接被 Equinix/Microsoft/Meta/政府项目刷掉。Auto 缺更基础——皮卡进工地不可能没保险。

**老板需回填**：

- ✦ 1.2-A：GL 单次/累计限额？（典型 $1M/$2M 或 $2M/$4M）
- ✦ 1.2-B：Workers' Comp 保险公司
- ✦ 1.2-C：Commercial Auto 限额（CSL Combined Single Limit）
- ✦ 1.2-D：Umbrella / Excess Liability 限额（$5M / $10M / 其他）
- ✦ 1.2-E：是否同时持 Pollution Liability（HVAC 制冷剂回收）/ Builder's Risk？— 不进首页表格，但 Pre-Qual PDF 必列

---

### 修订 1.3 — Bonding 行（已合规，仅待填）

**定位锚点**：

```
<dt class="text-white/55">Bonding Capacity</dt>
<dd class="font-mono">[ Single / Aggregate — TBD ]</dd>
```

**说明**：旧版"Surety-backed"已删除 ✅。当前格式是干净的，**等老板填数字即可**。

**老板需回填**（二选一）：

- ✦ 1.3-A：实际 Bonding Capacity（如 `$10M Single · $30M Aggregate`）→ 直接替换 TBD
- ✦ 1.3-B：若不愿公开 → 改文案为 `Bondable · Capacity on prequal` 并删除 dt/dd 这一行内的 `[ ... ]` 占位符

---

### 修订 1.4 — Prequalification 行（必须新增，当前缺失）

**问题**：当前 `<dl>` 表 6 行里**完全没有 Prequalification**，但这是 B2B 招投标体系最关键的"通行证"行。

**新增定位**：插在 Bonding 行后、EMR 行前（或紧贴 EMR）。

**新增内容**（按老板真实状态三选一）：

**A. 三个平台都已注册并 Active（理想态）**：

```html
<div class="flex justify-between border-b border-line pb-3">
  <dt class="text-white/55">Prequalification</dt>
  <dd class="font-mono">ISN · Avetta · Veriforce · Active</dd>
</div>
```

**B. 已注册其中部分**：

```html
<div class="flex justify-between border-b border-line pb-3">
  <dt class="text-white/55">Prequalification</dt>
  <dd class="font-mono">ISN Active · Avetta Enrolled · Veriforce TBD</dd>
</div>
```

**C. 都未注册但能快速注册**：

```html
<div class="flex justify-between border-b border-line pb-3">
  <dt class="text-white/55">Prequalification</dt>
  <dd class="font-mono">Onboarding-ready · 5-business-day enrollment</dd>
</div>
```

**原因**：B2B 招投标语境里，没有 ISN/Avetta/Veriforce 等于工业项目门票都没有。**强烈建议老板尽快走完三个平台的注册——这是工业 / 数据中心项目的硬筛选项**。

**老板需回填**：

- ✦ 1.4：ISN / Avetta / Veriforce 当前各自状态 → 决定走 A/B/C 方案

---

### 修订 1.5 — EMR 行扩展（已加，需补 OSHA 信息）

**定位锚点**：

```
<dt class="text-white/55">EMR (Safety)</dt>
<dd class="font-mono">[ TBD ]</dd>
```

**问题**：EMR 行已加 ✅，但**只有一个数字不够**。现场工人 OSHA-10 覆盖率 / 管理层 OSHA-30 覆盖率是 EMR 的同级硬指标。

**改成**（在 EMR 行下方追加一行 Safety Program）：

```html
<div class="flex justify-between border-b border-line pb-3">
  <dt class="text-white/55">EMR (Safety)</dt>
  <dd class="font-mono">[ 0.XX — TBD ] · Below industry avg.</dd>
</div>
<div class="flex justify-between">
  <dt class="text-white/55">Safety Training</dt>
  <dd class="font-mono">100% OSHA-10 field · OSHA-30 leadership</dd>
</div>
```

**原因**：EMR ≤ 1.0 + 100% OSHA-10 是工业 / 数据中心招标硬筛选项，缺一不可。

**注意**：**如果 EMR > 1.0，则不要主动显示具体数字**，留白或写 "Detail provided on prequal"，避免前置失分。

**老板需回填**：

- ✦ 1.5-A：Oak Shield 当前 EMR 数字（如 ≤ 1.0 则填具体值；如 > 1.0 则写 `Detail on prequal`）
- ✦ 1.5-B：现场工人 OSHA-10 覆盖率 / 管理层 OSHA-30 覆盖率
- ✦ 1.5-C：是否有 Drug-Free Workplace Program / Site Background Check Policy？（如有，可在 dl 表下方加一行 chip 或在 Pre-Qual PDF 里写）

---

### 修订 1.6 — Capability Statement CTA：从"两个跳同一页按钮"改成真 Lead Capture（v2 修订）

**定位锚点**：

```
<a href="contact.html" class="btn-primary">Request Capability Statement (PDF)</a>
<a href="contact.html" class="btn-ghost text-white"><span>Prequalification Docs</span></a>
```

**问题**：当前两个按钮在视觉上是两段式 ✅，但**都跳 contact.html**，相当于把所有访客都丢进同一个表单。Capability Statement Public 应当是**直接 PDF 下载（轻 Lead）**，Pre-Qual 才是**重表单（深 Lead）**。

**改成**：

```html
<!-- 公开版 Capability Statement: 直接下载 PDF + 触发轻量 Lead Form -->
<a href="#cap-statement-modal"
   class="btn-primary"
   data-action="open-cap-form"
   data-pdf="/assets/Oak_Shield_Capability_Statement_Public.pdf">
  Download Capability Statement (PDF)
</a>

<!-- Pre-Qual 完整包: 跳 Contact 表单, 主题预填 -->
<a href="contact.html?form=prequal&subject=Prequalification%20Package%20Request"
   class="btn-ghost text-white">
  <span>Request Prequalification Package</span>
</a>
```

**对应 Lead Form 字段**（主按钮 modal 弹窗）：

- Name (必填)
- Work Email (必填，验证非 gmail/yahoo 域)
- Company (必填)
- Project Type (下拉：Data Center / Hospitality / Cold Storage / Big-Box Retail / Industrial / Other)
- Project Location (下拉：Texas City)
- Project Timeline (下拉：< 3 mo / 3-6 mo / 6-12 mo / Exploring)

**提交后**：

1. 自动发邮件到 `estimating@oakshieldservice.com`
2. 自动回邮件给提交者，附带 `/assets/Oak_Shield_Capability_Statement_Public.pdf` 下载链接
3. （可选）提交者邮箱自动加入 HubSpot/Mailchimp Lead List

**Pre-Qual 按钮直接 mailto 也可**：

```html
<a href="mailto:estimating@oakshieldservice.com?subject=Prequalification%20Package%20Request">
```

**原因**：当前两个跳同页 contact.html 浪费了"两段式 CTA"结构。轻 Lead（Capability PDF）抓早期意向 GC/Estimator，重 Lead（Pre-Qual）保护 License#/COI/EMR 详细数字只给真采购流程。

**老板需做**：

- ✦ 1.6-A：准备 `Oak_Shield_Capability_Statement_Public.pdf`（建议 4 页：Markets / Self-Performed Trades / Representative Projects / Contact）
- ✦ 1.6-B：确认接收 Lead 的邮箱（estimating@ / info@ / 其他）
- ✦ 1.6-C：是否需要接 HubSpot / Mailchimp / 仅邮件即可

---

## 修订 2 — Signature Project 敏感数据脱敏

**问题定性**：5/3 重建版的 Hospitality / Cold Storage / Big-Box / Industrial 4 个 Market 已 ✅ 全部脱敏，**仅剩 NVIDIA Data Center 卡片仍残留 `480V · 4000A`**。Hero 区改用静态图后，原 SVG 动态文字脱敏问题自动消失。

**默认审核原则**（开发 / AI Agent 按这把尺扫整个 mockup）：

| 类别 | 处理 |
|------|------|
| ✅ **可以写** | Owner 名字 · 城市 · 大类项目类型 · 你做的工种范围 · 时间窗口（年/月） · Tier 级别（如 Tier III）· 大类定性形容（hyperscale-grade / mission-critical） |
| ❌ **不能写** | 具体电压（除非已脱敏到 "Class XXX"）· 具体安培数 · kW/MW 精确数 · 设备型号或品牌 · 楼宇精确平方英尺（可写大致量级如 "100K+ sqft"）· 库温精确数 · 制冷吨精确数 · 客房精确数 · UPS/PDU 具体规格 · 网络架构 · 安全系统配置 |

### 修订 2.1 — NVIDIA Data Center chip 脱敏（仅剩这一处）

**定位锚点**：line ~597

```html
<span class="chip border border-white/15 text-white/70 text-[10px]">480V · 4000A</span>
<span class="chip border border-white/15 text-white/70 text-[10px]">Mission-critical</span>
<span class="chip border border-white/15 text-white/70 text-[10px]">AI / HPC</span>
```

**改成**：

```html
<span class="chip border border-white/15 text-white/70 text-[10px]">Mission-Critical Switchgear</span>
<span class="chip border border-white/15 text-white/70 text-[10px]">AI / HPC Tenant</span>
<span class="chip border border-white/15 text-white/70 text-[10px]">Active Phase Build</span>
```

**说明**：删除 "480V · 4000A" 具体技术参数，替换为脱敏定性表达。其他 3 个 chip 不变。

---

### 修订 2.2 - 2.4 — Hospitality / Cold Storage / Big-Box（已合规）

| Market | 当前 chips | 状态 |
|--------|----------|------|
| Hospitality (Blossom) | All Trades · Guest-room VRF · F&B kitchen | ✅ 定性 OK |
| Cold Storage (OCM) | Walk-in / Freezer · Process refrig. · Food-grade | ✅ 定性 OK |
| Big-Box (Costco) | RTU / packaged · Refrigerated cases · National prototype | ✅ 定性 OK |

**老板检查项**：上述 chips 措辞是否匹配实际项目交付内容？如有偏差，按"❌ 不能写"原则替换。

---

### 修订 2.5 — Industrial chip（已合规）

**当前 chips**：`Process piping · High-tonnage · 24/7 turnover` ✅ 全部定性。

**可选优化**：第三个 chip 可改成 `Capability · No Reference Project Yet` 诚实表达"该垂直暂无可披露案例"，比假装有更可信。但当前 `24/7 turnover` 也不算虚构（属于通用工艺特征），可保留。

**老板决定**：保留现状 / 替换为 "Capability Highlight" 表达。

---

## 修订 3 — 品牌授权与 TBD 暴露（v2 新增）

### 修订 3.1 — Owner Logo Strip 的 NVIDIA 文字标志

**定位锚点**：line ~422

```html
<span class="lg-nvidia">NVIDIA</span>
```

**问题**：line 284 注释虽写了"placeholder, NOT actual NVIDIA logo"，但实际 DOM 输出仍是 "NVIDIA" 字样（哪怕用了自定义字体），任何采购员/律师都会理解为"声称 NVIDIA 为客户"。**NVIDIA 是商标受高度保护的对象，未授权显示其名字 / 标志是高风险**。

**改成**（三选一，按授权状态）：

**A. 已获得 NVIDIA 客户授权（理想态）**：

保留 NVIDIA 文字 + 加一个 footnote：

```html
<span class="lg-nvidia">NVIDIA</span>
<!-- 紧邻 logo strip 下方加一行 -->
<p class="text-[9px] text-white/30 mt-2">
  Client and trade-partner names shown with permission. Specific scope and project details available under NDA.
</p>
```

**B. 没有客户授权（最常见）**：

替换为脱敏表达：

```html
<span class="lg-nvidia">Hyperscale AI Tenant</span>
```

或

```html
<span class="lg-nvidia">Mission-Critical Tenant</span>
```

**C. 完全删除 NVIDIA logo（最保守）**：

把 logo strip 整个换成项目类型 strip：

```html
<span>Data Center</span>
<span>Big-Box Retail</span>
<span>Hospitality</span>
<span>Cold Storage</span>
```

**原因**：B2B 网站显示客户 logo **必须有书面授权**（Logo Usage Approval / Marketing Release）。NVIDIA / Costco / Blossom Hotel / OCM 这种规模的 Owner 100% 有 brand guideline，未授权使用 = 律师函。**这是法务硬伤，不是审美问题。**

**同步审核**：line 426-431 的 Costco / Blossom Hotel / OCM 同样是文字 logo：

```html
<span class="lg-costco">COSTCO</span>
<span class="lg-blossom">Blossom Hotel</span>
<span class="lg-ocm">OCM<span> · MUSHROOM</span></span>
```

按相同三选一原则处理（推荐 B 或 C 方案）。

**老板需做**：

- ✦ 3.1-A：是否已与 NVIDIA / Costco / Blossom / OCM 任何一方拿到 logo 使用授权？
- ✦ 3.1-B：如有授权，提供授权信扫描件存档（防 marketing 律师抽查）
- ✦ 3.1-C：如无授权，确认走 B 或 C 方案

---

### 修订 3.2 — Footer TBD 占位符必须上线前清掉

**定位锚点**：line ~1203-1204

```html
<span>TACL # — TBD</span>
<span>TECL # — TBD</span>
```

**问题**：footer 直接显示 `TACL # — TBD` `TECL # — TBD`，访客一眼看到 "TBD" 会判定"这家公司还没准备好"。

**改成**（基于修订 1.1 的真实 license）：

```html
<span>TACL-A · #XXXXXX</span>
<span>TECL-Master · #XXXXXX</span>
```

**原因**：mockup 阶段允许 TBD，**上线前 100% 必须替换**。建议在 README.md 的"上线前 Checklist"加一条：全文搜索 `TBD` 应当返回 0 结果。

---

## ✦ 老板回填项汇总（一次性提供给我，我直接生成最终 HTML）

| 编号 | 待回填项 | 老板答 |
|------|----------|--------|
| 1.1-A | TACL 等级（A / B） | |
| 1.1-B | TECL 等级（Master / Journeyman） | |
| 1.1-C | TACL / TECL 实际号码 | |
| 1.2-A | GL 限额（如 $2M/$4M） | |
| 1.2-B | Workers' Comp 保险公司 | |
| 1.2-C | Commercial Auto 限额（CSL） | |
| 1.2-D | Umbrella / Excess Liability 限额 ($5M / $10M / 其他) | |
| 1.2-E | 是否持 Pollution Liability / Builder's Risk（仅 Pre-Qual PDF 用） | |
| 1.3 | Bonding Capacity（Single / Aggregate 数字，或选 "不公开"走 Bondable 方案） | |
| 1.4 | ISN / Avetta / Veriforce 当前各自状态（Active / Enrolled / Not yet） | |
| 1.5-A | EMR 当前数字（如 ≤ 1.0；如 > 1.0 选"不主动显示"） | |
| 1.5-B | OSHA-10 现场覆盖率 / OSHA-30 管理层覆盖率 | |
| 1.5-C | 是否有 Drug-Free Workplace / Background Check Policy | |
| 1.6-A | Capability Statement Public PDF 是否已准备（4 页结构） | |
| 1.6-B | 接收 Lead 的邮箱（estimating@ / info@ / 其他） | |
| 1.6-C | 是否需要接 HubSpot / Mailchimp / 仅邮件即可 | |
| 3.1-A | NVIDIA / Costco / Blossom / OCM logo 使用授权状态 | |
| 3.1-B | 如有授权,提供授权信扫描件 | |

---

## 验收清单（开发 / AI Agent 改完后老板检查）

### Compliance & Coverage 表格

- [ ] HVAC License 行显示 `TACL-A · #XXXXXX`（不再是裸 # — TBD）
- [ ] Electrical License 行显示 `TECL-Master · #XXXXXX`
- [ ] Insurance 至少 4 行（GL / WC / Auto / Umbrella），或 2 行紧凑式包含全部 4 项
- [ ] Bonding 行有具体数字或显示 `Bondable · Capacity on prequal`
- [ ] **新增 Prequalification 行**（A/B/C 任一方案）
- [ ] EMR 行有数字 + 紧邻一行 Safety Training（OSHA-10/30）
- [ ] Capability Statement 主按钮触发 Lead Form modal（不是跳 contact.html）
- [ ] Pre-Qual 按钮跳 contact.html?form=prequal 或 mailto

### Signature Project 脱敏

- [ ] NVIDIA 卡片 chip 不再出现 `480V · 4000A`
- [ ] 全文搜数字 + `V`、数字 + `A`、数字 + `MW`、数字 + `kW`、数字 + `ton`、数字 + `°F` 应当 0 结果（除 alt text 中通用描述）

### 品牌授权

- [ ] Owner Logo Strip 的 NVIDIA / Costco / Blossom / OCM 文字按 A/B/C 方案处理
- [ ] 如保留客户名，加授权 footnote
- [ ] Footer 不再出现 `TBD` 字样（全站搜索 `TBD` 应 0 结果）

### 全站扫一遍同类问题

- [ ] 全站搜 `TBD` → 0 结果
- [ ] 全站搜具体技术参数（电压/电流/MW/吨/°F）→ 仅保留定性表达
- [ ] 所有 client/tenant 名字均有授权或已脱敏

---

## 一句话总结（给开发 / AI Agent）

> v2 共 9 条修订（v1 的 7 条 + v2 新增 2 条）：
>
> **修订 1（1.1 - 1.6）**：把 `<dl>` 表格从"看起来轻"升级到"采购员看完直接放进 Approved Bidder 名单"，重点补 Insurance 缺的 Auto + Umbrella，以及消失的 Prequalification 整行。
>
> **修订 2（2.1）**：仅剩 NVIDIA chip `480V · 4000A` 一处脱敏（其他 4 个 Market chips 已合规）。
>
> **修订 3（3.1 - 3.2）**：法务级硬伤——客户 logo 文字标志必须按授权状态处理（NVIDIA 风险最高），上线前 footer 不能留 TBD。
>
> 9 条全部改完后，Mockup 的"信任建立 + 法务合规"模块就过线了，可以进入下一阶段（4 个 Signature Project 标准化案例页 + Markets 拆独立 Landing Page）。

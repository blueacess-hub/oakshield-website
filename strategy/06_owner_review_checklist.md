# Oak Shield 网站修改清单 — 等你逐项审批

> **使用方法**: 每行末尾 `[ ]` 是你打勾的位置,改成 `[x]` 表示同意,或在备注栏写"否"/修改意见。
>
> 全部审完发回,我开干 5 页 mockup 修改。
>
> 编写日期: 2026-05-06 · 基于 Owner Questionnaire v2 回填

---

## 第一组 · 立即可加(高价值实锤数据)

### A. Footer / Schema.org / 联系页

| # | 内容 | 拟加位置 | 同意? | 备注 |
|---|---|---|---|---|
| A1 | TACL # **111021** Class A | footer + JSON-LD,替换 [pending] | [x ] | |
| A2 | TECL # **TACLA111021C** | footer + JSON-LD | [ x] | |
| A3 | Designated Master Electrician: **Xinchao Xi** | services.html / company.html | [x ] | |
| A4 | 公司地址: **1819 First Oaks St #180, Richmond, TX 77406** | footer + contact.html + JSON-LD | [ x] | |
| A5 | 物业类型: Commercial space + 自有 warehouse/yard | contact.html "Office & Operations" | [ x] | |
| A6 | 创办年份 **2016** | About / JSON-LD foundingDate | [ x] | |
| A7 | 员工总数 **30**(field 25 / office 5) | JSON-LD numberOfEmployees + 数字栏 | [ x] | |
| A8 | 营收级别 **$5–10M** | Capability Statement(网站不显式公开) | [ 不写] | |

### B. Founder / Leadership(消除 shell company 红旗)

| # | 内容 | 拟加位置 | 同意? | 备注 |
|---|---|---|---|---|
| B1 | Founder / President: **Xinchao Xi**,17 年 MEP 行业 | About 页新建 Leadership 区 | [ x] | |
| B2 | Founder LinkedIn URL(老板同意加) | About + Schema sameAs | [ x] | URL: ____________ |
| B3 | Founder 头像 | About 页 | [ x] | 老板提供照片 |
| B4 | VP / GM: **Ben** | Leadership 卡片 | [ x] | 全名+履历? |

### C. EHS Safety 数据(B2B 招标硬通货,新建 Safety 板块)

| # | 指标 | 数据 | 拟加位置 | 同意? | 备注 |
|---|---|---|---|---|---|
| C1 | EMR | **0.85**(5年趋势 0.9) | 首页 + Safety 子页 | [ x] | |
| C2 | TRIR | 2.2 | Safety 子页 | [ x] | |
| C3 | DART | **0** | 首页 + Safety 子页 | [ x] | |
| C4 | LTIR | 1 | Safety 子页 | [ x] | |
| C5 | OSHA-10 现场覆盖率 | **100%** | 首页 + Safety 子页 | [ x] | |
| C6 | OSHA-30 管理层覆盖率 | **100%** | Safety 子页 | [ x] | |
| C7 | 重认证周期 | 每 3 年 | Safety 段 | [ x] | |

### D. 技术能力实锤(Markets / Services 升级)

| # | 内容 | 拟加位置 | 同意? | 备注 |
|---|---|---|---|---|
| D1 | **MV 实际经验 Y,最高 25kV** | data-centers / industrial 页大写特写 | [x ] | |
| D2 | MV-trained 电工 **15 人** | 同上 | [ x] | |
| D3 | UPS 厂家授权: **Eaton + ABB authorized partner**(仅 install + power feed,不含 commissioning) | data-centers 页(明确范围) | [ x] | |
| D4 | Switchgear: 整套 Power Module + Stick-built **两种都做过** | data-centers / industrial | [x ] | |
| D5 | EPA 608 持证: **15 HVAC tech 中 7 人持 Type II 高压商用** | refrigeration / cold-storage 页 | [ x] | |
| D6 | NVIDIA Dallas 项目定性: **≥100MW Hyperscale**,GC = GPI,业主侧 = WESCON | data-centers 页 | [x ] | |

### E. 保险数据(Capability Statement)

| # | 内容 | 拟加位置 | 同意? | 备注 |
|---|---|---|---|---|
| E1 | Umbrella **$2M / USLI / 到期 03/09/2027** | Capability Statement(网站可不公开,见决策 J3) | [ ] | |
| E2 | CPL **$1M / USLI**(明确不覆盖 NH3) | Capability Statement | [x ] | |
| E3 | Builder's Risk: 可 join GC named insured | Capability Statement | [ x] | |

### F. Signature Project 时间线 + 金额(Projects 页升级)

| # | 项目 | 起止 | 合同金额 | GC | 同意公开? | 备注 |
|---|---|---|---|---|---|---|
| F1 | NVIDIA Dallas (Hyperscale) | 02/2025 至今 | $3–5M | GPI | [ ] |项目金额和甲方不用写 |
| F2 | Costco Business Center, Stafford | 03/2021 – 06/2022 | $5–10M | (待补) | [ ] | |
| F3 | Blossom Hotel, Houston | 01/2022 – 08/2024 | $5–10M | (待补) | [] | |
| F4 | OCM Mushroom Cold Storage | 10/2025 | $3–5M | FINC | [ ] | |

---

## 第二组 · 必须改或删(网站现状超出真实资质,审计风险)

| # | 网站现状 | 老板回答 | 拟改动作 | 同意? | 备注 |
|---|---|---|---|---|---|
| G1 | "Self-perform 4 trades(含 plumbing)" 共 5 处 | Plumbing 是分包,无 TSBPE | 全站改 "Self-perform HVAC + Refrigeration + Electrical;Plumbing through licensed TSBPE partner" | [ 不改] | |
| G2 | services.html "Medical / lab gas (where applicable)" | 0 持证 + 确认删除 | **删除整行** | [ x] | |
| G3 | "Fire alarm coordination" | 通过分包 | 改 "FA raceway/conduit only;detection via licensed partner" | [x ] | |
| G4 | "Pre-fab capability" 暗示自有 | 无自有 shop | 改 "Through pre-fab supplier partners" 或删除 | [ 删除] | |
| G5 | Cold Storage FAQ "we carry the qualifications" 关于 NH3 | 无 IIAR/PSM,但做过 600 lbs | 改 "NH3 systems delivered through IIAR-certified partner;Oak Shield performs MEP coordination & ancillary scope" | [x ] | |
| G6 | "ISNetworld · Avetta · Veriforce capable" | 三个都未注册 | 删除"capable"措辞 | [ x] | 见决策 J5 |
| G7 | NEBB/AABC TAB 暗示 | 0 持证 | 不出现 TAB 自有能力,只写 "TAB through certified specialist" | [ x] | |
| G8 | Services 页暗示 design-assist / design-build | E&O 未购买 | 措辞收紧到 "constructibility review" | [ x] | |
| G9 | Inland Marine | 未购买 | Capability Statement 不列 | [ x] | |
| G10 | Drug-Free Workplace + Background Check | 全 N | 网站不出现这两条 | [ x] | |
| G11 | Schema.org type 是 GeneralContractor | (项目自身问题) | 5 个文件改 LocalBusiness + HVACBusiness + ElectricalContractor + Plumber 多类型,JSON-LD 移到 `</body>` 前 | [ ] | |

---

## 第三组 · 等你拍板(请勾选方案)

### J1 — NVIDIA logo 怎么处理(无授权)

- [x ] **A. 改成脱敏文字 "Hyperscale AI Tenant" + 项目级别说明 ≥100MW** ⭐ 推荐
- [ ] B. 完全删除 NVIDIA 名字
- [ ] C. 保留 NVIDIA + 加 footnote(法务风险高,不推荐)

备注: ____________

### J2 — Costco / Blossom / OCM logo 处理(全无授权)

- [ ] **默认走 B 方案脱敏**(改成文字描述,不用 logo + 不用品牌色) ⭐ 推荐
- [ ] 其他方案: __costco改个模糊词 其他两个不用处理__________

### J3 — Umbrella 限额($2M)是否在网站公开

- [ x] **A. 网站只列 GL/WC/Auto,Umbrella 留 Capability Statement PDF(签 NDA 后给)** ⭐ 推荐
- [ ] B. 网站直接写 $2M(小项目无影响,大项目 PM 看到会跳过)

备注: ____________

### J4 — 是否新建 Safety Stats 板块

- [ x] **A. 首页 + Safety 子页正面打 EMR/TRIR/DART/OSHA,不提缺项(DFW/Background)** ⭐ 推荐
- [ ] B. 暂不上 Safety 板块,等 DFW Policy + Background 走完流程再上

备注: ____________

### J5 — Pre-Qual 平台措辞(三平台都未注册)

- [ x] A. 网站完全不提 Pre-Qual,改写 "Complete pre-qualification packages on request"
- [ ] B. 写 "Pre-Qual onboarding underway — ETA Q3 2026"
- [ ] **C. 先花一周注册 ISNetworld(年费 ~$399),再上线** ⭐ 强烈建议

备注: ____________

### J6 — data-centers 页 NVIDIA 项目要不要写满 ≥100MW

- [x ] **A. 直接写 "≥100MW Hyperscale AI Cluster"(强卖点)** ⭐ 推荐
- [ ] B. 保留模糊 "Mission-critical AI workload"

备注: ____________

---

## 第四组 · 后续补(不阻塞上线)

| # | 缺什么 | 影响 | 何时补? |
|---|---|---|---|
| K1 | Estimating Manager / Safety Director / Sr. PM 全名+履历 | About 页 Leadership 现阶段只放 2 人 | ____________ |
| K2 | 4 个项目的 GC PM 姓名+电话+邮箱 | 网站写 "References available on request",Pre-Qual 会卡 | ____________ |
| K3 | Costco / Blossom 项目的 GC 名字 | Projects 页这两个先只写 "Confidential GC" | ____________ |
| K4 | Switchgear 最大体量(kVA / breaker 数) | data-centers 页 switchgear 段先泛写 | ____________ |
| K5 | Plumbing / FA 分包商名字 + 持牌人 | services.html 改 "TSBPE-licensed plumbing partner"(不点名) | ____________ |
| K6 | LinkedIn / GBP / 任何 social URL | sameAs schema 留空。**建议优先开 Google Business Profile** | ____________ |

---

## 我建议你这周做的两件事(可独立于网站修改)

| # | 行动 | 成本 | 周期 | 同意? |
|---|---|---|---|---|
| L1 | 注册 ISNetworld(任何 GC 第一句就问 ISN ID) | ~$399/年 | 7–10 天到 Active | [ ] |
| L2 | 开 Google Business Profile(本地 SEO 必备) | 免费 | 30 分钟 | [ ] |

---

## 总览统计

- 第一组(可加): 8+4+7+6+3+4 = **32 条**
- 第二组(必改): **11 条**
- 第三组(决策): **6 个决策点**
- 第四组(后续补): 6 项
- 周边行动: 2 项

**全部审完发回,我立即修订 5 页 mockup HTML。**

---

*— Oak Shield Website Project Team · 2026-05-06*

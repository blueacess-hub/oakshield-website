# Oak Shield Service 网站改版 — 策略 & 素材请求

**日期**: 2026-05-04
**阶段**: 样板审阅前
**目标**: 把一个空壳WordPress站，改造成能撬动德州B2B商业/工业MEP RFP的销售工具

---

## 1. 核心定位（不能动）

**一句话定位**:
> Texas-based commercial & industrial MEP contractor — self-performed HVAC, refrigeration, electrical & plumbing for inspection-driven complex projects.

**目标受众（按优先级）**:
1. **General Contractors** 的Project Manager / Estimator — 找MEP分包
2. **Owner / Developer** 项目方 — 直接找turnkey MEP
3. **Design Teams (MEP engineers, architects)** — 推荐合作的施工方

**绝对不是**:
- 住宅业主 (Homeowner)
- 紧急维修客户 (Emergency Service)
- 个人定制装修

→ 任何"24/7 Emergency"、"$59 Tune-up"、"Free Estimate"这类住宅HVAC话术，**全部禁用**。

---

## 2. 竞争对手 & 差异化

**德州商业/工业MEP头部对手**：
- TDIndustries（达拉斯，最大）
- Way Companies（休斯顿）
- Comfort Systems USA（休斯顿，公开上市）
- McKinstry（多州，不限德州）
- Letsos Company（休斯顿）
- DBR Engineering（设计端）

**Oak Shield目前能讲的差异化**（从已有案例提炼）：

| 维度 | 大厂 | Oak Shield |
|------|------|-----------|
| 自营4个trade | ✓（但分成多个子公司） | ✓ 单点责任 |
| Mission-critical数据中心 | ✓ | ✓ NVIDIA案例背书 |
| 食品级冷库 | 部分 | ✓ 专业能力 |
| 反应速度/灵活性 | 慢 | 快（中小盘） |
| 单项目体量 | $10M+ | $500K–$5M（推测） |
| 客户层级 | 大GC | 中小GC + 灵活Owner |

→ **Oak Shield的甜点位**：中等规模复杂项目（$500K–$5M MEP合同），客户嫌大厂慢/价高、嫌小厂没经验。

---

## 3. 网站架构（最终版）

### 主页面（保持5页+扩展2页）

| 页面 | 现状 | 改版后定位 | 优先级 |
|------|------|-----------|--------|
| Home | 1行字 | Hero + Services概览 + Markets + Featured Projects + Why + CTA | 🔴 P0 |
| Services | 4段文字 | 4个trade详情卡片 + Integrated MEP亮点 + 单trade case study | 🔴 P0 |
| Projects | 4个项目纯文字 | 4-8个项目带图卡片 + 按行业/规模筛选 + 详情子页 | 🔴 P0 |
| Company | 4段文字 | Story + Leadership + Safety/Compliance + License/EMR/Bonding + Capability Statement下载 | 🔴 P0 |
| Contact | 邮箱+电话 | RFP表单 + 直拨 + 邮件 + 地图 + 服务区 + 办公时间 | 🔴 P0 |
| **Markets**（新） | 无 | 5个垂直行业独立landing page（Data Center / Hospitality / Cold Storage / Big-Box Retail / Industrial）→ Local SEO + RFP针对性 | 🟠 P1 |
| **Insights**（新） | 无 | 行业内容（Texas data center electrical trends / cold storage compliance），用于SEO权重和教育型内容 | 🟢 P2 |

### 主CTA层级

```
Primary CTA（出现在每个页面）: "Submit Project Inquiry" 或 "Request Capability Statement"
Secondary CTA: "Call 713-815-0552"
辅助路径: "Download Capability Statement (PDF)" / "Prequalification Documents"
```

→ **不要**用 "Get a Free Quote"，B2B分包不是这种逻辑。

---

## 4. 视觉设计方向

### 配色（已应用在样板）
- **Ink** `#0B1220` — 主背景深蓝黑
- **Steel** `#1F2A3F` — 卡片/边框
- **Paper** `#F4F4F0` — 浅色块
- **Safety Orange** `#E26B2C` — 强调色（灵感来自施工安全色，呼应"Shield"品牌名）
- **Signal Blue** `#5BA5C9` — 蓝图、技术辅助色

→ 不用纯黑（太丧）、不用蓝白（太医疗）、不用绿色（太低端）。橙色是工程行业的信任色。

### 字体
- **Manrope**（标题）— 几何工业感
- **Inter**（正文）— 数字/技术现代

### 摄影方向（**最重要的素材**）
- 大量使用**真实项目现场施工照片**：Ductwork安装、机房、冷库、配电盘
- **Before/After**对比（机房改造类）
- **航拍/远景**（数据中心、酒店外观）— 体现项目规模
- **细节特写**（焊接、铭牌、控制柜）— 体现工艺
- **避免**：库存图（Shutterstock那种戴安全帽笑的工人）

---

## 5. SEO策略

### 核心关键词矩阵

| 类型 | 关键词示例 | 月搜索量预估 | 落地页 |
|------|-----------|------------|--------|
| 品牌 | oak shield service | <100 | Home |
| 城市+服务 | commercial hvac contractor houston | 200-500 | Services /HVAC + Home |
| 城市+服务 | industrial electrical contractor dallas | 150-300 | Markets/Industrial + Services/Electrical |
| 行业+服务 | data center electrical contractor texas | 100-300 | Markets/Data-Centers ⭐⭐⭐ |
| 行业+服务 | food grade cold storage contractor texas | 50-150 | Markets/Cold-Storage |
| 行业+服务 | hotel mep contractor houston | 50-150 | Markets/Hospitality |
| 长尾 | walk-in freezer installation houston | 50-100 | Services/Refrigeration |

### 必做SEO动作
1. 每页独立`<title>`和`<meta description>`
2. **LocalBusiness Schema**（含address、phone、area served）
3. **Service Schema**（每个服务页）
4. **Organization Schema** + sameAs链接到LinkedIn/Google Business Profile
5. 建立 **Google Business Profile** — Houston地址 + 服务半径 + 项目照
6. 在 **Yelp / BBB / Texas Construction directories** 注册
7. Markets页URL用语义化路径：`/markets/data-centers`, `/markets/hospitality`等
8. Sitemap.xml + robots.txt + Google Search Console验证

### 反派项（不做的）
- ❌ 买Google Ads导流住宅关键词
- ❌ 给"Houston Cheap HVAC"这种低质流量做内容
- ❌ Yelp Pro / Angi类住宅平台

---

## 6. 转化与跟进

### 表单字段最小集（已在样板里）
Full Name · Company · Email · Phone · Project Type · Scope Needed · Project Location · Scope Description · GC联系人确认checkbox

### 必做后端动作
1. 表单提交 → 同时发邮件到 `info@oakshieldservice.com` + Slack/微信通知
2. 自动回复邮件（1分钟内，告知1个工作日响应）
3. CRM最简版：Notion / Pipedrive / HubSpot Free 任选
4. Capability Statement PDF下载需留邮箱（轻表单，不强制）

---

## 7. 我需要你提供的素材清单 ⚠️

按重要性从高到低，标 🔴 = 必须，🟠 = 重要，🟢 = 加分：

### A. 项目素材（最最最重要）

| 项目 | 需要素材 | 优先级 |
|------|---------|--------|
| **NVIDIA Data Center (Dallas)** | 现场照片3-5张（机房/配电柜/线管/远景）+ 项目规模数据（sqft / 电力容量 / 工期）+ 是否能挂NVIDIA名/Logo（**关键合规问题**） | 🔴 |
| **Costco Business Center (Stafford)** | 现场照片3-5张（屋顶机组/管道/室内）+ sqft + Costco Logo使用授权 | 🔴 |
| **Blossom Hotel Houston** | 现场照片+酒店外观图 + 房间数 + GC名字 | 🔴 |
| **OCM Mushroom Cold Storage** | 现场照片+冷库内部 + 容量(立方英尺/吨位) + 温度区间 | 🔴 |
| 其他已完成项目 | 任何能用的项目，越多越好 | 🟠 |

⚠️ **关于客户Logo和项目名展示**：B2B项目通常需要客户书面同意才能在网站展示。如果NVIDIA/Costco没明确同意，需要做**模糊处理**（"Major hyperscale data center in Dallas area" / "National membership warehouse retailer"）。**这事必须提前确认**，否则有法律风险。

### B. 公司基本信息

| 项目 | 内容 |
|------|------|
| 🔴 公司Logo（矢量SVG/AI/EPS最好） | 当前样板用占位盾牌图标 |
| 🔴 公司Houston办公地址 | 用于Google Business Profile + Footer + Schema |
| 🔴 TACL # (Texas HVAC License Number) | Footer + Trust页 |
| 🔴 TECL # (Texas Electrical License Number) | Footer + Trust页 |
| 🔴 General Liability保险限额 + 保险公司 | Trust页 |
| 🔴 Workers' Comp Carrier | Trust页 |
| 🟠 Bonding Capacity（单笔/总额） | Trust页 |
| 🟠 EMR (Experience Modification Rate) — 安全记录 | Trust页 |
| 🟠 公司成立年份 | About页用于"Since 20XX" |
| 🟠 团队规模（field employees数量） | 信任要素 |
| 🟢 创始人/Leadership照片+简介 | Company页 |
| 🟢 Safety Awards / Industry Awards | Trust页 |

### C. 合作伙伴

| 项目 | 内容 |
|------|------|
| 🟠 合作过的GC清单 + Logo使用权（Logo Wall） | 强信任信号 |
| 🟢 合作过的设备品牌（Trane, Carrier, Lennox等）+ Logo | 行业绑定信任 |
| 🟢 工会/协会成员资格（NECA, MCAA, ABC等） | 行业认可 |

### D. 数字与故事

| 项目 | 内容 |
|------|------|
| 🟠 累计完成项目数 | "X+ projects across Texas" |
| 🟠 累计MEP合同金额（粗估） | "$XXM+ in MEP scope delivered" |
| 🟠 累计sqft面积 | "X.XM+ sqft installed" |
| 🟢 1-2个客户quote/推荐语 | Testimonial区 |
| 🟢 创业故事（为什么叫Oak Shield） | About页 |

---

## 8. 阶段计划

### Phase 1 — 样板审阅（本周）
- [x] 抓取现网站，做完整审计
- [x] 做出首页样板HTML（**已完成 → 需要你看**）
- [ ] 你审阅样板：方向对不对、配色行不行、文案口吻
- [ ] 提供素材清单的关键素材（至少A组项目照 + B组核心信息）

### Phase 2 — 完整设计（确认方向后1-2周）
- [ ] 做完所有内页样板（Services / Markets×5 / Projects / Company / Contact）
- [ ] 替换占位图为真实项目摄影
- [ ] 撰写最终文案（基于真实项目数据）
- [ ] 做Capability Statement PDF模板

### Phase 3 — 落地实施（2-3周）
- [ ] 决定技术栈（建议：**WordPress + 自定义主题**或**Webflow**，看后续维护人是谁）
- [ ] 开发主题/搭建站点
- [ ] 接入表单 → 邮箱+CRM
- [ ] SEO基础（schema, sitemap, GSC, GBP）
- [ ] 上线 + 域名切换

### Phase 4 — 持续运营（上线后）
- [ ] Google Business Profile优化（每月发项目动态）
- [ ] 每季度新增2-3个项目案例
- [ ] 行业内容博客（每月1-2篇）
- [ ] 反向链接策略（Texas建筑协会、AGC、合作GC站点）

---

## 9. 决策点（需要你拍板）

下面这些我有倾向但要你确认：

1. **客户Logo展示策略**：直接挂NVIDIA/Costco大Logo（高风险高回报）还是模糊处理（安全但弱）？
   - 我建议：**先去信合作过的GC/Owner书面确认**，能挂就挂，不能挂就用"Hyperscale AI Data Center · Dallas Area"这种描述
2. **技术栈**：保留WordPress（成本低、维护简单、SEO插件多）还是换Webflow（设计灵活、维护贵）？
   - 我建议：**WordPress**。德州本地维护人好找，且现有域名+SEO权重不丢
3. **Markets页是否值得做5个独立页**？
   - 我建议：**做**，这是最关键的SEO杠杆点。Data Center页一年能撬动百万级RFP
4. **是否做西语版本**？
   - 德州西语客户多，但B2B商业项目主要英文沟通。我建议**Phase 4再考虑**

---

## 10. 接下来要你做的两件事

1. **打开样板看方向**：双击下面的index.html，在浏览器看完整效果，告诉我：
   - 配色对不对（深沉工业 vs 太冷/太暖）
   - Hero的话术对不对（"Mechanical, Electrical & Refrigeration — built for Texas's most complex projects"）
   - 整体布局结构合不合理（要不要加/减区块）

2. **回复素材清单**：A组项目素材+B组公司信息能给多少给多少，我会基于真实数据更新文案

# Background Check Policy 模板

**用途**：Oak Shield Service LLC — ISNetworld / Avetta / Veriforce 入网审核 + GC 现场准入要求 + 客户场地（数据中心、医院、政府设施等）背调要求
**起草日期**：2026-05-15
**生效**：经 President 签字后即生效

---

## 关于认证 — 给 Ben 的简版答复

**结论：不需要任何政府部门认证，但必须严格遵守 FCRA 联邦法律流程，否则会被起诉。**

| 法规 / 平台 | 是否需要认证 | 真正要做的事 |
|------------|-------------|-------------|
| FCRA（Fair Credit Reporting Act） | 不发证 | 必须有 standalone Disclosure & Authorization Form + Pre-adverse / Adverse Action 流程 |
| EEOC | 不发证 | 不能 blanket ban，要做 individualized assessment |
| Texas 州法律 | 无州级 ban-the-box | 私营企业自由度高 |
| Austin 市 | 有 ban-the-box（2016） | Oak Shield 在 Richmond，**不受约束** |
| Houston / Fort Bend County | 无市级 ban-the-box | 自由 |
| ISN / Avetta | 不发证 | 上传政策 PDF + 抽查执行证据 |
| 联邦合同 | E-Verify 强制 | SAM.gov 注册时勾选 |

**关键合规点（FCRA Top 3 踩坑）**：
1. **Disclosure 必须是单独文档** —— FCRA §604(b)(2)(A)，不能埋在 employment application 里。这是被起诉最多的点（Whole Foods 2017、Frito-Lay 2014、UPS 都败诉过）。
2. **Pre-adverse Action Notice 必须等 5 个工作日**才能发 Adverse Action Notice —— 给候选人 dispute 的窗口。
3. **不能 blanket 拒绝有犯罪记录的人** —— EEOC 要求 individualized assessment（罪名性质 + 时间 + 岗位相关性）。

**部署流程**：
1. 选 CRA 供应商（Sterling 或 Checkr，二选一）
2. CRA 会给你一套合规模板（Disclosure / Authorization / Adverse Action）—— 直接用他们的，**别自己拟**
3. 把本政策签字采纳 → 存档
4. 现有 25 个 field 员工跑一遍合规背调（一次性约 $1,000–1,500）
5. 上传政策 PDF 到 ISN / Avetta

---

## 政策正文（英文，可直接交付）

```
═══════════════════════════════════════════════════════════════════
                  OAK SHIELD SERVICE LLC
            BACKGROUND CHECK AND SCREENING POLICY
═══════════════════════════════════════════════════════════════════

Document ID:        OSS-HR-POL-002
Effective Date:     [INSERT DATE]
Revision:           1.0
Approved By:        Xinchao Xi, President
Policy Owner:       [INSERT POLICY ADMINISTRATOR NAME / TITLE]

───────────────────────────────────────────────────────────────────
1. PURPOSE
───────────────────────────────────────────────────────────────────

Oak Shield Service LLC ("Oak Shield" or "the Company") performs
work on commercial, industrial, mission-critical, and client-
controlled premises — including data centers, cold-storage
facilities, hospitality projects, retail centers, and government-
adjacent sites. Many of these clients, general contractors, and
project owners require contractor personnel to clear a documented
background screening as a condition of site access.

This Policy establishes the Company's program for conducting
employment background screening in a manner that is (a) compliant
with the federal Fair Credit Reporting Act ("FCRA"), Equal
Employment Opportunity Commission ("EEOC") guidance, and applic-
able Texas law; (b) sufficient to meet the requirements of our
clients and prequalification platforms (including ISNetworld,
Avetta, and Veriforce); and (c) protective of the safety and
property of our employees, clients, and the public.

───────────────────────────────────────────────────────────────────
2. SCOPE
───────────────────────────────────────────────────────────────────

This Policy applies to:

  (a) All applicants who have received a conditional offer of
      employment with the Company;
  (b) All current employees, where re-screening is required by
      a specific client, project owner, or applicable law;
  (c) All employees assigned to projects or client sites that
      require background-cleared personnel; and
  (d) Subcontractors and their personnel performing work on
      Oak Shield project sites, through flow-down contract
      requirements.

───────────────────────────────────────────────────────────────────
3. CONSUMER REPORTING AGENCY
───────────────────────────────────────────────────────────────────

The Company shall engage a third-party Consumer Reporting Agency
("CRA") accredited by the Professional Background Screening
Association (PBSA) — currently Sterling Talent Solutions, Inc.
or Checkr, Inc. — to perform all background screening. The CRA
shall conduct each screening in compliance with the FCRA, all
applicable state and local laws, and the CRA's own quality and
dispute-resolution standards.

───────────────────────────────────────────────────────────────────
4. STANDARD SCREENING PACKAGE
───────────────────────────────────────────────────────────────────

All applicants receiving a conditional offer of employment shall
be required to clear, at minimum, the following standard package:

  4.1  Social Security Number Trace and Address History
       (7-year address history used to direct criminal searches)

  4.2  National Criminal Database Search

  4.3  County Criminal Court Search
       (all counties of residence in the prior 7 years; jurisdic-
       tion of current residence; jurisdiction of work location)

  4.4  Federal Criminal Court Search
       (all federal districts of residence in the prior 7 years)

  4.5  National Sex Offender Registry Search

  4.6  Global Watchlist / OFAC Sanctions Search
       (including SAM.gov debarment list, where applicable)

  4.7  Employment Verification
       (prior 7 years, all employers)

  4.8  Education Verification
       (highest claimed degree or trade credential)

  4.9  Professional License Verification
       (where the position requires a license — e.g., Texas TDLR
       electrical license, EPA 608 certification, master MEP
       license, OSHA 30, CDL)

───────────────────────────────────────────────────────────────────
5. ENHANCED SCREENING (POSITION-SPECIFIC)
───────────────────────────────────────────────────────────────────

The following enhanced screening shall be required for designated
positions:

  5.1  Motor Vehicle Record (MVR)
       Required for all employees who operate Company-owned,
       leased, or rented vehicles or drive personally owned
       vehicles for Company business. Reviewed initially and
       annually thereafter.

  5.2  Drug Screening
       Required per the Drug-Free Workplace Policy (OSS-HR-POL-001).

  5.3  Client-Specific Screening
       Where a client, GC, or project owner requires additional
       screening (e.g., 10-year criminal history, federal-facility
       clearance, credit check for financial-handling roles), the
       Company will conduct the additional screening as a condi-
       tion of project assignment, with separate written
       authorization from the employee.

───────────────────────────────────────────────────────────────────
6. DISCLOSURE AND AUTHORIZATION (FCRA COMPLIANCE)
───────────────────────────────────────────────────────────────────

Before any background screening is initiated, the Company shall
provide the applicant or employee with:

  6.1  A clear and conspicuous written Disclosure, in a document
       consisting solely of the Disclosure, stating that a
       consumer report may be obtained for employment purposes
       (in compliance with FCRA § 604(b)(2)(A));

  6.2  A separate written Authorization to be signed by the
       applicant or employee, authorizing the Company and the
       CRA to procure the consumer report;

  6.3  A copy of the FTC/CFPB "Summary of Your Rights Under the
       Fair Credit Reporting Act"; and

  6.4  Where applicable, any state-specific disclosures required
       by Texas Business & Commerce Code, or by the law of the
       state in which the applicant resides.

Standalone disclosure is mandatory: The Disclosure document
shall NOT contain a release of liability, employment application
language, at-will statements, or any extraneous information that
could distract from the disclosure required by FCRA. The Author-
ization may be combined with the Disclosure where state law
permits; otherwise it shall be separate.

───────────────────────────────────────────────────────────────────
7. INDIVIDUALIZED ASSESSMENT (EEOC GUIDANCE)
───────────────────────────────────────────────────────────────────

The Company does not maintain a blanket policy of excluding
applicants based solely on the existence of a criminal record.
Where a background report returns one or more criminal records,
the Policy Administrator shall conduct an individualized assess-
ment consistent with the EEOC's 2012 Enforcement Guidance on the
Consideration of Arrest and Conviction Records, considering:

  (a) The nature and gravity of the offense or conduct;
  (b) The time that has passed since the offense, conduct, and/or
      completion of the sentence;
  (c) The nature of the position sought, including the responsi-
      bilities, level of independent work, access to client
      property, and safety-sensitive nature of the role; and
  (d) Any evidence of rehabilitation, including the applicant's
      employment history since the offense.

Arrests that did not result in a conviction shall not, standing
alone, be used as the basis for an adverse employment decision.

───────────────────────────────────────────────────────────────────
8. ADVERSE ACTION PROCESS (FCRA TWO-STEP)
───────────────────────────────────────────────────────────────────

Where the Company is considering taking adverse action (rescind-
ing a conditional offer, declining to hire, terminating, or
removing the employee from a project assignment) based in whole
or in part on a consumer report, the Company shall follow the
FCRA two-step process:

  Step 1 — Pre-Adverse Action:
       The Company shall provide the applicant or employee with:
       (a) a copy of the consumer report;
       (b) a copy of the FTC/CFPB "Summary of Your Rights"; and
       (c) a written Pre-Adverse Action Notice.

       The Company shall then wait a minimum of five (5)
       business days before taking final adverse action, to
       provide the applicant or employee a reasonable opportunity
       to dispute the accuracy or completeness of the report
       directly with the CRA.

  Step 2 — Final Adverse Action:
       If, after the waiting period, the Company decides to
       proceed with the adverse action, the Company shall provide
       a written Adverse Action Notice including: (a) the name,
       address, and phone number of the CRA; (b) a statement that
       the CRA did not make the decision and cannot provide
       reasons; (c) notice of the right to dispute and obtain a
       free copy of the report within 60 days; and (d) any
       additional disclosures required by applicable state law.

───────────────────────────────────────────────────────────────────
9. CONFIDENTIALITY AND RECORD RETENTION
───────────────────────────────────────────────────────────────────

  9.1  All consumer reports and related screening records are
       confidential and shall be maintained separately from the
       employee's general personnel file, accessible only to
       Company personnel with a legitimate business need.

  9.2  The Company shall retain background screening records for
       a minimum of five (5) years from the date of the report,
       or for the duration of the employment relationship plus
       one year, whichever is longer.

  9.3  All disposal of consumer report information shall comply
       with the FTC Disposal Rule (16 CFR Part 682), including
       secure shredding of physical records and secure deletion
       of electronic records.

───────────────────────────────────────────────────────────────────
10. RE-SCREENING
───────────────────────────────────────────────────────────────────

The Company may re-screen current employees where:

  (a) Required by a specific client, project owner, or applicable
      law;
  (b) The employee is being considered for promotion or transfer
      to a position with materially different responsibilities;
  (c) The Company has reasonable basis to believe an event has
      occurred that would have disqualified the employee under
      this Policy; or
  (d) On a periodic basis, not less frequently than every three
      (3) years, for employees assigned to safety-sensitive
      positions or restricted-access client sites.

Re-screening shall follow the same Disclosure and Authorization
process as initial screening.

───────────────────────────────────────────────────────────────────
11. SUBCONTRACTORS
───────────────────────────────────────────────────────────────────

All subcontractors performing work on Oak Shield project sites
shall maintain a background screening program substantially
equivalent to this Policy, and shall warrant that each of their
personnel assigned to the project has cleared the required
screening prior to site access. Subcontractor non-compliance may
result in immediate removal from the project site and termination
of the subcontract.

───────────────────────────────────────────────────────────────────
12. EQUAL OPPORTUNITY
───────────────────────────────────────────────────────────────────

The Company is an Equal Opportunity Employer. This Policy shall
be applied consistently and without regard to race, color,
religion, sex, national origin, age, disability, genetic infor-
mation, veteran status, or any other protected characteristic
under federal, Texas, or local law. The Company will provide
reasonable accommodation in the screening process where required
by the Americans with Disabilities Act or other applicable law.

───────────────────────────────────────────────────────────────────
13. POLICY ADMINISTRATION
───────────────────────────────────────────────────────────────────

The Policy Administrator is responsible for:

  (a) Engaging and managing the relationship with the CRA;
  (b) Ensuring all Disclosure, Authorization, Pre-Adverse Action,
      and Adverse Action documents are current and FCRA-compliant;
  (c) Conducting and documenting individualized assessments;
  (d) Maintaining records in accordance with Section 9;
  (e) Reviewing this Policy at least annually for changes in
      law, regulation, or client requirements; and
  (f) Training hiring managers on FCRA compliance.

───────────────────────────────────────────────────────────────────
14. COMPLIANCE WITH APPLICABLE LAW
───────────────────────────────────────────────────────────────────

This Policy is intended to comply with all applicable federal,
Texas, and local law, including the Fair Credit Reporting Act
(15 U.S.C. § 1681 et seq.), Title VII of the Civil Rights Act
of 1964, the Americans with Disabilities Act, the Age Discrimina-
tion in Employment Act, and applicable Texas Business & Commerce
Code provisions. In the event of any conflict between this Policy
and applicable law, applicable law shall control.

This Policy does not create an employment contract or alter the
at-will employment relationship between Oak Shield Service LLC
and its employees.

───────────────────────────────────────────────────────────────────
15. APPROVAL
───────────────────────────────────────────────────────────────────



    ________________________________            ___________________
    Xinchao Xi, President                       Date
    Oak Shield Service LLC



═══════════════════════════════════════════════════════════════════
                       END OF POLICY
═══════════════════════════════════════════════════════════════════
```

---

## 附件 A — FCRA Disclosure & Authorization Form（独立文档）

> **关键合规点**：这一份必须是 standalone document，不能跟 employment application、handbook acknowledgment、at-will agreement 等任何其他东西放在一起。Sterling / Checkr 注册后会给你他们的合规版本，建议直接用他们的 —— 下方仅作参考。

```
═══════════════════════════════════════════════════════════════════
       OAK SHIELD SERVICE LLC
       DISCLOSURE AND AUTHORIZATION REGARDING
       BACKGROUND INVESTIGATION
═══════════════════════════════════════════════════════════════════

DISCLOSURE

Oak Shield Service LLC ("the Company") may obtain information
about you from a consumer reporting agency for employment
purposes. Thus, you may be the subject of a "consumer report"
and/or an "investigative consumer report" which may include
information about your character, general reputation, personal
characteristics, and/or mode of living, and which can involve
personal interviews with sources such as your neighbors, friends,
or associates. These reports may contain information regarding
your criminal history, social security number trace, motor
vehicle records, verification of your education or employment
history, professional license verifications, and other background
information.

The consumer report will be obtained from a consumer reporting
agency, currently:

  [INSERT CRA NAME: e.g., Sterling Talent Solutions, Inc.]
  [INSERT CRA ADDRESS]
  [INSERT CRA PHONE]
  [INSERT CRA WEBSITE]

You have the right, upon written request made within a reasonable
time, to request whether a consumer report has been run about you,
and disclosure of the nature and scope of any investigative
consumer report. You will also be provided a written summary of
your rights under the Fair Credit Reporting Act.



───────────────────────────────────────────────────────────────────
AUTHORIZATION
───────────────────────────────────────────────────────────────────

I have read and understand the above Disclosure. By my signature
below, I authorize Oak Shield Service LLC, and its designated
consumer reporting agency, to procure a consumer report and/or
investigative consumer report on me for employment purposes,
including consideration for employment, project assignment, and
during the course of my employment as permitted by law.

I understand that this authorization shall remain valid through-
out my employment with Oak Shield Service LLC, to the extent
permitted by applicable law.



  ____________________________________
  Applicant / Employee Printed Name


  ____________________________________      ____________________
  Applicant / Employee Signature              Date


  Last 4 of SSN: ______________
  Date of Birth: ______________________   (for identity matching)

═══════════════════════════════════════════════════════════════════

[ATTACH: FTC/CFPB "Summary of Your Rights Under the Fair Credit
 Reporting Act" — provided separately]
```

---

## 附件 B — Pre-Adverse Action Notice 模板

```
═══════════════════════════════════════════════════════════════════
       PRE-ADVERSE ACTION NOTICE
═══════════════════════════════════════════════════════════════════

[DATE]

[Applicant / Employee Name]
[Address]

Re: Background Check Results

Dear [Name]:

Oak Shield Service LLC recently received a consumer report
prepared by [CRA Name] in connection with your application for
employment / current employment. A copy of that report is enclosed
with this notice, together with a copy of the "Summary of Your
Rights Under the Fair Credit Reporting Act."

We are considering taking adverse action against your employment
application / employment, based in whole or in part on information
contained in this report. No final decision has been made.

If you believe the report contains inaccurate or incomplete
information, you have the right to dispute it directly with [CRA
Name] at the contact information provided in the enclosed
materials. You may also provide Oak Shield Service LLC with any
information you believe is relevant to our consideration,
including information about the accuracy of the report, mitigating
circumstances, or evidence of rehabilitation.

We will wait a minimum of five (5) business days from the date of
this notice before taking any final action, to provide you a
reasonable opportunity to respond.

If you have questions, please contact:

  [POLICY ADMINISTRATOR NAME]
  [TITLE]
  [PHONE]
  [EMAIL]


Sincerely,



[Signature]
[Name]
Oak Shield Service LLC

Enclosures:
  (1) Copy of consumer report
  (2) Summary of Your Rights Under the FCRA

═══════════════════════════════════════════════════════════════════
```

---

## 附件 C — Adverse Action Notice 模板

```
═══════════════════════════════════════════════════════════════════
       ADVERSE ACTION NOTICE
═══════════════════════════════════════════════════════════════════

[DATE — must be at least 5 business days after Pre-Adverse Notice]

[Applicant / Employee Name]
[Address]

Re: Notice of Adverse Action

Dear [Name]:

This is to inform you that, after careful consideration, Oak
Shield Service LLC has decided to [rescind the conditional offer
of employment / decline to hire you / take other adverse action]
based, in whole or in part, on information contained in the
consumer report prepared by [CRA Name].

Required disclosures under the Fair Credit Reporting Act:

  1. The consumer report was prepared by:

       [CRA NAME]
       [CRA ADDRESS]
       [CRA TOLL-FREE PHONE]
       [CRA WEBSITE]

  2. [CRA Name] did not make this adverse decision and is unable
     to provide you with the specific reasons for it.

  3. You have the right to obtain, free of charge, an additional
     copy of the consumer report from [CRA Name] within sixty
     (60) days of receiving this notice.

  4. You have the right to dispute, directly with [CRA Name], the
     accuracy or completeness of any information in the report.

A copy of the "Summary of Your Rights Under the Fair Credit
Reporting Act" was previously provided to you with the Pre-Adverse
Action Notice. Another copy is enclosed for your reference.

We appreciate your interest in Oak Shield Service LLC.



Sincerely,



[Signature]
[Name]
Oak Shield Service LLC

Enclosure: Summary of Your Rights Under the FCRA

═══════════════════════════════════════════════════════════════════
```

---

## 附件 D — Individualized Assessment Worksheet（内部用）

> 候选人背调出来有犯罪记录时，**必须填这张表**才能做拒录决定。EEOC 抽查时会要看这个。

```
═══════════════════════════════════════════════════════════════════
       INDIVIDUALIZED ASSESSMENT WORKSHEET
       (EEOC 2012 Enforcement Guidance Compliance)
═══════════════════════════════════════════════════════════════════

Applicant / Employee Name: _______________________________________
Position Applied For: ____________________________________________
Date of Assessment: ______________________________________________
Assessor: _______________________________________________________

───────────────────────────────────────────────────────────────────
A. NATURE AND GRAVITY OF THE OFFENSE
───────────────────────────────────────────────────────────────────

Offense(s) of Concern (list each separately):

  1. Offense: _________________________________________________
     Conviction Date: ___________________________________________
     Felony / Misdemeanor / Other: ______________________________
     Sentence: __________________________________________________
     Sentence Completion Date: __________________________________

  2. Offense: _________________________________________________
     [repeat as needed]

Severity Assessment:
[ ] Violent offense
[ ] Property / theft offense
[ ] Drug-related offense
[ ] Financial / fraud offense
[ ] Sex-related offense
[ ] Other: __________________________________

───────────────────────────────────────────────────────────────────
B. TIME ELAPSED
───────────────────────────────────────────────────────────────────

Years since offense: __________
Years since sentence completion: __________
Employment history since offense:
_______________________________________________________________
_______________________________________________________________

───────────────────────────────────────────────────────────────────
C. NATURE OF POSITION
───────────────────────────────────────────────────────────────────

Position responsibilities (check all that apply):
[ ] Access to client premises / restricted-access sites
[ ] Driving Company or client vehicles
[ ] Handling Company or client property / cash
[ ] Independent / unsupervised work
[ ] Safety-sensitive (high-voltage, height, confined space)
[ ] Supervisory responsibilities
[ ] Customer / public-facing
[ ] Other: __________________________________

Relationship of offense to position:
[ ] Direct relationship (e.g., theft offense for cash-handling role)
[ ] Indirect / partial relationship
[ ] No clear relationship

───────────────────────────────────────────────────────────────────
D. EVIDENCE OF REHABILITATION (if provided by applicant)
───────────────────────────────────────────────────────────────────

Stable employment history:               [ ] Yes  [ ] No
Completion of treatment / counseling:    [ ] Yes  [ ] No
Education / training since offense:      [ ] Yes  [ ] No
Character references:                    [ ] Yes  [ ] No
Other mitigating factors:
_______________________________________________________________

───────────────────────────────────────────────────────────────────
E. DECISION
───────────────────────────────────────────────────────────────────

[ ] Proceed with employment / project assignment
[ ] Proceed with restrictions: ___________________________________
[ ] Do not proceed (initiate Pre-Adverse Action Notice process)

Rationale (specific facts, in assessor's own words):
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________


  ___________________________________      ___________________
  Assessor Signature                          Date

  ___________________________________      ___________________
  President / HR Lead Signature              Date

═══════════════════════════════════════════════════════════════════

[ATTACH: Copy of background report; copy of any applicant response]
[FILE: Confidential — separate from personnel file]
```

---

## 给 Ben 的部署清单

| # | 动作 | 负责人 | 工期 | 备注 |
|---|------|--------|------|------|
| 1 | 选 CRA 供应商 | Xinchao | 2天 | **建议 Checkr**（界面友好、API好、API/手动两用），Sterling 是大企业用的复杂 |
| 2 | 跟 CRA 签 service agreement + 拿合规模板 | Xinchao | 1周 | 一定要 CRA 的 Disclosure/Auth 模板，**别用我这版**（我这版是参考） |
| 3 | 用公司抬头排版 Policy 正文 | Ben | 1天 | Word 套模板 → PDF |
| 4 | Xinchao 签字 + 日期 | Xinchao | 10分钟 | 扫描存档 |
| 5 | 25 名 field 员工跑一次合规背调（基线） | Ben | 1-2周 | 一次性 $750-1,250 |
| 6 | Office 员工跑背调（5名）| Ben | 1-2周 | $150-250 |
| 7 | 司机额外加 MVR | Ben | 同上 | +$10/人 |
| 8 | 上传 Policy PDF + 抽样证据到 ISN | Ben | 30分钟 | 等 ISN 注册到此步 |
| 9 | Avetta、Veriforce 复用同一份 PDF | Ben | 按需 | — |

**预算估算**：
- Checkr "Basic+" 套餐（含 SSN trace + Nat'l Crim + County Crim + Sex offender）：~$30/人
- 加 Federal criminal：+$10/人
- 加 Employment verification：+$15/人
- 加 MVR（司机）：+$10/人
- **首次合规 30 人**：$1,350–1,650
- **新员工年化（按 8-12 入职/年）**：$400–600/年
- **MVR 年检（司机 ~10人）**：$100/年
- **首年总成本：约 $1,500–2,000；后续每年 $500–800**

---

## 关键合规雷区（千万别踩）

1. **Disclosure 不能塞东西** —— 这一行就是 FCRA 集体诉讼之王。不要在 Disclosure 文档里加 release of liability、at-will 条款、employment application 内容、handbook acknowledgment。Sterling/Checkr 的模板都是 standalone 的，**用他们的、别改**。

2. **Pre-Adverse Action 后必须等 5 个工作日** —— 不是 5 天、不是 5 自然日，是 5 个**工作日**。等不够直接被 sue。

3. **不要 blanket 拒绝任何犯罪记录** —— EEOC 2012 Guidance 强制要 individualized assessment（附件 D）。哪怕最后还是拒，必须有这张表存档。否则 EEOC 投诉时无据可辩。

4. **Arrests without conviction 不能单独作为拒录理由** —— EEOC 红线。

5. **Texas 法律相对宽松，但 Austin 不一样** —— Oak Shield 在 Richmond（Fort Bend County），不受 Austin Fair Chance Hiring Ordinance 约束。但如果未来在 Austin 接项目雇 Austin 当地人，要重新评估。

6. **不要在 application 上问 "have you ever been convicted of a crime?"** —— 虽然德州不强制 ban-the-box，但这条问题已经是 EEOC 高风险信号。等 conditional offer 后再背调，不要预先筛掉。

7. **MVR 必须年检** —— 这是保险公司要求（一般在 GL 保单条款里），不是 FCRA 要求。但如果某员工出事故时 MVR 没年检过，保险公司可以拒赔。

8. **Background check 报告必须跟 personnel file 分开存** —— FCRA + ADA 要求。建议加密 Google Drive folder + 限 Xinchao 和 Ben 访问。

9. **保存 5 年最低** —— 但实际上很多 GC 合同会要求保留更长（项目结束后 5 年 / 7 年）。建议**永久保留**电子档。

10. **不要给客户/GC 看 raw report** —— 客户/GC 只能看到"该员工已通过背调"的 attestation。原始报告里有 SSN、地址、犯罪细节，泄露就是 FCRA 违规。

---

## 跟 DFW Policy 的协同

这两份政策一起构成 ISN 入网的"人员合规"双柱：

| ISN 字段 | 用哪份文档 |
|---------|-----------|
| Substance Abuse Program | DFW Policy（OSS-HR-POL-001） |
| Pre-Employment Drug Testing | DFW Policy §4.1 |
| Random Drug Testing | DFW Policy §4.2 |
| Background Check Program | Background Check Policy（OSS-HR-POL-002） |
| Criminal History Check | Background Check Policy §4 |
| MVR Program | Background Check Policy §5.1 |
| Subcontractor Management | 两份政策的 §10 / §11 |

提交时建议合并成一个 "Personnel Compliance Package" PDF，4 个附件统一编号。

---

## 下一步建议

ISN 入网三大件已经齐了：
1. ✅ Drug-Free Workplace Policy
2. ✅ Background Check Policy
3. ⚠️ Safety Manual / Written Safety Program（**最大的剩余卡点**）

ISN A-grade 要求有完整 Written Safety Program，至少包括：HazCom、PPE、LOTO、Fall Protection、Electrical Safety、Confined Space、Hot Work、Vehicle Safety、Incident Reporting。这一份篇幅是上面两份的 10 倍以上，建议**直接买 ISN 兼容的模板**（CompliancePoint、SafetyCulture 都有卖，$500–1,500），别从零起草。

要我下一步：
- **A.** 列 Safety Manual 必备章节 + 评估自起草 vs 买模板的 ROI
- **B.** 起草 Personnel Compliance Package 提交说明书（合并两份政策的 cover letter）
- **C.** 直接进 ISN 注册流程指导（一步步操作）

选哪个？

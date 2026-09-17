# Revenue Recovery Audit Playbook

## Stage 2 — Prospect / Revenue-Leak Detector

The goal is **not** to guess that a company has a problem. The goal is to collect observable evidence of a revenue-process gap, score the opportunity consistently, and only then decide whether it deserves outreach.

## 1. Prospect record

For each company, record:

- Company and website
- Industry and approximate size
- Primary revenue motion (inbound, outbound, booked calls, ecommerce, etc.)
- Contact/booking path
- Observable response-time evidence
- Follow-up evidence
- Pipeline/CRM signals that are publicly observable
- Number of steps/friction in the conversion path
- Weak or missing calls-to-action
- Evidence URL/screenshot notes
- Decision-maker name and role (research separately; never guess)

Use `prospects.csv` as the starting schema.

## 2. Scoring

Run the observable signals through `audit_engine.py`.

- **HIGH (60–100):** enough evidence to prepare a short audit and investigate the revenue owner.
- **MEDIUM (35–59):** collect more evidence before outreach.
- **LOW (0–34):** do not prioritize yet.

The score is a prioritization mechanism, not a claim that a company is losing a particular amount of money.

## 3. Evidence standard

Every material claim should have evidence. Good evidence includes:

- A documented response-time test
- A recorded number of conversion steps
- A public page with an unclear or missing next action
- A reproducible follow-up observation
- A clearly documented workflow inconsistency

Do not invent internal CRM behavior, conversion rates, revenue figures, or customer complaints.

## 4. Outreach trigger

A prospect becomes outreach-ready when:

1. At least one meaningful revenue-process gap is observable.
2. The evidence can be explained in one or two sentences.
3. The likely buyer/owner has been identified from a reliable public source.
4. The proposed improvement is within our implementation scope.

## 5. What happens after qualification

`Prospect → Evidence → Audit → Decision-maker → Diagnostic call → Proposal → Implementation → Measurement`

The next build stage will turn qualified audit data into a repeatable audit report and outreach workflow.

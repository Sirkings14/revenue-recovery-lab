# Stage 4B — Prospect Acquisition

## Objective

Build the first verified prospect batch for Revenue Recovery Lab without buying a large data stack or inventing contact information.

## Target market

- Industry: HVAC contractors
- Geography: United States
- Initial company size: approximately 5–50 employees
- Business condition: established company with an inbound customer journey
- Problem hypothesis: leakage between inquiry, response, qualification, booking, follow-up, CRM/pipeline, or estimate conversion

## Batch target

Start with **25 companies**, not 500.

The first batch is a validation batch. Its purpose is to learn whether the audit process consistently finds specific, commercially relevant workflow problems.

## Prospect sourcing

Use public business directories, Google search results, industry directories, company websites, and other legitimate public sources.

For every company, capture at minimum:

- company
- website
- industry
- employees (only when reasonably verifiable)
- source_url
- notes

Do not guess employee count. If it cannot be verified, leave it blank.

## Website research checklist

For each prospect, inspect the customer journey as a normal prospective customer would.

Record only observations that can be supported by what you actually see or legitimately test.

### 1. Contact path

- Is there a contact form?
- Is there a phone number?
- Is there an obvious request-service/request-quote path?

### 2. Booking path

- Can a visitor book an appointment online?
- Is the booking path obvious?
- Does it require unnecessary steps or dead ends?

### 3. Offer / CTA

- Is there a clear next action?
- Is there a service-specific offer or reason to inquire?
- Is the CTA missing, stale, confusing, or difficult to find?

### 4. Response test

Only perform a response test when it is appropriate and does not create a misleading or deceptive interaction.

Record the observed response time in hours. If no legitimate test is performed, leave the field blank.

### 5. Follow-up

Only record a follow-up sequence when it is legitimately observable—for example, through a real inquiry or publicly documented workflow.

Do not manufacture leads simply to create evidence.

### 6. Pipeline / CRM signals

Look for legitimate public signals such as forms, scheduling systems, customer portals, or other visible workflow infrastructure.

Do not claim a company uses a particular CRM unless there is evidence.

### 7. Pipeline friction

Use the existing 0–3 scale:

- `0` = no material friction observed
- `1` = minor friction
- `2` = meaningful friction
- `3` = major or repeated friction

## Qualification rule

A prospect becomes **audit-ready** when all of the following are true:

1. The company fits the target market.
2. The website/customer journey has been reviewed.
3. At least one concrete workflow observation exists.
4. The observation relates to revenue operations.
5. The observation can be discussed without inventing lost-revenue numbers.
6. A plausible decision-maker can be identified from a legitimate source.

## Data integrity rules

Never:

- invent a response time
- invent a CRM
- invent a follow-up sequence
- invent employee count
- claim lost revenue without underlying business data
- fabricate a case study or result
- scrape or collect private information without authorization

The audit engine is only as good as the evidence supplied to it.

## CSV workflow

Add verified prospects to `prospects.csv`.

Then run:

```bash
python prospect_pipeline.py
```

This creates `prospect_queue.csv`, ordered by the existing revenue-leak score.

## Stage 4B success condition

Do not scale acquisition yet.

Stage 4B is complete when we have **25 real HVAC prospects with documented observations**, enough to determine whether the scoring model is producing useful sales opportunities.

Next: **Stage 4C — Decision-Maker Verification + Outreach Queue.**

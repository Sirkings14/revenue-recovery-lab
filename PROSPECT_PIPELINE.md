# Stage 4 — Prospect Acquisition Engine

## Objective

Create a repeatable queue of companies that may have a revenue-process problem worth investigating.

The engine does **not** pretend to discover private information automatically. The operator records a company and its public/source evidence, then the scoring engine prioritizes the research queue.

## Operating loop

**1. Target → 2. Capture → 3. Research → 4. Score → 5. Verify decision-maker → 6. Generate audit → 7. Outreach**

### 1. Target

Start with one narrow market segment where a lead-response or follow-up problem can plausibly have meaningful commercial impact. Avoid trying to target every industry at once.

### 2. Capture

Add prospects to `prospects.csv`. Minimum useful fields:

- company
- website
- industry
- source_url
- notes

Add a decision-maker only when it has been verified from an appropriate source.

### 3. Research

Inspect the public customer journey and record observable signals:

- Contact path
- Booking path
- Response time, when legitimately testable
- Follow-up behavior, when legitimately observable
- CTA clarity
- Pipeline friction
- Relevant CRM/workflow signals

### 4. Score

Run:

```bash
python prospect_pipeline.py
```

The output is `prospect_queue.csv`, sorted by audit score.

### 5. Verify decision-maker

For high-priority prospects, identify the person responsible for sales, revenue operations, growth, customer acquisition, or a closely related function. Record the source used to verify the role.

### 6. Generate the audit

Only use documented observations. The audit generator should distinguish observed facts from reported information and hypotheses.

### 7. Outreach

Contact only after the evidence is strong enough to make the message genuinely specific. Follow applicable email, privacy, anti-spam, and platform rules. Keep outreach relevant, transparent and easy to opt out of.

## Definition of a qualified prospect

A prospect becomes **sales-ready** when:

- There is a concrete, documented workflow observation.
- The observation is relevant to revenue operations.
- A plausible owner of the workflow has been identified.
- The issue is specific enough to discuss without inventing financial loss.
- The audit contains a clear next step.

## Business model connection

The acquisition engine is not the product. It is the top of the commercial system:

**Qualified problem → paid diagnostic/implementation conversation → scoped workflow implementation → measurement → ongoing optimization.**

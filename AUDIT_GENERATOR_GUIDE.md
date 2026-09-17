# Stage 3 — Audit Generator Guide

## Purpose

The audit generator converts prospect-scoring output and verified observations into a concise document suitable for a discovery conversation or pre-call email.

## Workflow

1. Run the prospect through `audit_engine.py`.
2. Keep only observations you can verify.
3. Convert each observation into an `AuditEvidence` item:
   - `finding`: what was observed
   - `evidence`: what proves or supports it
   - `impact`: the operational consequence to investigate
   - `confidence`: Observed, Reported, or Hypothesis
4. Call `generate_audit(result, evidence)`.
5. Review the Markdown manually before sending it.
6. Never state that a company is losing a specific amount of money unless the client supplies the underlying numbers.

## Example evidence

```python
AuditEvidence(
    finding="Follow-up sequence",
    evidence="No structured follow-up was observed after an inquiry.",
    impact="Potential inconsistency in lead nurturing.",
    confidence="Observed",
)
```

## Sales use

The audit is not the sales pitch. Its job is to demonstrate that you investigated a specific workflow and found concrete questions worth discussing.

The conversation should move from:

**Observation → business context → baseline data → implementation scope → measurement**

Avoid generic AI claims, fabricated ROI, fake urgency, and unsupported revenue-loss estimates.

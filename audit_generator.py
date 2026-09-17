"""Revenue Recovery Lab — Evidence-led Audit Generator.

Turns a scored prospect plus observed evidence into a client-ready Markdown audit.
It does not invent metrics, clients, results, or revenue figures.
"""

from dataclasses import dataclass
from datetime import date
from typing import List

from audit_engine import AuditResult


@dataclass
class AuditEvidence:
    finding: str
    evidence: str
    impact: str
    confidence: str = "Observed"


def generate_audit(result: AuditResult, evidence: List[AuditEvidence], auditor="Revenue Recovery Lab") -> str:
    """Return a concise, evidence-led audit document in Markdown."""
    findings = "\n".join(
        f"### {i}. {item.finding}\n\n- **Evidence:** {item.evidence}\n- **Revenue-process impact:** {item.impact}\n- **Confidence:** {item.confidence}\n"
        for i, item in enumerate(evidence, 1)
    ) or "No findings have been documented yet. Collect evidence before sending this audit."

    actions = []
    if any("follow" in x.finding.lower() for x in evidence):
        actions.append("Map the first 7–14 days of lead follow-up and define ownership, timing and escalation rules.")
    if any("response" in x.finding.lower() for x in evidence):
        actions.append("Measure response time across a small sample and establish a target response workflow.")
    if any("booking" in x.finding.lower() or "cta" in x.finding.lower() for x in evidence):
        actions.append("Reduce friction between intent and the next conversion action, then track completion rate.")
    if any("pipeline" in x.finding.lower() or "crm" in x.finding.lower() for x in evidence):
        actions.append("Document pipeline stages, ownership and stale-lead rules before automating handoffs.")
    if not actions:
        actions.append("Run a short workflow mapping session to identify the highest-confidence operational leak.")

    action_text = "\n".join(f"{i}. {action}" for i, action in enumerate(dict.fromkeys(actions), 1))

    return f"""# Revenue Workflow Audit

**Prepared for:** {result.company}  
**Prepared by:** {auditor}  
**Date:** {date.today().isoformat()}  
**Opportunity score:** {result.score}/100  
**Priority:** {result.tier}

## Executive summary

This audit identifies observable gaps in the path from customer intent to qualification, follow-up, pipeline progression and conversion. It is a diagnostic document, not a claim about lost revenue. Any financial impact should be calculated only after the relevant baseline data is available.

## Observed findings

{findings}

## Recommended first actions

{action_text}

## Measurement plan

Before implementation, establish a baseline for the affected workflow. Depending on the problem, useful measures can include:

- First-response time
- Contact-to-conversation rate
- Lead-to-qualified-opportunity rate
- Booking completion rate
- Follow-up completion rate
- Stale-lead rate
- Pipeline stage conversion

## Proposed next step

Review the findings with the person responsible for revenue operations, sales, or customer acquisition. If the evidence is confirmed, scope a focused workflow implementation around the highest-impact gap.

## Evidence standard

This report contains only documented observations supplied to the generator. Unknowns remain unknowns. No customer results, revenue figures, testimonials, or performance guarantees should be added without evidence.
"""


def save_audit(result: AuditResult, evidence: List[AuditEvidence], path: str) -> None:
    """Write an audit to a Markdown file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(generate_audit(result, evidence))


if __name__ == "__main__":
    from audit_engine import ProspectSignals, score_prospect

    prospect = ProspectSignals(
        company="Example Company",
        website="https://example.com",
        industry="B2B services",
        has_contact_form=True,
        has_booking_flow=True,
        response_time_hours=8,
        follow_up_sequence_visible=False,
        stale_or_missing_cta=True,
    )
    result = score_prospect(prospect)
    evidence = [
        AuditEvidence("Follow-up sequence", "No structured sequence was observed after the initial inquiry.", "Potential inconsistency in lead nurturing."),
        AuditEvidence("Response time", "Test inquiry response measured at 8 hours.", "Delayed first response can create avoidable handoff friction; confirm with a larger sample."),
    ]
    print(generate_audit(result, evidence))

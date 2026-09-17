"""Revenue Recovery Lab — Revenue Leak Detector

Offline-first scoring engine for prospect audits.
No scraping, outreach, or CRM writes happen here. It turns observable
revenue-process signals into a repeatable audit score.
"""

from dataclasses import dataclass, asdict
from typing import Dict, List, Tuple


@dataclass
class ProspectSignals:
    company: str
    website: str = ""
    industry: str = ""
    employees: int = 0
    has_contact_form: bool = False
    has_booking_flow: bool = False
    has_crm_visible: bool = False
    response_time_hours: float = 0
    follow_up_sequence_visible: bool = False
    lead_magnet_or_offer: bool = False
    pipeline_friction: int = 0  # 0–3, based on observed steps/friction
    stale_or_missing_cta: bool = False


@dataclass
class AuditResult:
    company: str
    score: int
    tier: str
    signals: Dict[str, int]
    evidence_to_collect: List[str]
    recommended_next_step: str


def score_prospect(p: ProspectSignals) -> AuditResult:
    """Score observable signals; higher means a stronger audit opportunity."""
    points: Dict[str, int] = {}
    evidence: List[str] = []

    points["contact_path"] = 8 if p.has_contact_form else 0
    points["booking_path"] = 10 if p.has_booking_flow else 0
    points["crm_signal"] = 8 if p.has_crm_visible else 0
    points["slow_response"] = min(20, round(p.response_time_hours * 2)) if p.response_time_hours > 0 else 0
    points["follow_up_gap"] = 15 if not p.follow_up_sequence_visible else 0
    points["offer_gap"] = 10 if not p.lead_magnet_or_offer else 0
    points["pipeline_friction"] = max(0, min(15, p.pipeline_friction * 5))
    points["cta_gap"] = 14 if p.stale_or_missing_cta else 0

    if points["slow_response"]:
        evidence.append("Document response-time evidence with a test inquiry or published SLA.")
    if points["follow_up_gap"]:
        evidence.append("Check whether an inquiry receives structured follow-up after the first response.")
    if points["pipeline_friction"]:
        evidence.append("Record the number of steps from first intent to booking/contact completion.")
    if points["cta_gap"]:
        evidence.append("Capture the relevant page where the next action is unclear or weak.")

    score = min(100, sum(points.values()))
    if score >= 60:
        tier = "HIGH"
        next_step = "Prepare a short evidence-led Revenue Workflow Audit and contact the revenue owner."
    elif score >= 35:
        tier = "MEDIUM"
        next_step = "Collect one or two more pieces of evidence before outreach."
    else:
        tier = "LOW"
        next_step = "Keep in the prospect pool; do not prioritize until a stronger revenue leak is observable."

    return AuditResult(
        company=p.company,
        score=score,
        tier=tier,
        signals=points,
        evidence_to_collect=evidence,
        recommended_next_step=next_step,
    )


def audit_row(row: Dict) -> Dict:
    """Accept a dictionary (e.g. CSV/CRM row) and return JSON-friendly output."""
    result = score_prospect(ProspectSignals(**row))
    return asdict(result)


if __name__ == "__main__":
    demo = ProspectSignals(
        company="Example Company",
        website="https://example.com",
        industry="B2B services",
        employees=25,
        has_contact_form=True,
        has_booking_flow=True,
        response_time_hours=14,
        follow_up_sequence_visible=False,
        lead_magnet_or_offer=False,
        pipeline_friction=2,
        stale_or_missing_cta=True,
    )
    print(score_prospect(demo))

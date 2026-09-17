"""Revenue Recovery Lab — Prospect Acquisition & Prioritization Pipeline.

Stage 4 turns a raw prospect list into an ordered research queue. It deliberately
keeps company research separate from scoring: evidence must be supplied by the
operator or a permitted data source before a prospect can be prioritized.
"""

import csv
from dataclasses import dataclass, asdict
from typing import List

from audit_engine import ProspectSignals, score_prospect


@dataclass
class Prospect:
    company: str
    website: str = ""
    industry: str = ""
    decision_maker: str = ""
    decision_maker_title: str = ""
    source_url: str = ""
    notes: str = ""
    has_contact_form: bool = False
    has_booking_flow: bool = False
    has_crm_visible: bool = False
    response_time_hours: float = 0
    follow_up_sequence_visible: bool = False
    lead_magnet_or_offer: bool = False
    pipeline_friction: int = 0
    stale_or_missing_cta: bool = False


def prioritize(prospects: List[Prospect]) -> List[dict]:
    """Score prospects and return a research/outreach queue, highest score first."""
    queue = []
    for p in prospects:
        result = score_prospect(ProspectSignals(**{
            k: getattr(p, k) for k in ProspectSignals.__dataclass_fields__
        }))
        row = asdict(p)
        row.update({
            "score": result.score,
            "tier": result.tier,
            "recommended_next_step": result.recommended_next_step,
        })
        queue.append(row)
    return sorted(queue, key=lambda x: x["score"], reverse=True)


def read_csv(path: str) -> List[Prospect]:
    """Load the prospect intake CSV."""
    with open(path, newline="", encoding="utf-8") as f:
        return [Prospect(**row) for row in csv.DictReader(f)]


def write_queue(path: str, queue: List[dict]) -> None:
    """Write the prioritized research queue."""
    if not queue:
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(queue[0].keys()))
        writer.writeheader()
        writer.writerows(queue)


if __name__ == "__main__":
    queue = prioritize(read_csv("prospects.csv"))
    write_queue("prospect_queue.csv", queue)
    print(f"Prioritized {len(queue)} prospects → prospect_queue.csv")

"""Stage 4E: generate a fact-based Revenue Recovery Lab proposal.

The generator deliberately requires verified inputs. It does not estimate
lost revenue or promise ROI.
"""

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import List


@dataclass
class ProposalInput:
    client_company: str
    decision_maker: str
    problem: str
    current_workflow: str
    proposed_workflow: str
    systems: List[str]
    automation_actions: List[str]
    human_approval_points: List[str]
    baseline_metrics: List[str]
    target_metrics: List[str]
    timeline: str
    client_responsibilities: List[str]
    implementation_fee: str
    payment_schedule: str
    assumptions: List[str] = field(default_factory=list)
    exclusions: List[str] = field(default_factory=list)
    optional_optimization: str = "Optional monthly optimization can be scoped after the first implementation and baseline review."


def bullets(items: List[str]) -> str:
    if not items:
        return "- None specified"
    return "\n".join(f"- {item}" for item in items)


def generate_proposal(data: ProposalInput, prepared_by: str = "Revenue Recovery Lab") -> str:
    """Return a client-ready Markdown proposal from verified diagnostic inputs."""

    return f"""# Revenue Recovery Implementation Proposal

**Prepared for:** {data.client_company}  
**Decision maker:** {data.decision_maker}  
**Prepared by:** {prepared_by}  
**Date:** {date.today().isoformat()}

## 1. Executive summary

Based on the diagnostic discussion, the first workflow to address is:

**{data.problem}**

The objective is to make the workflow more consistent, reduce avoidable manual work, and create a measurable process for the agreed outcome. This proposal does not assume a specific revenue increase; performance will be evaluated against the baseline metrics below.

## 2. Current-state finding

{data.current_workflow}

## 3. Proposed workflow

{data.proposed_workflow}

## 4. Systems and integrations

{bullets(data.systems)}

## 5. Automation actions

{bullets(data.automation_actions)}

## 6. Human approval points

{bullets(data.human_approval_points)}

## 7. Measurement plan

### Baseline

{bullets(data.baseline_metrics)}

### Target measurements

{bullets(data.target_metrics)}

Targets should be agreed from the client's actual baseline. No performance guarantee is implied by this proposal.

## 8. Implementation timeline

{data.timeline}

## 9. Client responsibilities

{bullets(data.client_responsibilities)}

## 10. Investment

**Implementation fee:** {data.implementation_fee}

**Payment schedule:** {data.payment_schedule}

**Optional optimization:** {data.optional_optimization}

## 11. Assumptions

{bullets(data.assumptions)}

## 12. Exclusions

{bullets(data.exclusions)}

## 13. Next step

If this scope matches the workflow you want fixed, the next step is to confirm the scope, payment schedule, required access, and implementation start date.

---

**Revenue Recovery Lab**  
Recover more revenue from the customers you're already reaching.
"""


def save_proposal(data: ProposalInput, path: str = "proposal.md") -> None:
    Path(path).write_text(generate_proposal(data), encoding="utf-8")


if __name__ == "__main__":
    demo = ProposalInput(
        client_company="Example HVAC Company",
        decision_maker="Owner",
        problem="Unsold estimates are not consistently assigned a next follow-up action.",
        current_workflow="The diagnostic found that open estimates can remain without a clearly visible next action.",
        proposed_workflow="Detect qualifying open estimates, assign ownership, run the agreed follow-up sequence, capture the outcome, and update the pipeline.",
        systems=["Existing CRM / field-service platform"],
        automation_actions=["Detect qualifying open estimates", "Create follow-up task", "Send approved reminder", "Record outcome"],
        human_approval_points=["Review escalation rules before launch", "Approve customer-facing message templates"],
        baseline_metrics=["Open estimates older than the agreed threshold", "Current estimate-to-sale rate if available"],
        target_metrics=["Follow-up completion rate", "Stale-estimate count", "Estimate-to-sale conversion"],
        timeline="Initial workflow build and testing: 1–2 weeks after access and scope confirmation.",
        client_responsibilities=["Provide system access or exports", "Approve message templates", "Nominate a workflow owner", "Provide baseline data"],
        implementation_fee="$2,000",
        payment_schedule="50% to start; 50% at implementation handoff.",
        assumptions=["Required system access and documentation are available.", "Customer-facing messaging will be approved by the client."],
        exclusions=["CRM replacement", "Paid advertising", "Unapproved customer outreach", "Guaranteed revenue results"],
    )
    print(generate_proposal(demo))

# Stage 4E — Sales Diagnostic System

## Purpose

Turn a qualified prospect conversation into a fact-based implementation scope.

The diagnostic is **not a generic sales call** and is not designed to pressure a prospect into buying. Its job is to determine whether a measurable revenue-workflow problem exists, whether the company can provide enough access/data to fix it, and whether the problem is worth solving now.

Industry context: current HVAC sales guidance emphasizes systematic handling of leads, estimates, CRM stages, and follow-up. ServiceTitan's 2026 material specifically describes follow-up on unsold estimates and CRM pipeline stages as operational parts of the sales process. Treat those sources as industry guidance, not proof that any individual prospect has a problem. 

## Diagnostic outcome

Every call should end in exactly one of these states:

- `IMPLEMENTATION_READY` — verified problem, accessible system/data, clear owner, measurable baseline, agreed scope.
- `DIAGNOSTIC_REQUIRED` — problem appears real, but baseline data or workflow access is missing.
- `NURTURE` — relevant company, but timing or priority is not right.
- `NO_FIT` — problem is outside our scope or there is no sufficiently material workflow issue.

Never manufacture urgency or financial loss.

---

## 1. Opening

Use a short permission-based opening:

> "Thanks for taking the time. I looked at the customer journey before reaching out. I'd like to understand how inquiries and estimates move through your team, where follow-up is owned, and what happens when something stalls. If there is a real gap we can measure and fix, I'll outline it. If not, I'll tell you that too. Sound good?"

The objective is diagnosis, not pitching.

---

## 2. Core diagnostic questions

### A. Lead volume and sources

1. Where do most new HVAC inquiries come from today?
2. Roughly how many new inquiries do you receive in a normal week or month?
3. Which sources produce the highest-value opportunities?
4. Are calls, web forms, chat, paid leads, referrals, and repeat customers tracked separately?

**Capture:** source, approximate volume, tracking method.

### B. First response

5. What happens immediately after a new inquiry arrives?
6. Who owns the first response?
7. What is the normal response time during business hours? After hours?
8. What happens if nobody answers or responds?
9. Is first-response time visible in the CRM or reporting system?

**Capture:** owner, response process, response-time baseline, escalation path.

### C. Qualification and booking

10. What makes a lead qualified enough to schedule?
11. Is qualification handled by a CSR, salesperson, technician, owner, or automation?
12. How are unbooked inquiries followed up?
13. What percentage of inquiries become appointments, if you track it?
14. Where can a lead disappear between inquiry and booked appointment?

**Capture:** qualification rules, booking workflow, handoff points, unbooked-lead process.

### D. Estimate / proposal follow-up

15. After an estimate is sent, who owns the follow-up?
16. What is the standard follow-up sequence?
17. How many attempts are normally made before an opportunity is considered lost?
18. Are open estimates automatically surfaced to the team?
19. What happens to estimates that receive no response?
20. Do you know your estimate-to-sale conversion rate?

**Capture:** sequence, ownership, number of attempts, automation, baseline conversion if available.

### E. CRM / systems

21. What system is the source of truth for leads and opportunities?
22. Which tools receive or create new leads?
23. Where do staff still use spreadsheets, inboxes, sticky notes, or manual reminders?
24. Which parts of the workflow are automated today?
25. Which automations are unreliable or frequently bypassed?

**Capture:** CRM/field-service platform, integrations, manual work, automation gaps.

### F. Stale opportunities

26. How do you identify leads or estimates that have gone quiet?
27. How quickly does someone notice a stale opportunity?
28. Is there a defined owner for every open opportunity?
29. Can management see the number/value of opportunities sitting without a next action?
30. What normally causes an opportunity to be marked lost?

**Capture:** stale definition, reporting, ownership, lost reasons.

### G. Business impact

31. Which part of the process do you believe costs the team the most opportunities?
32. If you could fix one workflow this quarter, which one would it be?
33. What metric would prove that the change worked?
34. What is the approximate value of a typical sold opportunity in that segment?
35. How much operational time does the current process consume?

**Important:** ask for numbers; do not supply numbers yourself.

---

## 3. Qualification gates

A prospect should not move to implementation simply because they like the idea.

### Gate 1 — Problem

At least one concrete workflow failure is verified.

Examples:
- leads are not consistently followed up;
- estimates remain open without an owner or next action;
- response-time visibility is missing;
- qualification/booking handoffs are inconsistent;
- CRM stages do not reflect actual workflow;
- manual reminders are used for a process that could be automated.

### Gate 2 — Ownership

A person responsible for the affected process is identified.

### Gate 3 — Access

The prospect can provide the necessary workflow information, reports, CRM access, exports, screenshots, or supervised access needed to design the fix.

### Gate 4 — Measurement

At least one baseline metric can be established.

Preferred metrics:
- first-response time;
- inquiry-to-contact rate;
- inquiry-to-booking rate;
- booking show rate;
- estimate-to-sale rate;
- stale-opportunity count;
- follow-up completion rate;
- days-to-close;
- lost-reason distribution.

### Gate 5 — Economic relevance

The prospect confirms that the problem matters commercially or consumes meaningful operational time.

Do **not** claim a dollar loss unless the prospect's data supports it.

### Gate 6 — Timing

There is a realistic implementation window and a person available to participate.

---

## 4. Diagnostic scorecard

Score each category 0–2:

| Category | 0 | 1 | 2 |
|---|---|---|---|
| Problem clarity | unclear | suspected | verified |
| Revenue relevance | weak | plausible | directly relevant |
| Data availability | none | partial | usable baseline |
| System access | unavailable | uncertain | available |
| Ownership | unclear | identified | committed owner |
| Timing | no timing | later | active project |
| Automation opportunity | low | moderate | clear repeatable workflow |
| Measurement | unavailable | possible | defined baseline + target metric |

**Interpretation:**

- `13–16`: implementation-ready candidate
- `9–12`: diagnostic / scope clarification required
- `0–8`: nurture or no-fit depending on the conversation

This score is an internal qualification aid, **not a quality rating of the customer**.

---

## 5. Baseline data request

If the prospect is interested, request only what is needed for the proposed workflow.

Possible inputs:

- last 30–90 days of lead volume;
- lead source breakdown;
- response-time report;
- appointment/booking numbers;
- open and closed estimates;
- estimate-to-sale conversion;
- stale opportunity list;
- lost reasons;
- current follow-up sequence;
- CRM pipeline stages;
- screenshots or workflow diagrams;
- automation/integration list.

For sensitive data, request the smallest practical dataset and allow redaction/anonymization where possible.

---

## 6. Scope the first implementation

Do not sell a giant transformation.

Choose one revenue workflow with:

1. clear trigger;
2. clear owner;
3. repeatable actions;
4. measurable outcome;
5. defined systems;
6. manageable implementation boundary.

Example first scopes:

### Scope A — Lead response recovery
Trigger: new inbound lead.

Workflow:
- capture;
- immediate acknowledgement;
- qualification;
- booking attempt;
- escalation if unanswered;
- CRM logging;
- reporting.

### Scope B — Unsold estimate recovery
Trigger: estimate remains open/no response.

Workflow:
- identify stale estimate;
- assign owner;
- timed follow-up sequence;
- stop conditions;
- response capture;
- CRM stage update;
- manager visibility.

### Scope C — Pipeline hygiene
Trigger: opportunity has no next action or stale stage.

Workflow:
- detect stale opportunity;
- notify owner;
- create next action;
- escalate after threshold;
- record outcome;
- management dashboard.

---

## 7. Proposal handoff

Once the diagnostic passes the qualification gates, capture:

- client/company;
- decision maker;
- verified problem;
- current workflow;
- proposed workflow;
- systems involved;
- integrations;
- automation actions;
- human approval points;
- baseline metrics;
- target measurement window;
- implementation timeline;
- client responsibilities;
- implementation fee;
- optional monthly optimization;
- assumptions;
- exclusions;
- payment schedule.

Then generate the proposal from `proposal_engine.py`.

---

## 8. Pricing logic

Pricing is based on **scope and implementation complexity**, not a made-up percentage of revenue recovered.

Use three internal bands as starting points only:

- **Focused workflow:** $1,500–$2,500
- **Multi-workflow implementation:** $2,500–$5,000
- **Complex revenue-ops build:** $5,000+

Adjust after validating actual scope, systems, integrations, data quality, custom logic, and support requirements.

Do not promise that an implementation will produce a specific revenue increase.

A performance component can be considered later only when measurement, attribution, access, legal terms, and payment mechanics are clear.

---

## 9. Proposal structure

Every proposal should contain:

1. Executive summary
2. Current-state findings
3. Business impact to be measured
4. Proposed workflow
5. Systems and integrations
6. Automation + human approval points
7. Measurement plan
8. Implementation timeline
9. Client responsibilities
10. Investment
11. Payment schedule
12. Assumptions and exclusions
13. Acceptance / next step

The proposal should make the implementation concrete enough that the buyer understands what they are purchasing.

---

## 10. Sales transition language

Use:

> "Based on what you've shown me, I don't think the right move is to sell you a generic automation package. The specific workflow I'd address first is [workflow]. The current process is [verified observation]. I'd change it to [proposed workflow], connect it to [systems], and measure [metrics]. If that scope matches what you want fixed, I'll put the implementation plan and fee into a short proposal."

Then stop talking and let the prospect respond.

---

## 11. Integrity rules

Never:

- invent lost revenue;
- invent conversion rates;
- claim a guaranteed ROI;
- claim a prospect uses a CRM without evidence;
- imply a workflow failure that was not verified;
- fabricate testimonials or case studies;
- pressure a prospect after a clear no;
- hide implementation dependencies.

The system wins by making the business case **measurable and specific**, not by exaggerating the pain.

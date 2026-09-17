# Stage 5 — Real-Market Acquisition

## Objective

Move Revenue Recovery Lab from infrastructure into verified market activity.

Initial target:
- Industry: HVAC
- Market: United States
- Company size hypothesis: approximately 5–50 employees
- Buyer: owner, president, GM, sales leader, operations/customer-acquisition leader
- Batch size: 25 companies

## What counts as a qualified prospect

A prospect is not qualified merely because it is an HVAC company.

Minimum evidence:
1. Real operating HVAC company.
2. Public website or legitimate public business profile.
3. Inbound customer journey can be inspected.
4. At least one concrete revenue-workflow observation is documented.
5. A plausible decision maker can be identified from a legitimate public source.
6. The observation is relevant to inquiry handling, qualification, follow-up, booking, estimates, pipeline management, or conversion.
7. No unsupported claim about lost revenue is made.

## Research checklist

For every company inspect, where legitimately observable:

### 1. Lead entry
- Phone number visible?
- Contact form?
- Quote/request form?
- Chat?
- Emergency-service CTA?

### 2. Booking
- Online booking?
- Scheduling request?
- Clear next step after inquiry?
- Friction or unnecessary steps?

### 3. Offer / CTA
- Clear service CTA?
- Financing/maintenance/replacement offer?
- Estimate request?
- CTA prominent on key pages?

### 4. Follow-up hypothesis
Do not claim an internal follow-up sequence unless it is legitimately observable.

Instead record:
- what happens after an inquiry when legitimately testable;
- what cannot be verified;
- what process question should be asked during the diagnostic.

### 5. Pipeline hypothesis
Look for publicly visible signals such as:
- multiple inquiry channels with no obvious next step;
- estimate request without visible scheduling path;
- fragmented calls/forms/chat paths;
- unclear handoff from inquiry to appointment.

Do not claim a CRM is being used unless there is evidence.

## Prospect record

Required fields:

```text
company
website
industry
employees
source_url
notes
has_contact_form
has_booking_flow
has_crm_visible
response_time_hours
follow_up_sequence_visible
lead_magnet_or_offer
pipeline_friction
stale_or_missing_cta
decision_maker
decision_maker_title
decision_maker_source_url
specific_observation
observation_source_url
outreach_status
```

## Observation standard

Use:
- "I observed..."
- "The public customer journey shows..."
- "I could not verify..."
- "This may create a follow-up gap..."
- "I would want to measure..."

Never use:
- "You are losing $X" without client data.
- "Your leads are being ignored" without evidence.
- fabricated response times.
- fabricated employee counts.
- fabricated CRM usage.
- fabricated case studies or results.

## Batch workflow

### Phase A — Build 25

Research 25 real HVAC companies and complete the evidence fields.

### Phase B — Score

Run:

```bash
python prospect_pipeline.py
```

Review the resulting `prospect_queue.csv` manually.

### Phase C — Verify decision makers

For each high-priority prospect, verify the person responsible for revenue/customer acquisition/operations.

### Phase D — Outreach

Prepare one personalized first-touch message using `OUTREACH_PLAYBOOK.md`.

The message should reference exactly one concrete observation.

### Phase E — Diagnose

Interested replies move into the Stage 4E diagnostic.

## Daily operating target

Start with quality rather than volume:

- 5 researched companies/day
- 5 documented observations/day
- 5 decision-maker verification attempts/day
- 5 personalized messages/day

At 5/day, the first 25-company batch is a five-working-day validation cycle.

## Success criteria

Stage 5 succeeds when we have:

- 25 real HVAC prospects;
- 25 evidence-backed workflow observations;
- verified decision-maker information for the strongest prospects;
- personalized outreach ready/sent;
- response classifications recorded;
- at least one real diagnostic conversation to use for refining the offer.

The objective is learning and revenue validation, not producing an impressive spreadsheet.

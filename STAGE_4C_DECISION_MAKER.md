# Stage 4C — Decision-Maker Verification + Outreach Queue

## Objective

Convert qualified HVAC companies into a verified, human-reviewed outreach queue.

The goal is not to collect as many contacts as possible. The goal is to identify the person who can discuss the revenue workflow problem and document why that person is relevant.

## Priority roles

Use this order as a practical starting point:

1. Owner / Founder / President
2. General Manager
3. Sales Manager / Sales Director
4. Operations Manager / Service Manager
5. Revenue / Growth / Marketing leader, when the role clearly owns the relevant workflow

For small HVAC companies, the owner or general manager is often the most relevant starting point.

## Verification standard

A decision maker is considered verified when:

- the person's name is found from a legitimate public or permitted source;
- the role is current enough to reasonably rely on;
- the role has a clear relationship to sales, operations, customer acquisition, or revenue workflow;
- the source is recorded in `role_source`.

Do not guess a person's title from a generic email address.

## Contact data

Use legitimate business contact information and respect applicable laws, platform rules, and company preferences.

Do not collect or expose private personal information merely because it can be found online.

## Outreach queue fields

`decision_maker_queue.csv` contains:

- company
- website
- decision_maker
- decision_maker_title
- source_url
- role_source
- contact_channel
- problem_summary
- audit_score
- tier
- outreach_status
- notes

## Outreach status values

Use one of:

- `researching`
- `verified`
- `ready`
- `contacted`
- `replied`
- `meeting_booked`
- `not_now`
- `not_a_fit`
- `do_not_contact`

## Problem summary rule

The summary must describe an observed workflow issue, not an invented financial loss.

Good:

> Website accepts quote requests but the path to an online appointment is unclear; follow-up process has not been verified.

Bad:

> You are losing $20,000/month from missed leads.

The second statement requires company-specific financial evidence that we do not have.

## Outreach sequence

1. Research the company.
2. Document one specific observation.
3. Verify the relevant decision maker.
4. Prepare a short, personalized message tied to the observation.
5. Ask for a short conversation or permission to send the audit.
6. Record the outcome.
7. If there is no response, follow the defined follow-up policy rather than sending unlimited messages.

## Qualification gate

Only move a prospect to `ready` when:

- the company fits the HVAC ICP;
- a concrete workflow observation exists;
- the observation is evidence-based;
- the relevant decision maker is verified;
- the reason for contact is specific;
- no unsupported revenue-loss claim is being made.

## Stage 4C success condition

Create an initial queue of **10 verified decision makers** from the strongest qualified prospects in the first 25-company research batch.

Then move to **Stage 4D — Outreach System**, where messaging, follow-up tracking, response handling, and meeting conversion are operationalized.

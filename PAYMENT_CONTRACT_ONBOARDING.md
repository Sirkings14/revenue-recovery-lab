# Stage 4F — Payment, Contract & Client Onboarding Engine

## Objective

Turn an accepted proposal into a clean, documented, paid client engagement without relying on informal promises.

The operating sequence is:

**Proposal accepted → agreement signed → invoice/payment request → payment received → onboarding → implementation kickoff**

## 1. Payment architecture

### Primary collection route for initial validation

Use a business payment method that is actually available to the operator and approved for the account's country/region.

For Payoneer users, the current platform documentation says businesses can request payments from international clients and can use payment requests, payment links, receiving accounts and other supported methods. Availability and eligibility vary by country and account. Verify the exact options shown inside the account before presenting them to a client.

Do not claim to be located in another country or use another person's financial account to bypass eligibility requirements.

### Client-facing payment rule

The client should receive:

- Company/service name
- Exact project scope
- Total project fee
- Deposit/payment schedule
- Currency
- Due date
- Payment method/link or bank instructions
- What starts work
- Refund/cancellation terms where applicable

For a first implementation, a practical commercial structure is:

- **50% to schedule and begin implementation**
- **50% at agreed implementation milestone / handoff**

Alternative terms can be used when the client or project requires them. Never promise a payment schedule before agreeing it with the client.

## 2. Contract minimums

Every paid implementation should document:

1. Parties
2. Scope of work
3. Deliverables
4. Client responsibilities
5. Systems/access required
6. Timeline and milestones
7. Fees and payment schedule
8. Change-request process
9. Acceptance/handoff criteria
10. Confidentiality/data handling
11. Third-party software costs
12. Cancellation/termination terms
13. Limitation of liability where appropriate
14. Ownership/licensing of deliverables
15. Communication and support expectations

This document is an operating checklist, not legal advice. Use a locally appropriate contract and obtain professional legal review when the engagement warrants it.

## 3. Scope protection

The proposal must define the workflow being changed.

Example:

> Implement and configure a lead follow-up workflow covering new inbound inquiries, qualification, follow-up tasks, booking handoff, CRM status updates and reporting for the agreed systems.

Avoid vague promises such as:

> We will increase your revenue by 30%.

Revenue outcomes depend on the client's lead volume, sales process, pricing, staff execution and other factors. The engagement should commit to implementation work and measurement, not invented guarantees.

## 4. Payment gate

No implementation work begins until all required kickoff conditions are satisfied.

### Gate A — Commercial acceptance

- Proposal accepted
- Scope confirmed
- Price confirmed
- Payment terms confirmed

### Gate B — Agreement

- Contract signed by required parties

### Gate C — Payment

- Required deposit received
- Payment record stored
- Receipt/invoice status updated

### Gate D — Access

- Client contact confirmed
- Required CRM/software access granted
- Relevant workflow documentation/data supplied
- Technical constraints documented

### Gate E — Kickoff

Only after A–D should the implementation move to active status.

## 5. Client onboarding form

Collect:

### Business
- Company name
- Primary contact
- Role
- Time zone
- Main business goal

### Revenue workflow
- Main lead sources
- Approximate monthly inbound inquiry volume
- Current response process
- Current qualification process
- Current booking/estimate process
- Current follow-up process
- Current CRM/software
- Who owns follow-up
- Known bottleneck

### Baseline measurements
Collect whatever the client can reliably provide, such as:

- First-response time
- Contact-to-conversation rate
- Lead-to-booking rate
- Estimate/proposal conversion
- Follow-up completion rate
- Stale-lead count
- Pipeline stage conversion

Do not fabricate missing baseline data. Mark unavailable metrics as **Not provided** and establish a measurement plan.

## 6. Kickoff agenda

1. Confirm objective
2. Confirm scope
3. Map current workflow
4. Confirm systems and permissions
5. Confirm baseline measurements
6. Define implementation milestones
7. Identify approval owner
8. Confirm communication channel
9. Confirm first deliverable/date
10. Record open risks and dependencies

## 7. Internal CRM status model

Recommended lifecycle:

`PROPOSAL_SENT → ACCEPTED → CONTRACT_PENDING → PAYMENT_PENDING → PAID → ACCESS_PENDING → KICKOFF → BUILDING → QA → HANDOFF → OPTIMIZATION`

Every client must have one current status.

## 8. Implementation handoff

The implementation record should contain:

- Signed agreement
- Proposal
- Payment record
- Client contacts
- Systems list
- Credentials/access status — never store passwords in this repository
- Workflow map
- Baseline metrics
- Scope boundaries
- Milestones
- Risks/dependencies
- Measurement plan

## 9. Commercial integrity rules

Never:

- Fake payment confirmation
- Claim a client has paid when they have not
- Guarantee a specific revenue increase without a contractually appropriate basis
- Invent baseline metrics
- Use fake testimonials or case studies
- Misrepresent location, company identity or payment eligibility
- Store client passwords/API secrets in GitHub

## 10. Definition of Stage 4F complete

The business is ready to accept its first implementation when:

- A payment method has been verified in the operator's account
- A contract template exists
- A proposal can be accepted and converted into an engagement
- A payment request/invoice process exists
- A client onboarding form exists
- A kickoff checklist exists
- Client status can be tracked from proposal through handoff

## Next stage

**Stage 5 — First 25 verified HVAC prospects + live outreach execution.**

The objective is no longer to build infrastructure for its own sake. The objective becomes evidence: real companies, real observations, real decision makers, real conversations and eventually the first paid diagnostic/implementation.

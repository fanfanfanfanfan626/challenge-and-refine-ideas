---
name: challenge-and-refine-ideas
description: Help users clarify, expand, improve, compare, and stress-test rough ideas through one human-facing facilitator and an automatically sized set of independent advisory perspectives. Use when a user wants to brainstorm, refine an idea, 补充细节, 优化方案, hear multiple viewpoints, invite objections, simulate a focused advisory meeting, expose assumptions, compare alternatives, or turn an early product, business, creative, project, strategy, policy, or decision idea into a decision-ready charter. Use before implementation or commitment. Do not use for simple factual lookup, routine copy editing, emotional therapy, or executing an already-approved plan.
---

# Challenge and Refine Ideas

Help the user think with a small, focused idea council. Keep one facilitator as the only required human-facing voice. Treat perspectives as reasoning lenses and Agent instances as optional independent thinkers, not as simulated employees. Improve the idea without taking ownership away from the user, preserve real disagreement, and end with a clearer decision or a smaller experiment—not manufactured consensus.

Protocol version: `idea-council-v2`.

## Preserve the discussion contract

Apply these rules throughout:

1. Let the user begin with incomplete language, examples, preferences, frustrations, or a half-formed idea.
2. Preserve the user's purpose and vocabulary before proposing a replacement frame.
3. Separate supplied facts, external evidence, user preferences, inferences, assumptions, recommendations, decisions, and unknowns.
4. Critique the idea, not the person. Be candid without performing hostility.
5. Give objections their strongest reasonable form. Do not add a ceremonial skeptic who only restates generic risks.
6. Never use voting or Agent consensus as truth. Explain why perspectives differ and what evidence would resolve the disagreement.
7. Ask one to three high-leverage questions per round. Do not turn the conversation into a form or exhaustive interview.
8. Use the smallest useful council. More voices are valuable only when they bring a genuinely different model, evidence source, stakeholder, failure mode, or decision criterion.
9. Keep the human in control of values, trade-offs, adoption, rejection, and commitment. Silence is not approval.
10. Treat a coherent idea as unvalidated until reality evidence supports it.
11. Treat modeled stakeholder reactions and Agent domain views as hypotheses, not interviews, credentials, or professional advice.

Respond in the user's language and preserve important phrases in their wording.

## Route the session

First infer the user's session intent:

- `explore`: open possibilities and discover meaning without forcing convergence;
- `refine`: improve one current idea and fill consequential gaps;
- `compare`: contrast real alternatives against human-owned criteria;
- `challenge`: steelman the current candidate, then try to reject or reshape it;
- `decide`: make the choice, dissent, evidence sufficiency, and next commitment explicit.

Do not force an `explore` session to produce a recommendation or experiment before the user wants convergence. Move toward `decide` only when the user asks or the discussion naturally reaches a commitment point.

Infer the lightest route that can reduce the current uncertainty:

- `quick-refine`: use the facilitator alone for a narrow, mostly coherent idea that needs clearer wording, missing details, or one counterpoint.
- `guided-workshop`: use the facilitator with two or three lenses serially when the idea has meaningful gaps but independent Agent contexts would add little.
- `independent-council`: use separate advisers when the user explicitly asks for multiple Agent perspectives or when material stakeholder conflict, a specialist question suitable for independent analysis, correlated assumptions, or independent opposition justifies isolation.
- `evidence-first`: pause opinion generation and investigate when a decision depends on unstable, disputed, high-stakes, or externally verifiable facts.
- `decision-review`: test the strongest current version against alternatives, no action, failure scenarios, and decision criteria before the human commits.

Default to `guided-workshop` for `refine` and to a facilitator-led divergent round for `explore`. Move between routes as the idea becomes clearer or new uncertainty appears. Do not ask the user to select Agent count, model, topology, or internal budget. The user may request a faster, deeper, more collaborative, or more delegated interaction style.

## Run one adaptive discussion loop

Use this loop rather than a fixed questionnaire:

```text
narrate → mirror → frame → expand → contrast → challenge
→ synthesize → ask → revise → decide, test, park, or reject
```

### 1. Receive the idea naturally

Let the user explain the idea in their own way. Identify, without demanding every answer at once:

- the desired change and why it matters now;
- the people, situation, or system affected;
- what already exists or is currently done instead;
- the part the user cares about most;
- constraints, non-goals, examples, and feared outcomes;
- the decision or next move the user is actually trying to make.

When the prompt is extremely thin, mirror the most charitable interpretation, mark it as provisional, and ask the single question that would most change the direction.

### 2. Build a live idea frame

Create a compact working model containing:

- current idea in the user's language;
- purpose and intended beneficiary;
- current alternative or status quo;
- known facts and evidence;
- preferences and design principles;
- assumptions and unknowns;
- success, failure, and unacceptable outcomes;
- current decision state.

Do not create or update a file without the user's approval and an agreed path. Never infer permission to overwrite an existing Charter. Keep one canonical Idea Charter when persistence is useful; read `references/idea-charter.md` and use `assets/idea-charter.template.md`.

### 3. Find the uncertainty that matters most

Rank only the uncertainties capable of changing the idea, such as:

- wrong problem or beneficiary;
- unclear value or behavior change;
- hidden alternative or simpler solution;
- contradictory preferences;
- feasibility, resource, timing, or dependency limits;
- adoption, incentives, economics, operations, or maintenance;
- safety, ethics, abuse, legal, privacy, or reputational exposure;
- missing evidence or an untestable success claim.

Choose perspectives to attack those uncertainties. Do not select advisers by impressive job titles. Read `references/perspective-lenses.md` when choosing or briefing multiple lenses. Read `references/discussion-methods.md` when the idea is ambiguous, stuck, contradictory, or needs a deeper workshop.

Before costly L1/L2 council work, show a compact provisional frame containing purpose, beneficiary, current candidate, and decision question. Ask for confirmation only when a materially different interpretation would change adviser selection. If the user explicitly requests immediate divergent brainstorming, proceed with a clearly provisional frame.

### 4. Activate independent advisers only when useful

When child-Agent tools are available, inspect current capacity, keep one slot for the facilitator, and normally use no more than three advisers at once. Prefer two materially different advisers over a large panel. For L1/L2 independence, start advisers with packet-only context and no inherited conversation/history, or the platform equivalent. If clean isolation cannot be guaranteed, label the result L0 even when another Agent produced it. If tools are unavailable or capacity is full, execute the same lenses serially and disclose that the viewpoints were not context-independent.

Give each adviser a bounded, read-only packet containing:

- the user's raw idea or the minimum faithful frame;
- one perspective and one decision-relevant question;
- relevant evidence and constraints;
- what is explicitly out of scope;
- the required brief format and stop condition.

Do not give advisers the facilitator's intended conclusion, another adviser's memo, or the expected answer during the first pass. Include only task-relevant excerpts and avoid propagating unnecessary sensitive information. An adviser may research only when the assigned question needs evidence and available tools permit it. Advisers do not contact external people, imply professional credentials, make commitments, edit the Idea Charter, vote, or authorize execution.

Require every adviser to return this small common core:

```text
Lens and bounded question:
Interpretation:
Decision-relevant claim:
Assumptions, evidence, confidence, and what would change the view:
Implication for the idea or decision:
One or two lens-specific fields requested in the packet:
```

Do not force every lens to write generic advice, objection, risk, and alternative sections. Reserve the fuller format—strongest objection, failure scenario, alternative, falsifier, and required decision—for skeptic/red-team work.

Use an independent challenger for material commitment. Optionally run a first blind pass on the raw idea to expose anchoring and category errors. For the decisive pass, give the challenger a neutral description of the **current candidate**, material changes from the raw idea, constraints, alternatives, and decision criteria; withhold the facilitator's advocacy and other adviser conclusions. Ask it to steelman that current candidate first, then find the strongest reason to reject or reshape it.

After the first adviser pass, check perspective distance: did the advisers use different stakeholders, criteria, time horizons, evidence, or causal assumptions? If their reasoning substantially overlaps, do not count repetition as corroboration. Rebrief an alternative-frame or evidence lens when useful, or disclose that convergence remains correlated.

### 5. Synthesize without laundering disagreement

The facilitator owns integration. Compare advisers by claims and evidence, not personality. Identify:

- genuine agreement and why it exists;
- material disagreements and the assumptions causing them;
- objections that changed the idea;
- objections that remain open;
- ideas that can be combined and choices that cannot;
- the strongest current version, strongest alternative, and no-action option;
- what can be decided now and what needs evidence.

Assign stable IDs such as `O-001` to material objections. Before final synthesis, map every adviser objection ID to exactly one canonical status: `open`, `requires evidence`, `resolved by change`, `resolved by evidence`, `accepted trade-off`, or `rejected by human`. State the supporting change, claim/evidence ID, or human decision. Never silently drop, soften, or mark an objection resolved merely because the facilitator disagrees.

### 6. Continue through focused rounds

Choose the user-facing shape from session intent. Do not force all fields into every round.

For `explore`, normally show emerging interpretations, surprising possibilities or tensions, and one generative question; omit a recommendation unless requested. For `quick-refine`, show the improved idea, important additions, one serious objection, and one next question or action. For `compare`, show alternatives, decision criteria, and unresolved trade-offs without inventing human weights. For `challenge`, show the steelman, strongest attack, repair, and residual objection. For `decide`, use the full decision-ready structure below.

When a full focused round is useful, include only what moves the discussion:

1. **Current understanding** — a short restatement in the user's language.
2. **What the council changed** — new detail, improvement, contradiction, or objection.
3. **Meaningful options** — two or three when a real choice exists, including no action when credible.
4. **Facilitator recommendation** — a reasoned view with confidence and assumptions.
5. **Open question** — one to three questions that would most change the result.
6. **Next reversible step** — a small research, prototype, conversation, test, or decision, when convergence or evidence is the current goal.

Do not show every adviser memo by default. Show distinct views and preserved dissent. Let the user request an adviser's memo verbatim or ask a perspective-specific follow-up relayed by the facilitator; do not stage identity theater.

### 7. Close at the right level

Track idea maturity, evidence/next-step state, and human disposition separately. Evaluate the evidence state against the exact current decision scope, not the idea in the abstract:

```text
maturity: raw → framed → expanded → challenged → decision-ready

evidence_state: discussion-useful | test-needed | review-needed | sufficient-for-scope

human_disposition: undecided | adopted | parked | rejected
```

- `raw`: the idea exists but important meaning is unsettled.
- `framed`: purpose, beneficiary, and intended change are coherent.
- `expanded`: important details, scenarios, alternatives, and constraints exist.
- `challenged`: material assumptions and objections have been tested.
- `decision-ready`: options, trade-offs, recommendation, dissent, and next evidence are explicit.
- `test-needed`: an evidence/next-step state meaning a reversible experiment is more valuable than further discussion; it does not erase maturity.
- `review-needed`: qualified human, professional, consent, legal-authority, safety, or governance review is required before the affected decision.
- `sufficient-for-scope`: the declared evidence standard is met, or no external evidence is required, for the explicitly stated scope; no required review gate remains, and any residual non-high-stakes uncertainty was explicitly accepted by the human within their authority. This is not proof beyond that scope or freshness window.
- `adopted`, `parked`, or `rejected`: human dispositions, not maturity states. Adoption does not prove validation.

Do not keep talking merely to make the idea look complete. Stop when the next uncertainty is best resolved by action or evidence.

Before declaring `decision-ready`, require all of the following:

- the current candidate, beneficiary, purpose, scope, and non-goals are coherent;
- at least one meaningful alternative or no-action path was considered;
- decision criteria and human-owned trade-offs are explicit;
- decision-changing assumptions and evidence limits are labeled;
- every material objection ID is preserved with a canonical status;
- non-high-stakes uncertainty is either bounded by evidence or explicitly accepted by the human within their authority;
- unresolved high-stakes claims, missing consent/legal authority/safety validation, or required professional review set `evidence_state: review-needed` or `test-needed` and block `decision-ready` for consequential action; a bounded non-consequential research/test decision may still be decision-ready within that narrow scope;
- any consequential-action decision uses `evidence_state: sufficient-for-scope` for its exact scope;
- the next commitment, reversibility, stop condition, and reserved human decisions are clear.

If these are not met, use the honest maturity state rather than filling a complete-looking template.

## Ground decision-changing claims

For `evidence-first`, read `references/evidence-grounding.md`. Identify the claim that could change the decision, set an appropriate source and freshness standard, gather only relevant evidence, record applicability and limitations, then mark the claim `supported`, `weakened`, `contradicted`, or `unresolved`. Resume council work only after the evidence threshold is met or the human explicitly chooses to proceed under stated non-high-stakes uncertainty. Medical, legal, financial, safety, and other high-stakes ideas cannot become decision-ready for consequential action from Agent analysis alone.

## Produce the decision-ready result

When the user asks for a final decision synthesis, provide:

```text
Idea and desired future:
Beneficiary, situation, and current alternative:
Value and differentiating principle:
Key experience or operating scenario:
Scope and non-goals:
Important details added:
Options considered:
Strongest objections and disposition:
Assumptions, evidence, and confidence:
Risks and unacceptable outcomes:
Success and failure signals:
Recommended version and why:
Open decisions reserved for the user:
Smallest useful experiment or next step:
Maturity, evidence state, human disposition, council route, adviser independence, and external grounding:
```

Use a smaller session-appropriate synthesis for exploration or quick refinement. Keep minority views when they remain decision-relevant. Report council route, adviser independence, and external grounding separately. Do not claim market, technical, legal, medical, financial, or safety validation from discussion alone.

## Hand off without accidental execution

This Skill develops and challenges intent; it does not automatically implement the idea. When the user explicitly asks to proceed:

- hand a decision-ready Idea Charter to the appropriate execution workflow;
- hand off consequential execution only when `evidence_state` is `sufficient-for-scope` and the human explicitly authorizes that exact scope; while it is `test-needed` or `review-needed`, hand off only the bounded test, research, or review scope that is actually authorized;
- for a substantial product, material feature, or governed multi-Agent project, use `$orchestrate-agent-organization` and preserve the Charter's dissent, evidence gaps, non-goals, and human-reserved choices;
- for a small reversible task, execute directly under the clarified scope;
- stop for professional or human approval when the decision creates legal, medical, financial, safety, privacy, or broad external consequences.

## Prevent meeting failure modes

- Do not simulate attendance, introductions, recurring meetings, or departmental theater.
- Do not let every perspective comment on everything.
- Do not repeat the same advice under different role names.
- Do not make the user coordinate advisers or read raw internal chatter.
- Do not replace a concrete objection with a balanced-sounding summary.
- Do not overwhelm an early idea with implementation detail before value and direction are coherent.
- Do not force consensus when the real choice depends on human taste or risk appetite.
- Do not use discussion to avoid a cheap reality test.
- Do not turn a user's preference into a factual claim or an Agent inference into evidence.
- Do not continue a council whose marginal insight is lower than its coordination cost.

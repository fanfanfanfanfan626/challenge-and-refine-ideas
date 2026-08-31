# Idea Charter and session state

Use one Idea Charter when the user wants a durable synthesis, the discussion spans tasks, several revisions exist, or the result will be handed to execution. Chat remains sufficient for a short session. Obtain the user's approval and agree on the path before creating or updating a file; never overwrite an existing Charter by inference.

## Contents

1. Canonical record
2. State transitions
3. Evidence and dissent
4. Versioning
5. Handoff and closeout

## 1. Canonical record

Use `assets/idea-charter.template.md` as the only normative idea artifact. Advisers return temporary briefs; the facilitator alone integrates accepted changes. Do not create separate strategy, objections, requirements, and summary documents when sections of the Charter remain navigable.

Keep maturity, evidence state, human disposition, council route, adviser independence, and external grounding at the top. Preserve consequential history below them. Use the user's language for purpose and principles; use precise labels for assumptions, evidence, disagreement, and decisions.

## 2. State transitions

Use three orthogonal fields. Evaluate the evidence state against the exact current decision scope, not the idea in the abstract:

```text
maturity: raw → framed → expanded → challenged → decision-ready

evidence_state: discussion-useful | test-needed | review-needed | sufficient-for-scope

human_disposition: undecided | adopted | parked | rejected
```

Advance only when the relevant condition is met:

- `framed`: purpose, beneficiary, intended change, and major boundary are coherent.
- `expanded`: scenarios, important details, alternatives, and constraints are represented.
- `challenged`: material assumptions, counterexamples, and stakeholder objections are visible.
- `decision-ready`: recommendation, trade-offs, dissent, evidence gaps, and next action are explicit.
- `discussion-useful`: another bounded discussion could still materially improve the decision.
- `test-needed`: further discussion has less value than a reversible evidence action.
- `review-needed`: consequential action requires missing consent, authority, safety validation, or qualified human/professional review.
- `sufficient-for-scope`: the declared evidence standard is met, or no external evidence is required, for the explicitly stated scope; no required review gate remains, and any residual non-high-stakes uncertainty was explicitly accepted by the human within their authority. It does not imply validation outside that scope or freshness window.
- `adopted`, `parked`, or `rejected`: the human explicitly chooses the disposition. These are never maturity values, and `adopted` does not mean validated.

A material change to purpose, beneficiary, central principle, scope, or unacceptable outcome returns the Charter to the appropriate earlier state.

## 3. Evidence and dissent

Label claims as:

- `supplied fact`: stated by the user or source but not necessarily independently checked;
- `external evidence`: linked observation or source with observed/published date, checked date, applicability, and limitations;
- `preference`: a human value, taste, or priority;
- `inference`: a conclusion from available information;
- `assumption`: necessary but unverified;
- `recommendation`: an adviser's or facilitator's proposed choice;
- `decision`: explicitly chosen by the human;
- `unknown`: important information not yet available.

Give each material objection a stable ID and exactly one status:

- `open`;
- `requires evidence`;
- `resolved by change`;
- `resolved by evidence`, with supporting claim or evidence ID;
- `accepted trade-off`;
- `rejected by human`, with rationale.

Do not mark an objection resolved merely because the facilitator disagrees. Agent consensus cannot change an evidence label or make a human decision.

Before a final decision synthesis, reconcile the complete adviser objection set against the Charter ledger. Every material objection must appear once with its original decision-relevant meaning preserved. A shortened wording must not weaken its required change, evidence, or accepted downside.

## 4. Versioning

Create a new version when purpose, target beneficiary, core principle, material scope, risk boundary, success evidence, or disposition changes. For small refinements, update the current version and add a dated decision entry.

Each version records:

- what changed;
- why it changed;
- which evidence or objection caused the change;
- who made the decision;
- which earlier assumptions or sections are superseded;
- what must be revisited later.

Never delete a consequential rejected option or dissent when it remains useful for understanding the decision. Summarize it and link to source evidence rather than retaining full transcripts.

## 5. Handoff and closeout

A decision-ready handoff includes:

- the exact idea version and state;
- desired outcome, beneficiary, non-goals, and principles;
- chosen option and rejected alternatives;
- accepted trade-offs and open objections;
- evidence and unresolved assumptions;
- success, failure, stop, and revisit signals;
- next experiment or authorized scope;
- decisions reserved for the human.

Do not label a Charter `decision-ready` unless the current candidate and alternatives are coherent, decision criteria and human trade-offs are explicit, evidence limits are visible, all material objections have canonical statuses, and the next bounded commitment has reversibility and stop conditions. A human may explicitly accept bounded, non-high-stakes uncertainty within their authority. Unresolved high-stakes claims, missing consent or legal authority, missing safety validation, or required qualified review set the evidence state to `test-needed` or `review-needed` and block `decision-ready` for consequential action. A bounded, non-consequential test, research step, or review request may itself be decision-ready, but only within that narrow scope.

Discussion readiness is not execution authorization. Hand off consequential execution only when the evidence state is `sufficient-for-scope` and the human explicitly authorizes that exact scope. While the evidence state is `test-needed` or `review-needed`, hand off only the explicitly authorized test, research, or review scope. When handed to a build or organization workflow, preserve the Charter's human language, dissent, and unknowns. Do not silently translate an assumption into a requirement or a recommendation into approval.

At closeout, report the council route, adviser independence level, external grounding level, what materially changed, which objections remain, and whether the next step is another decision, evidence gathering, professional review, implementation, parking, or rejection.

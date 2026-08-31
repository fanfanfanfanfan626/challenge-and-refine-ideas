# Evidence grounding for idea decisions

Use this reference only when a decision depends on facts that are unstable, disputed, externally verifiable, or high stakes. Evidence work answers a bounded decision question; it is not a broad research detour.

## Contents

1. Select the decision-changing claim
2. Set the evidence standard
3. Gather and compare
4. Record applicability and limits
5. Resume or stop

## 1. Select the decision-changing claim

Identify the smallest claim whose truth would materially change the option, design, risk, or next action. Examples include:

- a target user actually experiences the stated problem;
- an existing alternative already solves it;
- a law, policy, platform rule, price, or technical capability permits the plan;
- a claimed behavior, market, safety, or operational effect exists;
- a proposed experiment can measure the intended outcome.

Do not research a human preference as though it were a fact. Do not collect background information that cannot change the decision.

## 2. Set the evidence standard

Before searching, state:

- the claim and affected decision;
- required authority, directness, and recency;
- acceptable evidence types;
- disconfirming evidence to seek;
- the threshold for supported, contradicted, or still unresolved;
- time or search limits.

Prefer evidence closest to the claim: direct user/field observation, measured operational data, controlled experiment, primary official source, original research, maintained upstream documentation, then reputable synthesis. Agent explanation and repeated secondary summaries are orientation, not independent confirmation.

For current laws, regulations, prices, platform rules, market facts, medical or safety claims, use up-to-date authoritative sources and state jurisdiction or scope. High-stakes decisions require qualified human or professional review where appropriate.

## 3. Gather and compare

Use available research or browsing tools when the claim needs external facts. Search for both support and falsification. Compare source date, authority, method, population or environment, incentives, and whether sources are independent.

Do not count multiple pages repeating one origin as multiple sources. Do not treat modeled stakeholder opinion as user research. If direct evidence is unavailable, say what proxy was used and why.

Stop when:

- the decision threshold is met;
- the claim is contradicted strongly enough to change course;
- further sources repeat the same evidence;
- the remaining uncertainty requires an experiment, user contact, professional review, or unavailable private data;
- the search budget is exhausted.

## 4. Record applicability and limits

For every decision-relevant evidence item record:

```text
Claim and evidence ID:
Source and link/path:
Observed or published date:
Checked date:
Evidence type and independence:
Population, jurisdiction, product, or environment:
Result:
Applicability to this idea:
Limitations, conflicts, and producer incentives:
Confidence and freshness/revisit trigger:
```

Mark the claim outcome as:

- `supported`: the stated threshold is met within the recorded boundary;
- `weakened`: evidence reduces confidence but does not decide the claim;
- `contradicted`: the threshold for rejection or redesign is met;
- `unresolved`: evidence is missing, conflicting, stale, or inapplicable.

Never silently convert `unresolved` into an assumption that implementation may treat as true.

## 5. Resume or stop

Return to the council with only the evidence that changes the frame, options, objection status, or next action. Update the Idea Charter claim ledger and note which prior assumptions were confirmed, weakened, contradicted, or remain unresolved.

Resume convergence only when the declared evidence threshold is met or the human explicitly accepts bounded, non-high-stakes uncertainty within their authority. When the threshold is met, or no external evidence is required for the explicitly stated scope, no review gate remains, and any residual non-high-stakes uncertainty is accepted within the human's authority, set `evidence_state: sufficient-for-scope`; record the scope and freshness limit. If evidence shows the next best step is a reversible test, set `evidence_state: test-needed`. If qualified review, consent, legal authority, or safety validation is missing, set `evidence_state: review-needed` and do not label the idea decision-ready for consequential action. The review request or a bounded, non-consequential test may itself be decision-ready only within that narrow scope.

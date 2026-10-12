# First-use meeting prompts

These are request templates, not transcripts, testimonials, external evidence, or proof of live-host or model behavior. Replace brackets with your situation after installing the complete skill.

## `explore`

```text
Use $challenge-and-refine-ideas to explore this idea: [idea]. Keep the frame provisional, show two or three materially different interpretations or tensions, and ask one generative question. Do not recommend, decide, or prescribe an experiment or next commitment unless I explicitly ask to converge.
```

## `refine`

```text
Use $challenge-and-refine-ideas to refine this idea while preserving my purpose: [idea]. Separate supplied facts, external evidence, preferences, inferences, assumptions, recommendations, decisions, and unknowns. Return the improved current candidate, one consequential addition, one serious objection, and the next question. Do not turn council opinion into evidence.
```

## `compare`

```text
Use $challenge-and-refine-ideas to compare [option A], [option B], and no action against [criteria]. Do not invent my weights. Separate verified evidence from adviser opinion, label unknowns, preserve unresolved objections, and leave the final trade-off to me.
```

## `challenge`

```text
Use $challenge-and-refine-ideas to challenge the current latest version below, not an older draft: [current candidate]. Steelman that candidate first, then attack its strongest causal link. Give each material objection a stable ID and one canonical status, state what evidence would resolve it, and show both the best repair and the residual objection.
```

## `decide`

```text
Use $challenge-and-refine-ideas to help me decide this exact scope: [decision]. Show the current candidate, alternatives including no action, criteria, human-owned trade-offs, evidence limits, dissent, and recommendation confidence. Do not execute or hand off the decision. For medical, legal, financial, safety, privacy, consent, or broad external consequences, set test-needed or review-needed as appropriate and prohibit consequential execution until required review is complete, evidence is sufficient-for-scope, and I explicitly authorize the exact action.
```

Objection statuses: `open`, `requires evidence`, `resolved by change`, `resolved by evidence`, `accepted trade-off`, `rejected by human`.

## 中文首次使用

探索：用 $challenge-and-refine-ideas 帮我探索这个想法：[想法]。先保留两三个不同理解和一个值得继续追问的问题，不急着推荐、结论或安排实验。

反证：用 $challenge-and-refine-ideas 攻击下面这个最新版本：[当前方案]。先准确复述，再给异议编号、解决它需要的证据与修改后仍留下的风险。不要攻击已放弃的旧方案，也不要把顾问的一致看法当成现实证据。

# Compatibility and evidence

Compatibility claims are intentionally narrower than package-format claims.

| Environment or capability | Status | Evidence and limit |
| --- | --- | --- |
| Repository and standalone ZIP | Verified for 2.0.2 | The validator checks the exact eight-file package, nested MIT license, references, invariants, local-path leakage, ZIP bytes, checksum, and public version markers. |
| Codex Skill discovery | Package-compatible | The package follows the local Skill directory and `SKILL.md` layout. A named, repeatable live-host evaluation has not yet been published. |
| Other Agent Skills hosts | Portable instructions | Hosts must preserve relative files and expose the Skill entry point. Discovery, permissions, and invocation behavior must be verified on that host. |
| `L0` serial lenses | Baseline | Works without child-agent isolation, but the perspectives are correlated and must be labeled `L0`. |
| `L1` isolated memos | Capability-dependent | Requires child contexts that receive only the bounded adviser packet. |
| `L2` blind challenge | Capability-dependent | Requires a neutral current-candidate packet and a challenger isolated from facilitator advocacy. |
| External evidence | Not supplied by agent count | Browsing, field data, experiments, operations, or qualified review must be gathered and labeled separately. |

Automated package validation does not prove decision quality, adviser independence, host compatibility, or real-world outcomes. When reporting a successful run, record the host and version, available isolation level, exact Skill commit or release, and the evidence source used.

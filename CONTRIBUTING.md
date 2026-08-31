# Contributing

Issues and pull requests are welcome. Changes should preserve human control, honest independence labels, evidence boundaries, stable dissent, and explicit authorization before execution.

## Development rules

1. Edit the installable package under `skill/challenge-and-refine-ideas/`.
2. Keep repository documentation and release tooling outside the package.
3. Do not weaken an objection, evidence, review, consent, or authorization gate for smoother output.
4. Treat adviser independence and external grounding as separate dimensions.
5. Keep exploration open unless the user chooses convergence.
6. Run the release audit:

```bash
python -m pip install -r requirements-dev.txt
python tools/validate_release.py
```

When the seven package files change, build and review a new versioned ZIP rather than silently replacing the audited v2 archive.

## Pull request checklist

- Explain the decision failure or meeting failure the change addresses.
- Identify the affected session intent, route, state, evidence gate, or objection rule.
- Include a falsifiable scenario or clean-context review where appropriate.
- Avoid secrets, local paths, generated files, transcripts, and simulated credentials.
- Update both English and Chinese public documentation for user-visible behavior changes.

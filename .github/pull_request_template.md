## What changed

Describe the concrete discussion or decision failure this change addresses.

## Evidence and boundaries

- What source, fixture, or scenario supports the change?
- Does it affect adviser independence, evidence labels, objection preservation, professional review, or human authorization?
- Does it change the seven-file release package or audited ZIP?

## Validation

```bash
python -m pip install -r requirements-dev.txt
python tools/validate_release.py
```

- [ ] I ran the validator.
- [ ] I removed private paths, secrets, personal data, and confidential prompts.
- [ ] I updated English and Chinese documentation when user-facing behavior changed.

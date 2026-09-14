# AI installation contract

Install the `challenge-and-refine-ideas` skill from:

```text
https://github.com/fanfanfanfanfan626/challenge-and-refine-ideas
```

Package facts:

- The repository root contains documentation and validation infrastructure, not a root skill entry point.
- The complete installable directory is `skill/challenge-and-refine-ideas/`.
- Its entry point is `skill/challenge-and-refine-ideas/SKILL.md`.
- Copy the full directory without flattening it; `LICENSE`, `agents/`, `assets/`, and `references/` are required siblings.
- Do not search for a root-level `SKILL.md` and do not install only the entry file.
- Do not copy root-level `README*`, `dist/`, `tools/`, or `.github/` into the host's skill directory. The package's nested `LICENSE` must remain with the Skill.
- Do not overwrite an existing installation without first telling the user what will change.

An audited ZIP is available at `dist/challenge-and-refine-ideas-v2.0.1.zip` with SHA-256:

```text
7B8B69F30513D2E8E9F697616D161A55F5E3B8A6C7E0FBFE7AA417EDF6A45AF6
```

The ZIP expands to one top-level `challenge-and-refine-ideas/` directory containing exactly eight files, including the MIT license, and no cache files.

For Codex, the default destination is:

```text
~/.codex/skills/challenge-and-refine-ideas/
```

After installation, verify that the destination contains `SKILL.md`, then restart Codex. A valid invocation is:

```text
Use $challenge-and-refine-ideas to challenge the strongest current version of my idea, preserve every material objection, and identify what evidence would change the decision.
```

For another agent host, preserve relative paths and expose the entry point plus its resources. The guided workshop can run serially. L1/L2 adviser independence requires packet-only child contexts without inherited history; otherwise label the result L0.

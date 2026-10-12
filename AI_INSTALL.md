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

An audited ZIP is available at `dist/challenge-and-refine-ideas-v2.0.4.zip` with SHA-256:

```text
8CD26839FE7F959BF8AB550E4B1E5C4D02BC0A833B68FC8BD04733F992D75315
```

The ZIP expands to one top-level `challenge-and-refine-ideas/` directory containing exactly nine files, including the MIT license, and no cache files.

For Codex, the default destination is:

```text
~/.codex/skills/challenge-and-refine-ideas/
```

## Updating an existing installation

The README commands intentionally refuse an existing directory, file or link. Do not repeat a recursive copy into an existing directory: that can leave the old entry point active with a second package nested underneath it.

Close the host, verify the exact existing installation path, inspect any local edits, and obtain approval for replacement. Move only that specific skill directory to a backup outside the host's discovery roots. Then use the fresh-install procedure and confirm `SKILL.md`, `LICENSE`, `agents/`, `assets/` and `references/` are direct children of the destination. Do not delete the parent skills directory or other skills. Keep the backup until discovery and a real invocation have been checked. Stop for unexpected files or links rather than following them.

## Verify discovery separately from use

After installation, verify that the destination contains `SKILL.md`, then restart Codex. A valid invocation is:

```text
Use $challenge-and-refine-ideas to challenge the strongest current version of my idea, preserve every material objection, and identify what evidence would change the decision.
```

For another agent host, preserve relative paths and expose the entry point plus its resources. The guided workshop can run serially. L1/L2 adviser independence requires packet-only child contexts without inherited history; otherwise label the result L0.

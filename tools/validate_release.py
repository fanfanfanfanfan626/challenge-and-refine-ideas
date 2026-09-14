#!/usr/bin/env python3
"""Validate the public Idea Council skill and its audited v2 archive."""

from __future__ import annotations

import hashlib
import re
import sys
import zipfile
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "challenge-and-refine-ideas"
SKILL_MD = SKILL / "SKILL.md"
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
ARCHIVE = ROOT / "dist" / f"challenge-and-refine-ideas-v{VERSION}.zip"
EXPECTED_ARCHIVE_SHA256 = "24D940A87FD45DDF1608BBE734999A9E2168526DFDCD1DE6D5BF55266470A11F"

REQUIRED_FILES = (
    "LICENSE",
    "SKILL.md",
    "agents/openai.yaml",
    "assets/idea-charter.template.md",
    "references/discussion-methods.md",
    "references/evidence-grounding.md",
    "references/idea-charter.md",
    "references/perspective-lenses.md",
)

REQUIRED_PROTOCOL_MARKERS = (
    "idea-council-v2",
    "`explore`",
    "`refine`",
    "`compare`",
    "`challenge`",
    "`decide`",
    "L0",
    "L1",
    "L2",
    "sufficient-for-scope",
    "explicitly authorizes",
    "O-001",
)

LOCAL_OR_SECRET_PATTERNS = {
    "Windows user path": re.compile(r"(?i)C:\\Users\\"),
    "macOS user path": re.compile(r"/Users/[^/\s]+/"),
    "GitHub token": re.compile(r"(?:ghp_[A-Za-z0-9]+|github_pat_[A-Za-z0-9_]+)"),
    "private key": re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY"),
}


def error(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_frontmatter(text: str, errors: list[str]) -> None:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        error(errors, "SKILL.md must begin with YAML frontmatter")
        return
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        error(errors, "SKILL.md frontmatter must be a mapping")
        return
    if set(data) != {"name", "description"}:
        error(errors, "SKILL.md frontmatter must contain only name and description")
    if data.get("name") != "challenge-and-refine-ideas":
        error(errors, "SKILL.md name must match the package directory")
    if not isinstance(data.get("description"), str) or not data["description"].strip():
        error(errors, "SKILL.md description must be non-empty")


def validate_archive(errors: list[str], package_files: dict[str, bytes]) -> None:
    if not ARCHIVE.is_file():
        error(errors, f"missing audited archive: {ARCHIVE.relative_to(ROOT)}")
        return
    digest = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest().upper()
    if digest != EXPECTED_ARCHIVE_SHA256:
        error(errors, f"archive SHA-256 mismatch: {digest}")

    with zipfile.ZipFile(ARCHIVE) as archive:
        members = {
            name: archive.read(name)
            for name in archive.namelist()
            if not name.endswith("/")
        }
    prefix = "challenge-and-refine-ideas/"
    normalized: dict[str, bytes] = {}
    for name, content in members.items():
        if not name.startswith(prefix):
            error(errors, f"archive member is outside the skill directory: {name}")
            continue
        normalized[name[len(prefix) :]] = content
    if normalized != package_files:
        missing = sorted(set(package_files) - set(normalized))
        extra = sorted(set(normalized) - set(package_files))
        changed = sorted(
            name
            for name in set(normalized) & set(package_files)
            if normalized[name] != package_files[name]
        )
        error(errors, f"archive differs from package; missing={missing}, extra={extra}, changed={changed}")


def main() -> int:
    errors: list[str] = []

    package_files = {
        path.relative_to(SKILL).as_posix(): path.read_bytes()
        for path in SKILL.rglob("*")
        if path.is_file()
    } if SKILL.is_dir() else {}

    if VERSION != "2.0.3":
        error(errors, f"unexpected release version: {VERSION}")
    if (SKILL / "LICENSE").read_bytes() != (ROOT / "LICENSE").read_bytes():
        error(errors, "package LICENSE must match the repository LICENSE")
    public_markers = {
        ROOT / "README.md": f"challenge-and-refine-ideas-v{VERSION}.zip",
        ROOT / "README.zh-CN.md": f"challenge-and-refine-ideas-v{VERSION}.zip",
        ROOT / "AI_INSTALL.md": f"challenge-and-refine-ideas-v{VERSION}.zip",
        ROOT / "docs" / "index.html": f'"version": "{VERSION}"',
        ROOT / "docs" / "llms.txt": f"Current release: {VERSION}",
        ROOT / "CHANGELOG.md": f"## {VERSION}",
    }
    for path, marker in public_markers.items():
        if marker not in path.read_text(encoding="utf-8"):
            error(errors, f"{path.relative_to(ROOT)} is missing version marker: {marker}")

    if set(package_files) != set(REQUIRED_FILES):
        missing = sorted(set(REQUIRED_FILES) - set(package_files))
        extra = sorted(set(package_files) - set(REQUIRED_FILES))
        error(errors, f"package must contain exactly eight release files; missing={missing}, extra={extra}")

    if not SKILL_MD.is_file():
        error(errors, "missing skill/challenge-and-refine-ideas/SKILL.md")
    else:
        skill_text = SKILL_MD.read_text(encoding="utf-8")
        parse_frontmatter(skill_text, errors)
        if len(skill_text.splitlines()) > 500:
            error(errors, "SKILL.md exceeds 500 lines")
        for marker in REQUIRED_PROTOCOL_MARKERS:
            if marker not in skill_text:
                error(errors, f"required protocol marker missing from SKILL.md: {marker}")
        referenced = set(
            re.findall(r"(?:references|assets)/[A-Za-z0-9_.-]+", skill_text)
        )
        for relative in sorted(referenced):
            if not (SKILL / relative).is_file():
                error(errors, f"SKILL.md references a missing file: {relative}")

    metadata_path = SKILL / "agents" / "openai.yaml"
    if metadata_path.is_file():
        metadata = yaml.safe_load(metadata_path.read_text(encoding="utf-8"))
        interface = metadata.get("interface", {}) if isinstance(metadata, dict) else {}
        if not isinstance(interface, dict):
            error(errors, "agents/openai.yaml interface must be a mapping")
        else:
            short_description = interface.get("short_description", "")
            if not isinstance(short_description, str) or not 25 <= len(short_description) <= 64:
                error(errors, "short_description must contain 25-64 characters")
            default_prompt = str(interface.get("default_prompt", ""))
            if "$challenge-and-refine-ideas" not in default_prompt:
                error(errors, "default_prompt must mention $challenge-and-refine-ideas")

    for relative, raw in package_files.items():
        if "__pycache__" in Path(relative).parts or Path(relative).suffix in {".pyc", ".pyo"}:
            error(errors, f"generated file must not ship: {relative}")
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in LOCAL_OR_SECRET_PATTERNS.items():
            if pattern.search(text):
                error(errors, f"{label} found in {relative}")

    validate_archive(errors, package_files)

    sums = (ROOT / "SHA256SUMS").read_text(encoding="utf-8").strip()
    expected_line = f"{EXPECTED_ARCHIVE_SHA256}  {ARCHIVE.relative_to(ROOT).as_posix()}"
    if sums != expected_line:
        error(errors, "SHA256SUMS does not match the audited archive")

    if errors:
        for message in errors:
            print(f"ERROR: {message}", file=sys.stderr)
        return 1

    print(f"Validated {len(package_files)} skill files and archive {EXPECTED_ARCHIVE_SHA256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

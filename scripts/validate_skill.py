#!/usr/bin/env python3
"""Lightweight repository validator for Codex skill packaging."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(path: Path) -> None:
    if not path.exists():
        fail(f"missing required path: {path}")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    try:
        _, block, _ = text.split("---", 2)
    except ValueError:
        fail("SKILL.md frontmatter is not closed")

    values: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def check_skill(skill_dir: Path) -> None:
    skill_md = skill_dir / "SKILL.md"
    require(skill_md)
    require(skill_dir / "agents" / "openai.yaml")
    require(skill_dir / "references")

    text = skill_md.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)
    for key in ("name", "description"):
        if not meta.get(key):
            fail(f"SKILL.md frontmatter missing {key!r}")

    links = re.findall(r"\]\((references/[^)]+)\)", text)
    for link in links:
        require(skill_dir / link)

    for ref in (skill_dir / "references").glob("*.md"):
        if not ref.read_text(encoding="utf-8").strip():
            fail(f"empty reference file: {ref}")


def check_repo(repo: Path) -> None:
    for path in [
        repo / "README.md",
        repo / "README.en.md",
        repo / "LICENSE",
        repo / "CONTRIBUTING.md",
        repo / "docs" / "screening-checklist.md",
        repo / "docs" / "data-sources.md",
        repo / "docs" / "prompt-library.md",
        repo / "examples" / "README.md",
    ]:
        require(path)

    check_skill(repo / "skills" / "bay-area-rental")


def main() -> int:
    repo = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    check_repo(repo.resolve())
    print("Repository skill package is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

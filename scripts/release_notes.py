"""Write one version's CHANGELOG.md section as GitHub Release notes."""

import argparse
from pathlib import Path
import re

REPO_ROOT = Path(__file__).resolve().parents[1]


def extract(changelog, tag):
    """Return the body under `## <tag>`, up to the next second-level heading."""
    match = re.search(rf"^## {re.escape(tag)}\n(.*?)(?=^## |\Z)", changelog, re.MULTILINE | re.DOTALL)
    if not match or not match.group(1).strip():
        raise ValueError(f"CHANGELOG.md has no '## {tag}' section")
    return match.group(1).strip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tag")
    parser.add_argument("--changelog", type=Path, default=REPO_ROOT / "CHANGELOG.md")
    parser.add_argument("--output", type=Path, default=Path("release-notes.md"))
    args = parser.parse_args()
    try:
        notes = extract(args.changelog.read_text(encoding="utf-8"), args.tag)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Release notes failed: {error}\n")
    args.output.write_text(notes, encoding="utf-8")
    print(f"Wrote {args.output} for {args.tag}")


if __name__ == "__main__":
    main()

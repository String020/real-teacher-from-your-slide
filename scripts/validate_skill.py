"""Check this repository's Skill manifest and runtime reference files."""

import argparse
from pathlib import Path
import re

import yaml

SKILL_NAME = "a-real-teacher-from-your-slide"
REPO_ROOT = Path(__file__).resolve().parents[1]


def runtime_paths(root):
    """Select only the instruction bundle and its license, never the whole repo."""
    root = Path(root).resolve()
    paths = [Path("SKILL.md"), Path("LICENSE"), Path("agents/openai.yaml")]
    references = root / "references"
    if not references.is_dir() or references.is_symlink():
        raise ValueError("references/ must be a real directory")
    paths.extend(p.relative_to(root) for p in references.rglob("*.md"))
    if len(paths) == 3:
        raise ValueError("references/ contains no Markdown resources")
    for relative in paths:
        path = root / relative
        if any(part.startswith(".") for part in relative.parts):
            raise ValueError(f"Hidden runtime path: {relative}")
        if not path.is_file():
            raise ValueError(f"Missing runtime file: {relative}")
        if not path.resolve().is_relative_to(root):
            raise ValueError(f"Runtime path leaves the repository: {relative}")
        # Also reject links that point inside the repository: archives carry copies.
        if any(parent.is_symlink() for parent in [path, *path.parents] if parent != root):
            raise ValueError(f"Symlink in runtime path: {relative}")
    return sorted(paths)


def load_mapping(text, label):
    try:
        value = yaml.safe_load(text)
    except yaml.YAMLError as error:
        raise ValueError(f"Invalid YAML in {label}: {error}") from error
    if not isinstance(value, dict):
        raise ValueError(f"{label} must contain a YAML mapping")
    return value


def validate(root):
    root = Path(root).resolve()
    paths = runtime_paths(root)
    text = (root / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md needs YAML frontmatter between --- lines")
    manifest = load_mapping(match.group(1), "SKILL.md frontmatter")
    if manifest.get("name") != SKILL_NAME:
        raise ValueError(f"Skill name must remain {SKILL_NAME}")
    description = manifest.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        raise ValueError("Skill description must be a nonempty string of at most 1024 characters")
    if not text[match.end():].strip():
        raise ValueError("SKILL.md has no instructions")

    ui = load_mapping((root / "agents/openai.yaml").read_text(encoding="utf-8"), "agents/openai.yaml")
    interface = ui.get("interface")
    if not isinstance(interface, dict):
        raise ValueError("agents/openai.yaml needs an interface mapping")
    for key in ("display_name", "short_description"):
        if not isinstance(interface.get(key), str) or not interface[key].strip():
            raise ValueError(f"interface.{key} must be a nonempty string")

    included = {p.as_posix() for p in paths}
    for relative in paths:
        if relative.suffix != ".md":
            continue
        content = (root / relative).read_text(encoding="utf-8")
        for target in re.findall(r"references/[a-zA-Z0-9_./-]+\.md", content):
            if target not in included:
                raise ValueError(f"{relative}: reference is missing from the bundle: {target}")
    return paths


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPO_ROOT)
    args = parser.parse_args()
    try:
        paths = validate(args.root)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Validation failed: {error}\n")
    print(f"Validated {len(paths)} runtime files. Teaching behavior requires separate evaluation.")


if __name__ == "__main__":
    main()

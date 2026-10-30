"""Catch drift between the Skill's instructions, documentation, and fixtures without calling a model."""

import json
from pathlib import Path
import re
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_skill import REPO_ROOT

STATUS_VALUES = ["not started", "learning", "needs review", "mastered"]
# Plausible status spellings an editor might introduce instead of the four above.
STATUS_VARIANTS = {"in progress", "done", "completed", "complete", "reviewing", "todo", "not-started", "needs-review", "review"}
TREE_DIRECTORIES = ("references", "scripts", "tests")


def read(relative):
    return (REPO_ROOT / relative).read_text(encoding="utf-8")


def without_code_blocks(text):
    return re.sub(r"^```.*?^```", "", text, flags=re.MULTILINE | re.DOTALL)


def lettered_modes(text):
    """Return the names of the first A-J list, the direct mode menu."""
    names = re.findall(r"^[A-J]\. (.+?)\s*$", text, flags=re.MULTILINE)
    for start in range(len(names) - 9):
        lines = re.findall(r"^([A-J])\. ", text, flags=re.MULTILINE)[start:start + 10]
        if "".join(lines) == "ABCDEFGHIJ":
            return names[start:start + 10]
    raise AssertionError("No A-J mode list found")


def supported_modes(readme):
    section = re.search(r"^## (?:Supported Modes|支持的学习模式)\n(.*?)(?=^## )", readme, re.MULTILINE | re.DOTALL)
    return re.findall(r"^- \*\*(.+?)\*\*", section.group(1), flags=re.MULTILINE)


def path_sequences(text):
    """Return learning paths: lines with at least four arrows, split into steps."""
    sequences = []
    for line in without_code_blocks(text).splitlines():
        if line.count("->") < 4:
            continue
        if "**" in line:
            line = line.rsplit(": ", 1)[1]
        line = line.strip().strip("`").rstrip(".")
        steps = [re.sub(r"\s*[(（].*?[)）]$", "", step.strip()) for step in line.split("->")]
        sequences.append(steps)
    return sequences


def tree_entries(readme):
    """Map each tracked directory in the README tree to the file names listed under it."""
    tree = re.search(r"^```text\nreal-teacher-from-your-slide/\n(.*?)^```", readme, re.MULTILINE | re.DOTALL).group(1)
    entries, current = {}, None
    for line in tree.splitlines():
        top = re.match(r"^[├└]── (.+?)/?$", line)
        if top:
            current = top.group(1) if line.endswith("/") else None
            entries.setdefault(current, [])
            continue
        child = re.match(r"^[│ ]   [├└]── (.+)$", line)
        if child and current:
            entries[current].append(child.group(1))
    return entries


def slugs(markdown):
    """Approximate GitHub heading anchors, including -1 suffixes for repeated headings."""
    seen, result = {}, set()
    for heading in re.findall(r"^#{1,6} (.+?)\s*$", without_code_blocks(markdown), flags=re.MULTILINE):
        slug = "".join(c for c in heading.lower() if c.isalnum() or c in " -_").replace(" ", "-")
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        result.add(slug if count == 0 else f"{slug}-{count}")
    return result


class ModeNameTests(unittest.TestCase):
    def setUp(self):
        self.modes = lettered_modes(read("SKILL.md"))

    def test_mode_menus_and_readme_list_the_same_modes(self):
        self.assertEqual(lettered_modes(read("references/mode-router.md")), self.modes)
        self.assertEqual(supported_modes(read("README.md")), self.modes)
        self.assertEqual(len(supported_modes(read("README.zh-CN.md"))), len(self.modes))

    def test_learning_paths_use_only_defined_modes_and_agree(self):
        found = []
        for relative in ("SKILL.md", "references/mode-router.md", "README.md"):
            for sequence in path_sequences(read(relative)):
                for step in sequence:
                    self.assertIn(step, self.modes, f"{relative}: undefined mode in learning path: {step}")
                found.append(tuple(sequence))
        self.assertEqual(len(found), 6, "Expected the two learning paths in SKILL.md, mode-router.md, and README.md")
        self.assertEqual(len(set(found)), 2, "The same learning path differs between files")

    def test_chinese_paths_match_english_paths(self):
        names = [name.split(" / ") for name in supported_modes(read("README.zh-CN.md"))]
        translated = []
        for sequence in path_sequences(read("README.zh-CN.md")):
            steps = []
            for step in sequence:
                index = next((i for i, alternatives in enumerate(names) if step in alternatives), None)
                self.assertIsNotNone(index, f"README.zh-CN.md: undefined mode in learning path: {step}")
                steps.append(self.modes[index])
            translated.append(steps)
        self.assertEqual(translated, path_sequences(read("README.md")))


class RegistrationTests(unittest.TestCase):
    def test_every_reference_is_in_the_skill_reference_map(self):
        skill = read("SKILL.md")
        for path in sorted((REPO_ROOT / "references").glob("*.md")):
            self.assertIn(f"- `references/{path.name}`:", skill, f"SKILL.md reference map is missing {path.name}")

    def test_readme_trees_match_tracked_files(self):
        for readme in ("README.md", "README.zh-CN.md"):
            entries = tree_entries(read(readme))
            for directory in TREE_DIRECTORIES:
                suffix = ".md" if directory == "references" else ".py"
                actual = sorted(p.name for p in (REPO_ROOT / directory).glob(f"*{suffix}"))
                self.assertEqual(sorted(entries.get(directory, [])), actual, f"{readme} tree is out of date for {directory}/")


class StudyWorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.workspace = read("references/study-workspace.md")

    def template(self, name):
        pattern = rf"^## `{re.escape(name)}` template\n\n```markdown\n(.*?)\n```$"
        match = re.search(pattern, self.workspace, re.MULTILINE | re.DOTALL)
        self.assertIsNotNone(match, f"Missing {name} template")
        return match.group(1)

    def test_status_values_are_defined_once_and_used_consistently(self):
        line = re.search(r"^Status values: (.+)$", self.workspace, re.MULTILINE).group(1)
        self.assertEqual(re.findall(r"`([^`]+)`", line), STATUS_VALUES)
        progress_tables = [self.template("progress.md"), read("evals/fixtures/workspace-progress.md")]
        for table in progress_tables:
            for status in re.findall(r"^\| [A-Z]\d+\.\d+ \| ([^|]+?) \|", table, re.MULTILINE):
                self.assertIn(status, STATUS_VALUES)
        for path in [REPO_ROOT / "SKILL.md", *sorted((REPO_ROOT / "references").glob("*.md"))]:
            for token in re.findall(r"`([^`\n]+)`", path.read_text(encoding="utf-8")):
                self.assertNotIn(token.lower(), STATUS_VARIANTS, f"{path.name}: use one of {STATUS_VALUES}, not `{token}`")

    def test_agent_instructions_work_outside_the_skill_folder(self):
        agents = self.template("AGENTS.md")
        self.assertNotIn("references/", agents, "AGENTS.md is copied into the learner's folder, which has no references/")
        for name in ("teaching-outline.md", "progress.md"):
            self.assertIn(name, agents)
        self.assertEqual(self.template("CLAUDE.md").strip(), "@AGENTS.md")


class LinkTests(unittest.TestCase):
    def test_relative_links_and_anchors_resolve(self):
        documents = ["README.md", "README.zh-CN.md", "CONTRIBUTING.md", "CHANGELOG.md", "SKILL.md", "evals/README.md"]
        documents += [f"references/{p.name}" for p in sorted((REPO_ROOT / "references").glob("*.md"))]
        for relative in documents:
            source = REPO_ROOT / relative
            for target in re.findall(r"\]\(([^)\s]+)\)", without_code_blocks(read(relative))):
                if re.match(r"[a-z]+:", target):
                    continue
                path, _, anchor = target.partition("#")
                linked = (source.parent / path).resolve() if path else source
                self.assertTrue(linked.exists(), f"{relative}: broken link {target}")
                if anchor:
                    self.assertIn(anchor, slugs(linked.read_text(encoding="utf-8")), f"{relative}: missing anchor {target}")


class ReadmeParityTests(unittest.TestCase):
    def test_both_readmes_have_the_same_structure(self):
        english, chinese = read("README.md"), read("README.zh-CN.md")
        levels = [re.findall(r"^(#{1,6}) ", without_code_blocks(text), re.MULTILINE) for text in (english, chinese)]
        self.assertEqual(levels[0], levels[1], "README headings differ in number or level")
        blocks = [re.findall(r"^```(\w*)$", text, re.MULTILINE) for text in (english, chinese)]
        self.assertEqual(blocks[0], blocks[1], "README code blocks differ")


class FixtureTests(unittest.TestCase):
    def test_fixtures_are_marked_synthetic_and_used(self):
        cases = json.loads(read("evals/cases.json"))
        used = {resource for case in cases for resource in case["resources"]}
        for path in sorted((REPO_ROOT / "evals" / "fixtures").iterdir()):
            text = path.read_text(encoding="utf-8")
            self.assertRegex(text, r"(?i)synthetic", f"{path.name} must say it is synthetic")
            self.assertIn("MIT", text, f"{path.name} must state its license")
            self.assertIn(f"fixtures/{path.name}", used, f"{path.name} is not used by any case")


if __name__ == "__main__":
    unittest.main()

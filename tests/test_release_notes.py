"""Check changelog structure and the release notes the release workflow publishes."""

from pathlib import Path
import re
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from release_notes import extract
from validate_skill import REPO_ROOT

SAMPLE = """# Changelog

## Unreleased

- Pending change.

## v0.3.0

### Added

- New feature.

## v0.3

- Older entry.
"""


class ReleaseNotesTests(unittest.TestCase):
    def test_section_includes_subheadings_and_stops_at_next_version(self):
        self.assertEqual(extract(SAMPLE, "v0.3.0"), "### Added\n\n- New feature.\n")

    def test_tag_must_match_the_whole_heading(self):
        self.assertEqual(extract(SAMPLE, "v0.3"), "- Older entry.\n")
        with self.assertRaisesRegex(ValueError, "v0.3.1"):
            extract(SAMPLE, "v0.3.1")

    def test_empty_section_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "v1.0.0"):
            extract("## v1.0.0\n\n## v0.9.0\n- Entry.\n", "v1.0.0")

    def test_windows_line_endings_are_read_correctly(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "CHANGELOG.md"
            path.write_bytes(SAMPLE.replace("\n", "\r\n").encode("utf-8"))
            self.assertEqual(extract(path.read_text(encoding="utf-8"), "v0.3.0"), "### Added\n\n- New feature.\n")


class ChangelogTests(unittest.TestCase):
    def test_versions_are_unique_descending_and_have_notes(self):
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        headings = re.findall(r"^## (.+?)\s*$", changelog, re.MULTILINE)
        if headings and headings[0] == "Unreleased":
            headings = headings[1:]
        self.assertTrue(headings, "CHANGELOG.md has no released versions")
        versions = []
        for heading in headings:
            self.assertRegex(heading, r"^v\d+\.\d+\.\d+$", "Only the first section may be Unreleased")
            versions.append(tuple(int(part) for part in heading[1:].split(".")))
            self.assertTrue(extract(changelog, heading).strip())
        self.assertEqual(versions, sorted(set(versions), reverse=True), "Versions must be unique and newest first")


if __name__ == "__main__":
    unittest.main()

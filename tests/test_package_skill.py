"""Exercise packaging boundaries and broken-bundle failures without an API key."""

from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from zipfile import ZipFile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from package_skill import build
from validate_skill import REPO_ROOT, SKILL_NAME, runtime_paths, validate


class SkillBundleTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        self.root = self.directory / "repo"
        for relative in runtime_paths(REPO_ROOT):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPO_ROOT / relative, target)

    def test_archive_extracts_as_a_usable_skill_and_excludes_local_files(self):
        for name in (".env", "student-notes.md", "course.pdf", ".git/config"):
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("not a runtime file", encoding="utf-8")
        output = build(self.root, self.directory / "bundle.zip")
        extracted = self.directory / "installed"
        with ZipFile(output) as archive:
            names = archive.namelist()
            self.assertEqual(len(names), len(validate(self.root)))
            self.assertTrue(all(n.startswith(SKILL_NAME + "/") for n in names))
            self.assertFalse(any(".." in Path(n).parts for n in names))
            archive.extractall(extracted)
        self.assertEqual(len(validate(extracted / SKILL_NAME)), len(names))
        self.assertFalse((extracted / SKILL_NAME / ".env").exists())
        self.assertFalse((extracted / SKILL_NAME / "student-notes.md").exists())

    def test_repeated_builds_and_checkout_line_endings_do_not_change_bytes(self):
        first = build(self.root, self.directory / "first.zip").read_bytes()
        for relative in runtime_paths(self.root):
            path = self.root / relative
            path.write_bytes(path.read_text(encoding="utf-8").replace("\n", "\r\n").encode("utf-8"))
        second = build(self.root, self.directory / "second.zip").read_bytes()
        self.assertEqual(first, second)

    def test_broken_reference_cannot_replace_an_existing_archive(self):
        output = build(self.root, self.directory / "bundle.zip")
        original = output.read_bytes()
        with (self.root / "SKILL.md").open("a", encoding="utf-8") as handle:
            handle.write("\nRead `references/missing.md`.\n")
        with self.assertRaisesRegex(ValueError, "missing.md"):
            build(self.root, output)
        self.assertEqual(output.read_bytes(), original)

    def test_missing_license_is_rejected(self):
        (self.root / "LICENSE").unlink()
        with self.assertRaisesRegex(ValueError, "LICENSE"):
            validate(self.root)

    def test_malformed_yaml_is_rejected(self):
        (self.root / "SKILL.md").write_text("---\nname: [unclosed\n---\nInstructions\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Invalid YAML"):
            validate(self.root)

    def test_wrong_skill_identity_is_rejected(self):
        path = self.root / "SKILL.md"
        path.write_text(path.read_text(encoding="utf-8").replace(SKILL_NAME, "wrong-name", 1), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Skill name"):
            validate(self.root)

    def test_empty_reference_directory_is_rejected(self):
        for path in (self.root / "references").glob("*.md"):
            path.unlink()
        with self.assertRaisesRegex(ValueError, "no Markdown"):
            validate(self.root)

    def test_invalid_ui_metadata_is_rejected(self):
        (self.root / "agents/openai.yaml").write_text("interface: []\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "interface mapping"):
            validate(self.root)


if __name__ == "__main__":
    unittest.main()

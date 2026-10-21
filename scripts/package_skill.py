"""Build a reproducible, single-folder Skill ZIP after validation."""

import argparse
import os
from pathlib import Path
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from validate_skill import REPO_ROOT, SKILL_NAME, validate


def build(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    paths = validate(root)
    if output.suffix.lower() != ".zip":
        raise ValueError("Output must have a .zip extension")
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=output.parent, suffix=".tmp", delete=False) as handle:
            temporary = Path(handle.name)
        with ZipFile(temporary, "w", compression=ZIP_DEFLATED) as archive:
            for relative in paths:
                info = ZipInfo(f"{SKILL_NAME}/{relative.as_posix()}", date_time=(1980, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                info.compress_type = ZIP_DEFLATED
                # Normalize Windows checkout line endings for reproducible text.
                content = (root / relative).read_text(encoding="utf-8").encode("utf-8")
                archive.writestr(info, content)
        os.replace(temporary, output)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPO_ROOT)
    parser.add_argument("--output", type=Path, default=REPO_ROOT / "dist" / f"{SKILL_NAME}.zip")
    args = parser.parse_args()
    try:
        output = build(args.root, args.output)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Packaging failed: {error}\n")
    print(f"Created {output}")


if __name__ == "__main__":
    main()

"""Print self-contained teaching evaluation inputs, keeping rubrics separate."""

import argparse
import json
from pathlib import Path
import re

EVAL_ROOT = Path(__file__).resolve().parents[1] / "evals"


def load_cases():
    cases = json.loads((EVAL_ROOT / "cases.json").read_text(encoding="utf-8"))
    if not isinstance(cases, list) or not cases:
        raise ValueError("cases.json must contain a nonempty list")
    seen = set()
    for case in cases:
        if not isinstance(case, dict):
            raise ValueError("Every case must be an object")
        identifier = case.get("id", "")
        if not isinstance(identifier, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", identifier):
            raise ValueError("Case IDs must use lowercase words separated by hyphens")
        if identifier in seen:
            raise ValueError(f"Duplicate case ID: {identifier}")
        seen.add(identifier)
        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            raise ValueError(f"{identifier}: missing prompt")
        if not isinstance(case.get("checks"), list) or not case["checks"]:
            raise ValueError(f"{identifier}: missing checks")
        if any(not isinstance(c, str) or not c.strip() for c in case["checks"]):
            raise ValueError(f"{identifier}: checks must be nonempty strings")
        if not isinstance(case.get("resources"), list):
            raise ValueError(f"{identifier}: resources must be a list")
        for resource in case["resources"]:
            if not isinstance(resource, str):
                raise ValueError(f"{identifier}: resource paths must be strings")
            path = (EVAL_ROOT / resource).resolve()
            if not path.is_relative_to(EVAL_ROOT.resolve()) or not path.is_file():
                raise ValueError(f"{identifier}: invalid resource {resource}")
    return cases


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    options = parser.add_mutually_exclusive_group(required=True)
    options.add_argument("--check", action="store_true")
    options.add_argument("--list", action="store_true")
    options.add_argument("--case")
    parser.add_argument("--rubric", action="store_true", help="Print checks instead of learner input")
    args = parser.parse_args()
    try:
        cases = load_cases()
    except (OSError, ValueError) as error:
        parser.exit(1, f"Fixture validation failed: {error}\n")
    if args.check:
        print(f"Validated {len(cases)} case definitions; no model responses were evaluated.")
    elif args.list:
        print("\n".join(case["id"] for case in cases))
    else:
        case = next((case for case in cases if case["id"] == args.case), None)
        if case is None:
            parser.error(f"Unknown case: {args.case}")
        if args.rubric:
            print("\n".join(f"- {check}" for check in case["checks"]))
        else:
            print("Use $a-real-teacher-from-your-slide for this request.\n")
            for resource in case["resources"]:
                print(f"Source: {Path(resource).name}")
                print((EVAL_ROOT / resource).read_text(encoding="utf-8"))
            print("User request:")
            print(case["prompt"])


if __name__ == "__main__":
    main()

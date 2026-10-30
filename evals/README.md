# Teaching behavior evaluations

These are small, synthetic learning tasks for checking Skill changes. They contain no university course files, student submissions, or personal data. The repository's MIT license applies to the fixtures.

The cases cover local-step teaching, explicit answer preferences, conflicting source evidence, attempt diagnosis, one-question recall, incomplete scans, mock-exam marks, unsupported exam predictions, creating or resuming a study workspace, and planning or converting large material sets. They are a starting point for regression evaluation, not a benchmark of learning outcomes or evidence of adoption.

## Run a case

Use Python 3.10 or newer; the helper needs only the standard library.

```sh
python scripts/eval_case.py --check
python scripts/eval_case.py --list
python scripts/eval_case.py --case practice-explicit-answers
```

1. Install or load the Skill version being evaluated. Record the exact Git commit and any other system instructions that affect teaching.
2. Start a fresh conversation and supply the printed input, including the complete source texts. Do not give the assistant the rubric or previous responses.
3. Save its actual response before reviewing it. Keep follow-up turns for a separate run so they do not hide a first-response failure.
4. Print the rubric separately and score each check as pass, fail, or unverified. Inspect mathematical answers by substitution, including intermediate operations; add marks independently for quiz cases.
5. Record the date, model identifier if available, host, commit, case ID, response, check results, and limitations. Mark unexecuted cases as not run. Repeat relevant cases when a change affects them, using the same model and host for comparisons when possible.

```sh
python scripts/eval_case.py --case practice-explicit-answers --rubric
```

`--check` validates case definitions and resource paths. It does not call a model or grade teaching. Structural validation and packaging tests must not be reported as behavioral pass rates. Outputs can vary between runs, so preserve actual transcripts and report the number of runs.

## Result template

```text
Date and timezone:
Skill commit:
Host and model (or unknown):
Case ID and run number:
Actual response or transcript location:
Each rubric check: pass / fail / unverified, with supporting response excerpt
Independent calculation or marks check:
Limitations / cases not run:
```

Keep private transcripts outside the public repository. Before publishing an example, remove identifying details and replace course content with a synthetic example you may share. Real student feedback should remain separate from synthetic evaluation results.

# Contributing

Small improvements backed by a concrete learning problem are welcome. Explain what a student asked, what happened, and what should improve. Reports and discussion can be in English or Chinese.

## Propose a change

- Keep shared behavior in `SKILL.md` and mode-specific detail in the relevant `references/` file.
- Preserve the Skill name `a-real-teacher-from-your-slide` and keep referenced files available.
- Reuse the learner's explicit choices and course notation. Use a small example to explain a proposed teaching change.
- Update both READMEs when changing public setup or usage instructions.
- Keep independent changes in separate PRs and describe the student-visible behavior and checks performed.

## Verify teaching changes

Use the synthetic cases in [evals/README.md](evals/README.md). Run the affected case in a fresh conversation and inspect the actual output, including calculations, source claims, answer placement, and whether the assistant waits when requested. Report unexecuted checks clearly.

```sh
python scripts/eval_case.py --check
python scripts/eval_case.py --case attempt-first-error
```

Add a small, shareable case when fixing a behavior not yet represented. Keep evaluation inputs separate from expected outcomes so the assistant is not coached with the rubric.

## Share feedback responsibly

Use the learning-feedback issue template. Describe what helped as well as what was confusing, without inventing outcome measurements. You can report that a classmate used the Skill without naming them. Get permission before publishing another person's words, and avoid student IDs, grades, private conversations, assessment answers, and copyrighted handouts. A short synthetic reproduction is usually enough to investigate a problem.

The maintainer reviews and merges PRs; opening a PR does not change the installed Skill or publish a release. This project remains a learning aid, and contributors should follow applicable course rules.

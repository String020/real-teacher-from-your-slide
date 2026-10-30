# Changelog

## Unreleased

- Added parallel material intake for many or long resources: a quick survey that keeps each file's own structure, conversion with a local tool such as MarkItDown into `materials/` with an index, subagent reading tasks with a self-contained brief, a merge step that assigns knowledge point IDs, and on-demand transcription of scanned pages, formulas, and diagrams.
- Mock exams, and practice when verified answers are requested, can be solved independently by a subagent before delivery.

## v0.2.0

### Study workspace

- Added a study workspace: `teaching-outline.md`, `progress.md`, and `AGENTS.md` / `CLAUDE.md` templates with evidence-based update rules, so agents can resume learning across conversations.
- Attempt Diagnosis, Active Recall, Practice Generator, Mock Exam, and Exam Outline now read and update the workspace files. Active Recall reviews `needs review` and least recently practised points first.
- Conversations in a folder with workspace files resume from the recorded next step instead of the full mode menu.

### Teaching flow

- Explicit choices for language, practice format, and answer placement are reused instead of asked again, and concrete requests are routed directly without the mode menu.
- Foundation Guides no longer include answers by default; answer handling is consistent across modes.
- The Foundation Path names Practice Generator (foundation drills) instead of a nonexistent Basic Practice mode.
- The Skill description lists the supported resources, modes, and example requests so hosts can trigger it more reliably.

### Source evidence

- Multi-source work records actual file and page, slide, or section locators and separates explicit course statements from observations in sample questions.
- Resource conflicts are resolved by the authority relevant to each claim.
- Mock exams are checked for solvability, answers, and marks before delivery.

### Packaging and evaluation

- Added a validator and a reproducible Skill ZIP packager with Windows and Linux CI.
- Added a release workflow that attaches the validated ZIP to a GitHub Release when a version tag is pushed.
- Added ten synthetic teaching evaluation cases, a helper that prints inputs separately from rubrics, contributor guidance, and a bilingual learning-feedback template.

## v0.1.0

- Initial public release.
- Added course-resource-grounded learning workflow.
- Added mode router with Foundation Path and Exam Revision Path.
- Added knowledge outline, exam outline, foundation guide, exam strategy pack, problem tutor, attempt diagnosis, practice generator, mock exam, active recall, and exam compression modes.
- Added artifact quality rules for Markdown, PDF, and slides.
- Added source grounding, academic integrity, and example workflow references.

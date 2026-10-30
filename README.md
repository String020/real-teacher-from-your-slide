# A Real Teacher From Your Slide

[English](README.md) | [中文](README.zh-CN.md)

A Real Teacher From Your Slide is a course-resource-grounded learning Skill that turns user-uploaded study materials into teaching, exam review, practice, mock exams, and polished study artifacts.

It is designed for courses where students learn from lecture slides, notes, problem sheets, solutions, formula sheets, sample exams, past exams, revision guides, and instructor-provided scope documents.

The GitHub repository name is `real-teacher-from-your-slide`. The Skill package/frontmatter name is `a-real-teacher-from-your-slide`.

## Design Philosophy

1. Teach from user-uploaded resources, not generic assumptions.
2. Build understanding before compressing for exams.
3. Use problems to reveal weak points.
4. Keep artifact generation user-controlled.
5. Preserve source grounding without damaging readability.

## Quick Start

1. Upload course resources.
2. Choose either Foundation Path or Exam Revision Path, or select a single mode directly.
3. Choose the output format: chat, Markdown, PDF, slides, formula sheet, practice pack, or mock exam.
4. For long artifacts, review the outline before generation.
5. Use tutoring, diagnosis, practice, mock exams, active recall, and exam compression as needed.

## Installation / Usage

This repository is platform-agnostic. Use it in any environment that can read a Skill-style instruction bundle or a structured prompt workflow.

### Build the Skill bundle

With Git and Python 3.10 or newer installed, run these commands in a terminal (PowerShell or Bash):

```sh
git clone https://github.com/String020/real-teacher-from-your-slide.git
cd real-teacher-from-your-slide
python -m pip install -r requirements-dev.txt
python scripts/validate_skill.py
python scripts/package_skill.py
```

This creates `dist/a-real-teacher-from-your-slide.zip`. The archive has one top-level folder named `a-real-teacher-from-your-slide`, containing `SKILL.md`, the reference files, UI metadata, and the MIT license. Repository history, development tools, and files outside these runtime locations are excluded. Keep private course materials outside the repository's `references/` directory.

### Local Codex setup

Extract the ZIP's `a-real-teacher-from-your-slide` folder into your chosen local Skill directory. The final path must look like `.agents/skills/a-real-teacher-from-your-slide/SKILL.md`, not an extra nested copy of that folder. For a user-level install, the parent is `~/.agents/skills` (on Windows, `%USERPROFILE%\.agents\skills`). A project-level install uses that project's `.agents/skills` directory.

These paths follow the [official local Skill documentation](https://learn.chatgpt.com/docs/build-skills). If a host or organization configures a different Skill location, use that location. Codex should detect the Skill; restart if it does not appear.

Start with:

```text
Use $a-real-teacher-from-your-slide to explain the attached course notes.
Start with one worked example, then ask me one check question.
```

To update, build the new bundle and replace the installed Skill folder after preserving any personal modifications. To uninstall, remove only that Skill folder. Other Skill-enabled hosts can read the same instruction bundle, but their installation steps and file-generation tools differ. This ZIP is a local Skill bundle, not a marketplace plugin.

### Check a change

```sh
python scripts/validate_skill.py
python -m unittest discover -s tests -v
python scripts/package_skill.py
```

The validator checks the manifest, runtime files, UI metadata structure, and reference targets. The tests also exercise extraction, excluded local files, broken inputs, and reproducible packaging. They do not measure teaching quality or prove host compatibility. GitHub Actions runs these checks on Windows and Linux and provides the ZIP as a workflow artifact; it does not publish a release automatically.

If your environment cannot generate PDFs, slides, or other files directly, ask the assistant to produce clean Markdown or a generation-ready outline instead.

## What to Upload First

Useful resources include:

- lecture slides or notes
- syllabus or weekly outline
- problem sheets or tutorial questions
- applied class materials
- solutions or marking guides
- formula sheets
- sample exams or mock exams
- past exams
- revision guides or instructor-provided exam scope

The Skill works best when course-content resources and question/exam resources are both available.

## Learning Paths

### Foundation Path

For users with weak foundations or who need to learn from the beginning.

Recommended flow:

`Knowledge Outline -> Foundation Guide -> Problem Tutor -> Basic Practice -> Exam Outline -> Exam Strategy Pack -> Attempt Diagnosis -> Mock Exam -> Active Recall -> Exam Compression`

### Exam Revision Path

For users who have already studied the course and mainly need exam preparation.

Recommended flow:

`Exam Outline -> Exam Strategy Pack -> Problem Tutor -> Attempt Diagnosis -> Practice Generator -> Mock Exam -> Active Recall -> Exam Compression`

These paths are recommendations only. Users can start from any mode, skip steps, repeat steps, or combine modes.

## Supported Modes

- **Knowledge Outline**: map course structure, modules, prerequisites, and learning order.
- **Exam Outline**: map exam-facing topics, problem types, formulas, and common loss points.
- **Foundation Guide**: create textbook-style learning material with intuition, definitions, formula origins, examples, mistakes, and practice.
- **Exam Strategy Pack**: create exam-ready templates, formula usage conditions, problem-type entry tables, and quick-reference material.
- **Problem Tutor**: teach through one problem by reviewing related knowledge before solving.
- **Attempt Diagnosis**: diagnose a user's own solution attempt before giving the corrected solution.
- **Practice Generator**: generate targeted practice by module, difficulty, style, and answer format.
- **Mock Exam**: generate exam-like tests based on selected scope and optional sample-exam style.
- **Active Recall**: run one-question-at-a-time recall for formulas, definitions, methods, and mistakes.
- **Exam Compression**: produce final review checklists, formula conditions, entry tables, and common mistakes.

## Artifact Generation

The Skill can produce chat output, Markdown, PDF, slides, formula sheets, practice packs, and mock exams when the current environment supports them.

For long PDFs, slide decks, or long Markdown documents, it should first generate a table of contents or structure draft and wait for user confirmation.

PDF outputs should be book-quality study documents, not exported chat logs. They should use LaTeX math environments, readable fonts, clear sectioning, page numbers, tables of contents for long documents, and layout checks for broken formulas, missing glyphs, overlapping text, and clipped equations.

## Study Workspace

When the host can write files, the Skill can keep your learning in your own course folder so a later conversation, or a different agent, can continue where you stopped:

- `teaching-outline.md`: knowledge points with stable IDs, learning goals, prerequisites, and source locators.
- `progress.md`: status of each knowledge point, evidence, weak points, a dated session log, and the next step.
- `AGENTS.md`: instructions that tell agents to read both files at the start of a session and how to update them.
- `CLAUDE.md`: one line, `@AGENTS.md`, for hosts that read `CLAUDE.md`.

The Skill creates these files only when you ask or agree, does not overwrite existing files, and changes a knowledge point's status only after your attempts, answers, or results. You can edit the files yourself at any time.

## Example Prompts

### Study Workspace

- "Create a teaching outline and progress file for this course in this folder, plus AGENTS.md."
- "Continue from my progress file."

### Resource Upload

- "I uploaded my lecture slides and problem sheets. First tell me what these resources can support."
- "Use these course resources to build a Knowledge Outline."

### Foundation Learning

- "Create a Foundation Guide for this module. Make it beginner-friendly."
- "Explain this topic like a textbook, including intuition, formula origins, worked examples, and common mistakes."

### Exam Revision

- "Generate an Exam Outline from these sample exams and problem sheets."
- "Create an Exam Strategy Pack for this topic, but do not assign priority unless the resources support it."

### Problem Tutoring

- "Teach me this problem. Start with the related knowledge, then solve it step by step."
- "I only do not understand this step. Do not re-explain the whole chapter."

### Attempt Diagnosis

- "Here is my solution attempt. Diagnose where I first went wrong."
- "Check my reasoning before giving the standard solution."

### Practice Generation

- "Generate practice questions for this module. Ask me whether I want answers before including them."
- "Create three exam-style variations of the problem I just got wrong."

### Mock Exams

- "Create a module test for these topics. Ask whether to imitate the sample exam style."
- "Generate a half mock exam with marking guidance."

### PDF / Slides / Markdown

- "Turn this module into a textbook-style PDF. Show me the table of contents first."
- "Create a one-page formula sheet in Markdown."
- "Create slides for quick revision, not a detailed textbook guide."

## Source Grounding

Formal artifacts should include source grounding in a separate page or section, such as `Source Basis`, `Resources Used`, or `Material Coverage`. Source notes should improve trust without interrupting the main reading experience.

## Academic Integrity

This project supports learning, revision, practice, diagnosis, and mock exams. It should not be used to bypass course rules, complete live exams, impersonate students, or generate submit-ready answers without learning intent.

## Disclaimer

This project is a learning aid. It is not official instructor material and does not replace course policies, marking guides, instructor guidance, or official assessment instructions. Users are responsible for following academic integrity rules.

## Limitations

- Output quality depends on the quality and completeness of uploaded resources.
- Exam-priority analysis requires exam-like evidence such as sample exams, past exams, problem sheets, or instructor-provided scope.
- Artifact generation depends on the tools available in the current environment.
- The Skill does not include user course files.

## For Developers / Skill Maintainers

Repository structure:

```text
real-teacher-from-your-slide/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── CHANGELOG.md
├── .gitignore
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── mode-router.md
    ├── material-intake.md
    ├── knowledge-outline.md
    ├── exam-outline.md
    ├── foundation-guide.md
    ├── exam-strategy-pack.md
    ├── problem-tutor.md
    ├── attempt-diagnosis.md
    ├── practice-generator.md
    ├── mock-exam.md
    ├── active-recall.md
    ├── exam-compression.md
    ├── artifact-quality.md
    ├── source-grounding.md
    ├── example-workflows.md
    └── academic-integrity.md
```

`SKILL.md` is the main entrypoint. Detailed behavior rules live in `references/` so each mode can be updated independently.

## License

MIT License. See [LICENSE](LICENSE).

## Feedback and Contributions

Share a concrete learning problem or useful experience through the learning-feedback issue template. English and Chinese feedback are welcome. Use synthetic examples rather than private course files or student information. See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidance and [evals/README.md](evals/README.md) for reproducible teaching checks.

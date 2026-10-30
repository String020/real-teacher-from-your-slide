# Study Workspace

Use this file when the user wants learning to continue across conversations through files in their own folder: a teaching outline of knowledge points, a progress record, and an agent instruction file that tells any agent opening the folder to read and maintain them.

## When to use

- The user asks to create, save, track, or continue a teaching outline, progress file, `AGENTS.md`, or `CLAUDE.md`.
- The user asks to "continue from last time" and the folder already contains these files.
- A multi-session course workflow is starting and the host can write files. Offer the workspace once in one line; create files only after the user agrees.

Do not create workspace files for a single problem, a local step, or when the host cannot write files. Without write access, offer the file contents in chat for the user to save.

## Files

Create these at the root of the folder the user names, or the authorized folder that holds the course materials. Ask only when no folder is clear.

| File | Purpose | Main writer |
|---|---|---|
| `teaching-outline.md` | Knowledge points to teach, with stable IDs, goals, prerequisites, and source locators | Agent, after the user accepts the outline scope |
| `progress.md` | Status of each knowledge point, evidence, weak points, session log, and next step | Agent, after learning evidence; the user may edit it |
| `AGENTS.md` | Instructions that tell agents how to read and maintain the two files | Agent once; the user owns later changes |
| `CLAUDE.md` | A one-line import of `AGENTS.md` for hosts that read `CLAUDE.md` | Agent once |
| `materials/` | Converted Markdown of the course files and `materials/index.md`, created only when resources are converted | Agent; see `references/parallel-intake.md` |

Create both `AGENTS.md` and `CLAUDE.md` by default so the folder works in hosts that read either file. If the user chooses only one, create that one and put the full instructions in it.

Before writing, check whether each file exists:

- `teaching-outline.md` or `progress.md` exists: read it and continue from it. Do not replace it with a new template.
- `AGENTS.md` or `CLAUDE.md` exists: keep its content. Show the user the section to append under the heading `## Study workspace`, and append it after they agree. If `CLAUDE.md` already imports `AGENTS.md`, leave it unchanged.

## Creation workflow

1. Inspect the available course resources and agree on the course scope, language style, and folder, reusing choices already given.
2. Draft the knowledge points with the rules in `references/knowledge-outline.md`, at the granularity of one teachable idea, method, or definition per point. For a large course, show the module list first and fill modules in after confirmation. For many or long resources, survey, convert, and split them with `references/parallel-intake.md`.
3. Write `teaching-outline.md`, then `progress.md` with every point set to `not started`, then the agent instruction files.
4. Report the files created or changed in one or two lines. Do not paste their full contents into chat unless asked.

Write file content in the session's language style. Keep the field labels below so later agents can find them, translated only if the user asks.

## `teaching-outline.md` template

```markdown
# Teaching Outline: <course or module>

Scope: <resources and modules covered>
Last updated: <YYYY-MM-DD>

## M1 <module name>

| ID | Knowledge point | Learning goal | Prerequisites | Source |
|---|---|---|---|---|
| M1.1 | <point> | <what the learner should be able to do> | <IDs or "none"> | <file, page/slide/section> |

## Out of scope or unsupported

- <points excluded by the current scope, or requested but missing from the resources>

## Missing materials

- <what cannot be determined from the current resources>
```

Outline rules:

- Give every knowledge point a stable ID. Never renumber existing IDs; add new points with new IDs.
- When scope changes, move a point to `Out of scope or unsupported` rather than deleting it if `progress.md` refers to it.
- Use real locators only. Leave the source as `not found in resources` rather than inventing one, and mark supplementary prerequisites as `supplementary`.
- Do not assign exam priority here. If the user wants it, add an `Exam relevance` column only with evidence from Exam Outline and cite that evidence.

## `progress.md` template

```markdown
# Learning Progress: <course or module>

Last updated: <YYYY-MM-DD>
Path: <Foundation Path / Exam Revision Path / direct modes>
Language and format: <chosen language style and preferred output>

## Next step

<one concrete next action, such as "Problem Tutor on M1.2 using Problem Sheet 2 Q3">

## Knowledge point status

| ID | Status | Evidence | Last practiced |
|---|---|---|---|
| M1.1 | not started | | |

Status values: `not started`, `learning`, `needs review`, `mastered`.

## Weak points and misconceptions

- <ID>: <specific error and the correction that worked>

## Session log

- <YYYY-MM-DD>: <modes used, points covered, outcome>
```

Progress rules:

- Change a status only on evidence from the learner: an attempt, a recall answer, a diagnosed solution, or a mock-exam result. Being taught a point moves it to `learning` at most.
- Mark `mastered` only after the learner applies the point correctly without hints, preferably more than once or in a later session. Return it to `needs review` after a later error.
- Record the learner's own assessment as `self-reported` in the evidence column; it does not count as `mastered` alone.
- Write absolute dates. Add one session log entry per session and keep earlier entries.
- Keep evidence short: the question or task and the outcome. Do not store full solutions to assessed work, grades, student IDs, or long copies of course materials.
- Update `Next step` at the end of each session so the next agent knows where to start.
- Tell the user in one line what changed in `progress.md`. If they disagree, follow their correction.

## Updates by mode

Each mode file describes its own workspace step. In short:

| Mode | Reads | Writes |
|---|---|---|
| Knowledge Outline | resources | `teaching-outline.md` points and IDs |
| Exam Outline | `teaching-outline.md`, exam-like evidence | `Exam relevance` column, only with evidence |
| Attempt Diagnosis | point ID of the attempt | status, first key error under weak points |
| Active Recall | statuses and `Last practiced` to choose questions | evidence, `Last practiced`, status after the round |
| Practice Generator | `needs review` points and weak points to choose topics | nothing until the user attempts the questions |
| Mock Exam | outline IDs for the question mapping | per-ID results and statuses after marking |
| Any mode, end of session | `progress.md` | session log entry and `Next step` |

## `AGENTS.md` template

```markdown
# Study workspace instructions

This folder is a study workspace for <course or module>. Teach from the course materials in this folder. If the a-real-teacher-from-your-slide Skill is available, use it.

## At the start of each session

1. Read `teaching-outline.md` and `progress.md` before teaching.
2. Tell the learner in two or three lines where they are and propose the `Next step` from `progress.md`. Follow the learner if they choose something else.
3. Reuse the path, language style, and format recorded in `progress.md` unless the learner changes them.

## While teaching

- Teach knowledge points in the order and scope of `teaching-outline.md`. Check prerequisites marked `needs review` or `not started` before relying on them.
- Use the IDs from `teaching-outline.md` when referring to knowledge points.
- For review, recall, or practice without a named topic, start from points marked `needs review` and the recorded weak points, then `learning` points practised longest ago.
- If `materials/index.md` exists, read the converted files in `materials/` before reopening the originals. Check formulas, diagrams, and pages marked for visual checking against the original file.

## Updating `progress.md`

- Change a status only after evidence from the learner: an attempt, a recall answer, a diagnosed solution, or a mock-exam result. Teaching a point moves it to `learning` at most.
- Mark `mastered` only after correct, unaided application. Return a point to `needs review` after a later error.
- Record self-assessment as `self-reported`. Add weak points with the specific error.
- At the end of a session, add a dated session log entry and update `Next step`.
- Tell the learner in one line what changed.

## Updating `teaching-outline.md`

- Update it when new materials or a new scope arrive, and say what changed.
- Keep existing IDs. Add new points with new IDs and move removed points to `Out of scope or unsupported`.
- Use real source locators only.

## Boundaries

- Do not edit these instructions unless the learner asks.
- Follow course academic integrity rules. Do not store solutions to live or assessed work.
```

## `CLAUDE.md` template

```markdown
@AGENTS.md
```

Hosts that read `CLAUDE.md` and support `@` imports load `AGENTS.md` from this line. If the host does not support imports, or the user asked for `CLAUDE.md` only, write the full `AGENTS.md` instructions into `CLAUDE.md` instead.

## Resuming a session

When a conversation starts in a folder with these files, read them before broad routing. Summarize the current position briefly and offer the recorded next step instead of the full mode menu. If the files conflict with each other or with new resources, describe the conflict and ask only about the affected points.

# Parallel Material Intake

Use this file when a course-level task, such as a Knowledge Outline or a study workspace, depends on many or long resources. It covers surveying the materials, converting them to text with a local tool, splitting the reading across subagents, and merging the results.

## When to use

- Consider it when the resources exceed about 3 files or 50 pages in total. Below that, read them directly.
- Before starting subagents or a conversion tool, tell the user in one line what will run and why. Start after they agree, or proceed directly if they already asked for it.
- If the host has no subagent tool, process the same units one at a time, summarizing each before the next. If it cannot run local commands, read the files directly.

## 1. Survey

Make a quick pass before splitting any work. Read only filenames, page or slide counts, tables of contents or bookmarks, the first page or two, and any syllabus.

For each file, record:

- its role, using the categories in `references/material-intake.md`;
- its own organization: week, lecture, chapter, unit, topic, question, or none;
- its locator type: slide, page, section, or question.

Do not assume the course is organized by weeks. Keep each file's own structure, and identify meaningless filenames such as `scan001.pdf` from their first page.

## 2. Convert with a local tool

If the host can run local commands and a converter such as MarkItDown is installed, convert files with it instead of retyping their content. Tool output costs no model output tokens. Do not install software without the user's permission.

```sh
markitdown lecture-03.pdf -o materials/lecture-03.md
```

Behavior observed with MarkItDown 0.1.8:

- **PPTX**: keeps `<!-- Slide number: N -->` markers, tables, and speaker notes under `### Notes:`.
- **PDF**: adds no page markers; pages are separated by form feed characters. A page without a text layer, such as a scanned page or an image-only slide, becomes empty without any warning. Split on form feeds, insert `<!-- Page N -->` markers, check that the page count matches the original, and mark empty pages `no text layer`.
- **Math, diagrams, and layout** are not reliable. Formulas from typeset PDFs may come out garbled, and arrows or chart details are lost. Check formulas against the original page before teaching them.
- Underscores may be escaped as `\_`; this is formatting, not lost content.

Save converted text as `materials/<original file name>.md` in the study workspace, keeping the original name. Without a converter, read the originals directly and keep the same locators.

## 3. Split the work

| Material | Unit of work |
|---|---|
| Small file | the whole file |
| Large file with a table of contents, bookmarks, or headings | its own chapters, lectures, or sections |
| Large file without structure | ranges of about 30 pages, cut at a heading or paragraph break |
| Exam paper or problem sheet | questions or question groups |

Process course content (slides, notes, textbooks) first. Map exam-like resources to knowledge points in a second pass, after the outline exists.

## 4. Subagent tasks

Give each subagent one unit and a self-contained brief, because it cannot see this conversation. If the host lets you choose a model, use a cheaper or faster model for these reading tasks and keep merging and teaching on the main model.

```text
Read <file>, <locator range>. The course is <course>; this file is <role>, organized by <organization>.
Return, without rewriting the source text:
1. Knowledge points: name, one-line learning goal, prerequisites if stated, and exact locators.
2. Locators that need visual checking: no text layer, garbled formulas, or diagrams needed for understanding.
3. Whether the first or last topic continues from the previous unit or into the next one.
4. Statements that seem to conflict with other course material, with locators.
Use only real locators. Mark unreadable parts instead of guessing their content.
Do not write files unless this brief names a materials file for you to write.
```

Each subagent writes at most the one materials file its brief names. Only the main agent writes `teaching-outline.md`, `progress.md`, and `materials/index.md`.

## 5. Merge

1. Combine the returned knowledge points and remove duplicates, keeping every locator.
2. Join topics that span unit boundaries using the continuation notes.
3. Group points into modules by the course's own structure from the survey. When files are organized differently, follow the syllabus or current lecture materials and list the other files as sources. When no structure exists, group by topic and prerequisite.
4. Assign knowledge point IDs during the merge, not during the split.
5. Resolve conflicts with `references/source-grounding.md`.
6. Write `teaching-outline.md` and `materials/index.md`. Then run the second pass that maps exam-like questions to knowledge point IDs as evidence for `Exam relevance`.

## 6. Transcribe on demand

Spend model output only on content the converter could not handle: pages without a text layer, garbled formulas, and diagrams that matter for understanding. Transcribe them when their module is taught or the user asks, not all at once.

- Skip cover pages, administrative slides, and repeated headers or footers.
- Describe a diagram in one line unless its details are needed for the lesson.
- Write formulas in LaTeX and keep the original locator.
- Update `materials/index.md` when pages are transcribed.

## 7. Spot-check

For math-heavy or scanned material, compare a few converted or transcribed pages with the original, prioritizing formulas and symbols. Record what was checked in `materials/index.md`, and say which pages were not checked.

## `materials/index.md` template

```markdown
# Materials Index

Last updated: <YYYY-MM-DD>

| File | Role | Organization | Locator | Size | Converted | Needs visual check | Spot-checked |
|---|---|---|---|---|---|---|---|
| <original file name> | <role> | <week / lecture / chapter / topic / none> | <slide / page / section / question> | <pages or slides> | <tool and date, or "read directly"> | <locators, or "none"> | <locators, or "not checked"> |
```

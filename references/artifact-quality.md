# Artifact Quality

Use this file when generating Markdown, PDF, slides, formula sheets, practice packs, or mock exams.

## Output control

Do not default to artifacts. Let the user choose chat, Markdown, PDF, slides, formula sheet, practice pack, or mock exam.

For long PDFs, long slide decks, or long Markdown documents:

1. Generate a table of contents or structure draft first.
2. Wait for user confirmation.
3. Generate module by module.
4. Combine only after the user confirms the parts are acceptable.

Short artifacts such as one-page formula sheets or small topic notes do not require full TOC confirmation.

## PDF quality checklist

PDFs must be book-quality study documents, not exported chat logs.

Check:

- math uses LaTeX math environments;
- short formulas use inline math;
- important formulas, derivations, matrices, ODEs, limits, Taylor series, and multi-line equations use display math;
- Chinese text, if present, uses clear CJK-capable fonts;
- formulas are not rasterized as screenshots unless unavoidable;
- A4 layout is used unless the user asks otherwise;
- long documents include a title page;
- long documents include a table of contents;
- page numbers are present;
- margins and line spacing are readable;
- section hierarchy is clear;
- tables fit on the page;
- formulas are not clipped;
- glyphs are not missing;
- text does not overlap;
- black boxes or failed render artifacts are absent;
- source notes are visually separate;
- the document looks like a study guide, textbook, or exam pack.

## Markdown quality

Use clear headings, tables only where helpful, readable equations, and consistent section structure. Do not produce a wall of bullets when the user asks for a teaching guide.

## Slides quality

Use slides for quick review, presentation, or staged learning. Do not make slides carry dense textbook paragraphs unless the user asks for a slide-style handout.

## Formula sheets

Formula sheets should include formula, usage condition, trigger phrase, and common mistakes when possible.

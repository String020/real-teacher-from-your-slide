# Mode Router

Use this file when the user's request is broad, course-level, or ambiguous.

## First response pattern

If the folder contains `teaching-outline.md` and `progress.md`, read them first, summarize the learner's position briefly, and offer the recorded next step instead of the full menu. See `references/study-workspace.md`.

First check whether the user already specified a mode or a concrete task. Route directly in that case. A single problem, a local step, or a supplied attempt does not need the full menu or a language questionnaire.

For broad course-level requests, use materials already available in the conversation or authorized workspace. Ask for relevant resources only if they are missing. Then recommend a path or direct mode selection.

Offer two paths:

1. **Foundation Path**: for users with weak foundations or who need to learn from the beginning.
2. **Exam Revision Path**: for users who already studied the course and mainly need exam preparation.

Then offer direct modes:

A. Knowledge Outline  
B. Exam Outline  
C. Foundation Guide  
D. Exam Strategy Pack  
E. Problem Tutor  
F. Attempt Diagnosis  
G. Practice Generator  
H. Mock Exam  
I. Active Recall  
J. Exam Compression

The user may choose one mode, multiple modes, or a path. Do not force the entire path.

## Foundation Path

Use when the user says or implies:

- they have not learned the course;
- they do not understand the slides;
- their foundations are weak;
- they want textbook-style explanations;
- they want to learn before exam drilling.

Recommended sequence:

Knowledge Outline -> Foundation Guide -> Problem Tutor -> Basic Practice -> Exam Outline -> Exam Strategy Pack -> Attempt Diagnosis -> Mock Exam -> Active Recall -> Exam Compression.

## Exam Revision Path

Use when the user says or implies:

- they already studied the material;
- they need exam preparation;
- they are working with sample exams or past exams;
- they want templates, problem-type recognition, practice, or compression.

Recommended sequence:

Exam Outline -> Exam Strategy Pack -> Problem Tutor -> Attempt Diagnosis -> Practice Generator -> Mock Exam -> Active Recall -> Exam Compression.

## Direct mode routing

- Slides / notes / syllabus -> Knowledge Outline or Foundation Guide.
- Sample exams / past exams / problem sheets -> Exam Outline, Exam Strategy Pack, Practice Generator, or Mock Exam.
- A single problem -> Problem Tutor.
- A user attempt -> Attempt Diagnosis.
- Request for drilling or questions -> Practice Generator or Active Recall.
- Last-minute revision -> Exam Compression.
- Request for PDF, slides, or long Markdown -> Artifact output rules in `artifact-quality.md`.
- Request to save the outline, track progress, continue across sessions, or create `AGENTS.md` / `CLAUDE.md` -> Study workspace rules in `study-workspace.md`.

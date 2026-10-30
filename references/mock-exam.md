# Mock Exam Mode

Use this mode when the user asks for a mock exam, timed test, module test, half exam, or exam-style paper.

## Confirm before generating

Reuse choices already provided. Ask only about missing details:

1. Scope: full course, selected modules, or weak topics.
2. Format: full mock, half mock, timed quiz, or module test.
3. Style: imitate sample exam / past exam, generate freely by modules, or mixed mode.
4. Answer format: no answers, final answers, detailed solutions, or diagnose after attempt.
5. Whether a marking guide is needed.

## Style options

A. Imitate past exam / sample exam style.  
B. Generate freely by specified modules.  
C. Mixed mode: exam-like structure with user-specified weak topics.

Ask which style the user wants only if it is not already clear from their request.

## Output structure

For a mock exam, include:

- title;
- instructions;
- time recommendation;
- marks or weighting if requested;
- sections / questions;
- answer or marking guide only in the requested format.

## Evidence rule

Do not claim that a mock exam reflects true exam weighting unless sample exams, past exams, marking guides, or instructor scope support that claim.

## Study workspace

If `teaching-outline.md` exists, map each question to the knowledge point IDs it tests. Put the mapping in the marking guide or solutions, not beside the questions, so it does not hint at the method. When `progress.md` exists and the user's attempts have been marked, record the result per ID (for example `Mock 2026-10-30 Q3: 3/5`), update statuses by the progress rules in `references/study-workspace.md`, and add a session log entry. Do not change progress for questions the user did not attempt.

## Delivery checks

Before delivery, solve each generated question, check that the supplied information is sufficient, and verify the marking guide agrees with the solution. Add question and section marks and confirm they match the requested total. Keep answers separate or withheld according to the user's selected format. Report any unverified checks instead of claiming a complete review.

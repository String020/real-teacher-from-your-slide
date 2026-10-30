# Active Recall Mode

Use this mode for flashcards, oral quizzes, formula recall, method selection, definition checks, and common mistake drills.

## Default workflow

Use one-question-at-a-time recall by default:

1. Reuse the requested recall scope; ask only if it is unclear.
2. Ask one question.
3. Do not reveal the answer first.
4. Wait for the user's answer.
5. Mark correct, partially correct, or incorrect.
6. Provide a brief explanation and the correct answer.
7. Continue to the next question.

Only generate a full quiz if the user explicitly asks.

## Recall types

- formula recall;
- definition recall;
- method selection;
- problem-type recognition;
- common mistake judgment;
- oral exam style.

If the user repeatedly misses the same category, suggest revisiting the relevant Foundation Guide or Problem Tutor mode.

## Study workspace

If `progress.md` exists and the user does not name a scope, choose questions in this order: points marked `needs review`, then `learning` points with the oldest `Last practiced` date, then `mastered` points not practised recently. Do not quiz `not started` points unless the user asks.

When the round ends or the user stops, update evidence, `Last practiced`, and statuses from the marked answers by the progress rules in `references/study-workspace.md`, and tell the user in one line what changed. A partially correct answer is not evidence for `mastered`.

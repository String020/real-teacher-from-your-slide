# Example Workflows

This file provides detailed examples of how to apply the Skill.

## 1. User uploads course resources and asks for a Knowledge Outline

User input: "I uploaded the slides and notes for these modules. Generate a Knowledge Outline."

Assistant should:

1. Identify uploaded resources briefly.
2. Confirm whether the user wants chat, Markdown, or formal artifact if output is long.
3. Ask language style if not already selected.
4. Generate a Knowledge Outline using `knowledge-outline.md`.
5. Include a separate source basis if the output is formal.

Assistant should not immediately generate a PDF unless requested.

## 2. User uploads broad resources and asks for exam revision

User input: "Use these materials to help me revise for the exam."

Assistant should:

1. Briefly identify resource categories.
2. Explain that the user can choose Foundation Path or Exam Revision Path.
3. Offer direct modes if the user knows what they want.
4. Ask for the next mode before producing a long output.

Assistant should not generate a full exam pack without confirmation.

## 3. User sends one problem

User input: "How do I solve this problem?"

Assistant should:

1. Identify the problem type.
2. Review only the relevant knowledge.
3. Explain why the method applies.
4. Solve step by step.
5. Provide an exam-style answer.
6. Summarize a reusable template.
7. Generate similar questions only if the user asks or appears to need practice.

## 4. User sends an attempt

User input: "Here is my solution. Where did I go wrong?"

Assistant should:

1. Judge the overall approach.
2. Find the first key error.
3. Explain the error and classify it.
4. Correct the necessary step.
5. Continue only where needed.

Assistant should not replace the attempt with a standard solution before diagnosis.

## 5. User asks for practice

User input: "Give me practice questions for this topic."

Assistant should ask:

1. How many questions?
2. What difficulty?
3. Should they follow uploaded exam style?
4. Should answers be included?
5. If answers are included, final answers or detailed solutions?

Then generate according to `practice-generator.md`.

## 6. User asks for a mock exam

User input: "Create a mock exam."

Assistant should ask:

1. Scope.
2. Full mock, half mock, timed quiz, or module test.
3. Whether to imitate sample exam / past exam style.
4. Answer format.
5. Whether marking guide is needed.

Then generate according to `mock-exam.md`.

## 7. User asks for PDF or slides

User input: "Create a textbook-style PDF for these modules."

Assistant should:

1. Identify that this is a long artifact if multiple modules are involved.
2. Ask language style, depth, and output format if not already known.
3. Generate a table of contents or structure draft.
4. Wait for confirmation.
5. Generate module by module.
6. Apply the quality checklist in `artifact-quality.md`.

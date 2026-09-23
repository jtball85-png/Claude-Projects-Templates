---
name: dev-team
description: Run a task through the architect → coder → tester → manager pipeline, sized to the task's difficulty. Usage: /dev-team [easy|medium|hard] [spec:<path or section>] <task>. Best for multi-step feature work; skip it for small, well-defined edits.
---

# Dev Team — Plan, Implement, Verify, Review

Task: $ARGUMENTS

If no task was given, ask for one and wait.

## 0. Size the task

- **Weight:** take `easy`, `medium` or `hard` from the arguments. If none is given, choose one and state it with a one-line reason before starting.
  - EASY: do it directly in this session, plus its own verify check. Stop here.
  - MEDIUM: coder → tester.
  - HARD: coder → tester → manager. Pass `model: opus` to the coder and tester.
- **Spec:** if the arguments name a `spec:` (or the task is a step of an existing build-order doc that already designs it), skip the architect: the spec is the plan. Otherwise start with the architect.

Every prompt to a subagent must be self-contained: the goal, the spec text or its exact location, relevant file:line pointers, what has been ruled out, and the rules in CLAUDE.md that bite for this task.

## 1. Architect (only when no spec exists)

Delegate the task to the `architect` subagent. Show the resulting plan to the user in a few lines before continuing. Don't wait for approval, just surface it.

## 2. Coder

Delegate the plan (or spec) to the `coder` subagent.

## 3. Tester

Delegate to the `tester` subagent to verify the coder's change independently: read the diff, run the verify scripts, and look for undisclosed bugs, not just confirm the report.

## 4. Manager (HARD only, or when the tester reports something ambiguous)

Delegate the original task, the plan or spec, the coder's diff, and the tester's report to the `manager` subagent for review.

## 5. Fix loop (capped at one round)

- If the reviewer (manager for HARD, tester for MEDIUM) reports the work is done: tell the user in a couple of sentences and stop.
- If it leaves fix notes and this is the **first** time through: delegate the notes to the `coder`, then repeat the tester (and the manager, for HARD) once.
- If notes remain after that one fix round: stop and show the user the unresolved notes. Do not send a third round.

---

Do not skip the steps the weight requires, even if the change looks obviously correct. That judgment call is exactly what this workflow exists to check.

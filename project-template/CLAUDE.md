# Working rules for this project

Claude Code loads this file automatically at the start of every session, and so does every subagent (architect, coder, tester, manager). Keep it short: standing rules only. Status belongs in `project-context.md`, session history in `project-memory.md`.

Project state: `project-context.md` (What's next) and `project-memory.md` (newest session first). Older material is in `project-context-archive.md` / `project-memory-archive.md`; read those only when needed.

## Project rules

Add rules here as you decide them ("always X", "never Y"), one line each with the reason. Examples: which sources are authoritative, what is in or out of scope, UI conventions, cost limits.

- (none yet)

## Build process

- Size each task: EASY = direct edit plus a check; MEDIUM = coder + independent tester; HARD = coder + tester + manager (`/dev-team easy|medium|hard ...`). When a plan or spec already exists, skip the architect. State the weight and why when starting.
- Pass `model: opus` to the coder and tester on HARD tasks.
- Build the full scope asked for. Anything not built is disclosed by name with who or what step owns it, never silently dropped.
- Never commit unverified work.

## Testing conventions

- Test behavior through the real code path and persisted state, not a helper's return value. Include negative cases.
- No flaky tests: control randomness and external calls.
- Tests leave no stray data behind.
- Every edit to an existing test's expected values is disclosed (which test, what changed, why).

## Reporting

- Report every judgment call, simplification and changed test. "Not built" items need an owner.

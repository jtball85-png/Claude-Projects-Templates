# dev-team

Four subagents — architect, coder, tester, manager — that split feature work into plan → implement → verify → review, instead of one agent doing all four in its head.

Inspired by a video workflow that ran this by hand: four separate Claude chats, with the human copy-pasting work between them and the "manager" persona leaving notes. That manual shuffling isn't needed here — Claude Code's native subagents (this folder) give each role its own isolated context and scoped tools, and the orchestrating session plays the coordinator that the human played in the video.

## The four roles

| Agent | Tools | Job |
|---|---|---|
| `architect` | read-only + web | Breaks the task into a plan, names files/patterns to reuse |
| `coder` | read/write/bash | Implements the plan |
| `tester` | read-only + bash | Runs tests, exercises edge cases, reports pass/fail — cannot edit |
| `manager` | read-only + bash | Reviews everything against the original request, leaves fix notes or ships |

The tester and manager are deliberately read-only. Separating "did it work" and "is it right" from the coder's own judgment is the point — a single agent grading its own homework will rationalize past its own mistakes more easily than an independent pass will.

## When to use it

Multi-step feature work where a plan → implement → verify split actually earns its keep — enough surface area that a wrong assumption early on is expensive to discover late.

## When not to

Small, well-defined edits or quick fixes. Routing a one-line change through four agent handoffs is slower and burns more tokens than just making the change — the standard "why not one agent" critique is correct for this case. Use these agents individually (or just work directly) instead.

## Iteration cap

If the manager sends fix notes back to the coder, that's one loop. If the result still isn't right after that one round, the manager stops and hands the unresolved notes to the user rather than looping again — unbounded agent-to-agent loops compound mistakes rather than converging on a fix.

## Using it

Copy the four `.md` files into a project's `.claude/agents/` folder. They're then available as agent types on their own (for one-off delegation) or via the `/dev-team` command wired up in `app-project-template` and `project-template`, which runs the full pipeline in order.

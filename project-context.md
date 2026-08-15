# Project: Claude-Projects-Templates
Last updated: 2026-08-15 by Claude Code

## What this project is
Personal Claude Code project scaffolding. `project-template/` is the day-one starting point for every new project (app or general — `/new-project` branches). `library/` is a growing collection of reusable agents, skills, and commands, pulled into a project on demand with `/sync-tools` once they've earned a spot, or graduated into `project-template/` once they should ship by default.

## Current status
Actively maintained, under git, pushed to a private GitHub remote (`github.com/jtball85-png/Claude-Projects-Templates`). `project-template/` was originally two separate templates (`app-project-template` and `project-template`) and got consolidated into one, since the only real difference was the app-specific interview branch in `/new-project`. `library/` currently holds `dev-team` (4 subagents), `sync-tools`, `checkpoint`, and `markitdown` — all graduated into `project-template` — plus `remove-ai-marks`, kept library-only since it needs an external service most projects won't have running.

## Where we left off
Last commit: 9218805 — Add bitwarden-env-sync tool, generalized from Josh Ball Art
In progress: none
Branch: main

## What's next
- [ ] Keep collecting new agents/skills/commands into library/ as they're found
- [ ] Consider whether other existing projects' custom commands (like `checkpoint` was) are worth auditing for more graduation candidates
- [ ] Decide whether/when to standardize repo folder locations across Documents\GitHub and Documents\Claude Projects for the handful of projects not yet touched

## Project structure / terminology
- **`library/`** — the collection point; a component graduates into `project-template/` once it should ship with every new project by default
- **`project-template/`** — the one template, covers both app and general projects (branches in `/new-project`)
- **"Graduated"** — a library component that's been copied into `project-template/.claude/`
- This repo does not run its own `/start-of-day`/`/end-of-day` — it's the source of those commands for other projects, not a consumer of them. `/checkpoint` was run here directly, which is what created this file.

## File map (key files)
| File | Purpose |
|---|---|
| `project-context.md` | This file — project status and orientation |
| `project-memory.md` | Session decisions and reasoning |
| `library/README.md` | The collection-folder convention |
| `project-template/README.md` | Full workflow docs for the template itself |

## Key decisions made
- 2026-08-15 — Consolidated `app-project-template` and `project-template` into one, branching in `/new-project` on app-vs-general
- 2026-08-15 — Removed stale FIN370T files from the repo root; that project has its own repo (`Finance-Class`), well ahead of the stale copy
- 2026-08-15 — Standardized on `Documents\Claude Projects\` for own projects, `Documents\GitHub\` for reference-only clones
- 2026-08-15 — Added `git pull` to `/start-of-day` and `git push` to `/end-of-day` — neither touched the remote before, which is how `Finance-Class` ended up as two diverging local clones

## Known issues
None at this time.

## Context for each tool

### Chat
Thinking, planning, decisions, and fuzzy problems.
Flag anything that requires a major direction change before acting.

### Claude Code
Building and editing files in `library/` and `project-template/`.

### Cowork
Browser tasks, desktop automation, file management.
Use project-context-updater.html on Cowork-heavy days.

## Change log
- 2026-08-15 — Added publish-to-github skill (graduated), generalized bitwarden-env-sync into library/tools/, installed+authenticated gh CLI, finished the git/GitHub lesson, cleaned up 5 project folders (4 committed/pushed, Character Sheet 5E fully connected to GitHub) — Source: Claude Code
- 2026-08-15 — project-context.md and project-memory.md created via /checkpoint — Source: Claude Code

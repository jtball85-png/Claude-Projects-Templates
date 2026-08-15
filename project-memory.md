# Project Memory
Last updated: 2026-08-15

This file captures decisions, reasoning, and session context that
project-context.md doesn't hold. It is Claude's memory between sessions.

---

## Key decisions (permanent record)

- 2026-08-15 — Repo put under git and pushed to a private GitHub remote for the first time
- 2026-08-15 — Consolidated the two templates into one, branching in `/new-project`
- 2026-08-15 — Removed stale FIN370T files from the repo root; real project lives in its own `Finance-Class` repo
- 2026-08-15 — `git pull`/`git push` added to `/start-of-day`/`/end-of-day` — the gap that let `Finance-Class` silently diverge into two local clones

---

## Sessions

## Session — 2026-08-15 (checkpoint)

**Focus:** Setting up this repo's own git/GitHub presence, then a long working session that built out `library/`, consolidated the two templates into one, cleaned up the repo root, and hardened `/start-of-day`/`/end-of-day` with pull/push — much of it prompted by a step-by-step lesson on git/GitHub/GitHub Desktop best practices that surfaced real problems in the user's actual setup along the way.

**Decisions made:**
- Repo initialized with git and connected to `github.com/jtball85-png/Claude-Projects-Templates` (private) — was previously local-only
- `library/` created as the collection point for new agents/skills/commands, separate from the curated templates
- `dev-team` (4 subagents), `sync-tools`, `markitdown`, and `checkpoint` graduated into `project-template/` by default; `remove-ai-marks` kept library-only since it needs an external service
- Consolidated `app-project-template` + `project-template` into one template — the only real difference was the app-specific interview branch in `/new-project`, so it became a branch point instead of two parallel files
- Removed stale FIN370T `project-context.md`/`project-memory.md` from the repo root after confirming the real project has its own repo (`Finance-Class`) well ahead of the stale copy
- Added `git pull` to `/start-of-day` and `git push` to `/end-of-day`, both with safe-stop behavior (no force-push, no silent conflict resolution) — closes the gap that let `Finance-Class` end up as two diverging local clones
- `checkpoint` command (found already in use in `Finance-Class`/`Josh Ball Art`) graduated into the library, with its push step brought in line with the new safe-stop pattern

**Problems solved:**
- Two local clones of `Finance-Class` had drifted (`Documents\GitHub\Finance-Class` ahead through 2026-08-14, `Documents\Claude Projects\Finance-Class` stale at 2026-08-11) — resolved by keeping the current content and moving it to the correct location per the folder-ownership convention, deleting the stale copy
- `markitdown` clone deleted after confirming the skill only needs the published pip package, not the local clone; `watermarks-remover` clone kept since `remove-ai-marks` genuinely depends on running its service

**Approaches discussed:**
- Folder-location convention: split by ownership — `Documents\GitHub\` for reference clones you don't maintain, `Documents\Claude Projects\` for projects you actively build
- GitHub Desktop vs. CLI: CLI for fast/scriptable mechanical work (what's been used here), Desktop as an independent human review checkpoint (visual diffs, history graph) before trusting something is actually on GitHub as intended
- General rule for deleting a cloned repo after extracting from it: safe if what was copied is self-contained (markitdown), not safe if it's a thin wrapper still depending on the original repo's code at runtime (watermarks-remover)

**Left unresolved:**
- `sync-tools.md` and `checkpoint.md` were copied into all 7 existing project folders (`Class-Helper`, `Finance-Class`, `Josh Ball Art`, `VACE VC CLass Comparison`, `claude-project-Character Sheet 5E`, `claude-project-GC PM APP`, `claude-project-food-fasting-tracker APP`) but left **uncommitted** in each project's own repo, per explicit instruction — not yet committed anywhere except this templates repo
- `claude-project-GC PM APP` still has no GitHub remote at all — its work is only ever saved on this one machine
- `claude-project-Character Sheet 5E` still isn't a git repo at all
- Other `Documents\Claude Projects\` folders (`Class-Helper`, `VACE VC CLass Comparison`, the `claude-project-*` ones) haven't been checked for the same kind of duplicate-clone drift `Finance-Class` had
- Root README.md and this project-context.md/project-memory.md pair didn't exist before this session — this is genuinely the first entry

**Files changed this session:**
```
 72 files changed, 1762 insertions(+), 3005 deletions(-)
 (full session, baseline commit 99a18f5 through 80f4d47)
```

<!-- end-of-day skill appends new sessions here -->

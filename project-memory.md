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
- 2026-08-15 — GitHub CLI (`gh`) installed and authenticated on this machine, enabling real repo creation from Claude Code for the first time
- 2026-08-15 — `publish-to-github` skill added and wired into `/new-project`'s final step — new projects now get a GitHub repo automatically, name/visibility always confirmed first

---

## Sessions

## Session — 2026-08-15 (end of day)

**Focus:** Continuation of today's session — added `publish-to-github` (graduated, wired into `/new-project`), generalized the `bitwarden-env-sync` tool out of `Josh Ball Art`, finished the git/GitHub lesson (public vs. private + secrets, branches), then did a full pass across the actual project folders: committed pending `checkpoint`/`sync-tools` additions in 4 repos, fully set up `Character Sheet 5E` (git init, `.gitignore`, GitHub repo, `master`→`main` fix), and deliberately left `Josh Ball Art` and `claude-project-GC PM APP` untouched pending the user's own review.

**Decisions made:**
- `gh` CLI installed via winget and authenticated (device-flow login) — this repo's own remote already existed, but this unlocks creating *new* repos from Claude Code going forward
- `publish-to-github` skill built and graduated straight into `project-template` (not left library-only) since `/new-project` depends on it existing in every freshly-copied project — asks for repo name and public/private before ever creating anything, never silent
- `/new-project` now also `git init`s automatically if needed — the last manual pre-step is gone
- `bitwarden-env-sync` generalized from a project-specific setup in `Josh Ball Art` (hardcoded vault item name, assumed `.venv`) into portable tooling — vault item name now derives from the project folder name, Python runner no longer assumes a virtualenv. Filed under a new `library/tools/` category (standalone scripts a human runs, not something `/sync-tools` reaches) — kept library-only, not graduated, since it needs a Bitwarden account and a genuinely multi-computer project
- Checked actual visibility of every repo on the account via `gh repo list`: 4 public (`Claude-Projects-Templates`, `Josh-Ball-Art-Brain`, `Credit-Mapping-Chart-Tool`, `claude-run-canvas`), 5 private — this repo's own "private" preference from earlier in the session never actually got applied, since it turned out to already exist on GitHub with whatever visibility it already had

**Problems solved:**
- 6 project folders had `checkpoint.md`/`sync-tools.md` sitting uncommitted since earlier in the session — committed and pushed in the 4 straightforward ones (`Finance-Class`, `VACE VC CLass Comparison`, `Class-Helper`, `claude-project-food-fasting-tracker APP`), touching only those two files and leaving each project's own unrelated pending work (`app.py`/`catalog.json` in Class-Helper, `ketotrack-ui-redesign.md` in the fasting tracker) exactly as found
- `claude-project-Character Sheet 5E` had no git history at all — initialized, gitignored `.env`/`__pycache__`/three copyrighted D&D module PDFs (53MB + two chapter excerpts, kept local-only rather than pushed to GitHub), committed, published to a new private repo, and fixed an unwanted `master` default branch to `main` for consistency with every other repo

**Approaches discussed:**
- Public vs. private repos and secrets: bots scan GitHub for exposed keys within minutes of a push; the only real fix for a leaked secret is rotation, not history cleanup; avoid pasting real secret values into chat when avoidable
- Branches for a solo user: the PR/review ceremony is a team-collaboration answer to a problem that mostly doesn't apply solo; still worth reaching for a branch when trying something you might abandon entirely, so `main` never needs a messy revert

**Left unresolved:**
- `claude-project-GC PM APP` — still no GitHub remote, still a large pile of never-committed work including one file that looks deleted (`.claude/commands/end-session.md`) — needs the user's own review before anything touches it
- `Josh Ball Art` — still 12 commits behind its GitHub remote, with substantial uncommitted work in progress across many files and new folders — same, needs the user's own review before any pull/merge
- The 4 public repos haven't been individually reviewed for whether public is actually intended, or should be flipped to private
- `Class-Helper`'s `app.py`/`catalog.json` changes and the fasting tracker's `ketotrack-ui-redesign.md` remain uncommitted in their own repos — untouched on purpose, status unknown
- Other `Documents\Claude Projects\` folders beyond the ones already checked still haven't been audited for Finance-Class-style duplicate-clone drift

**Files changed this session:**
```
 13 files changed, 584 insertions(+), 10 deletions(-)
 (since the earlier checkpoint, commit 6e1a5ab through 9218805 — plus
 out-of-repo work across Character-Sheet-5E, Finance-Class, VACE-VC-CLass-
 Comparison, Class-Helper, and keto-fasting-tracker, not reflected in this
 repo's own diff)
```

---

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

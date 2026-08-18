# Library

This is where new agents, skills, commands, tools, and loops land when you find something worth keeping — before deciding whether it belongs in a template by default.

## The convention

- Every component lives in its own subfolder under `agents/`, `skills/`, `commands/`, or `tools/`.
- Every component has a short README: what it does, where it came from, when to use it, when not to.
- `agents/`, `skills/`, and `commands/` are things Claude Code invokes directly — `/sync-tools` knows how to pull them into a project's `.claude/` folder. `tools/` is different: standalone scripts a human runs directly (double-clicked, or from a terminal), not wired into Claude Code at all. `/sync-tools` doesn't reach these — install by copying the folder's contents in, per its own README.
- A component only gets copied into `project-template/` once you've decided it should ship with every new project by default. Until then, it stays here and you pull it into a specific project manually when you want it.

Templates stay lean. This folder is where things accumulate.

## What's here

| Component | Type | Status |
|---|---|---|
| [dev-team](agents/dev-team/) | agents | Graduated — included in the template |
| [sync-tools](commands/sync-tools.md) | commands | Graduated — included in the template |
| [checkpoint](commands/checkpoint.md) | commands | Graduated — included in the template |
| [markitdown](skills/markitdown/) | skills | Graduated — included in the template |
| [remove-ai-marks](skills/remove-ai-marks/) | skills | Library-only — needs an external service, pull in via `/sync-tools` when wanted |
| [publish-to-github](skills/publish-to-github/) | skills | Graduated — included in the template, used by /new-project |
| [audit-phase](skills/audit-phase/) | skills | Graduated — included in the template |
| [bitwarden-env-sync](tools/bitwarden-env-sync/) | tools | Library-only — needs a Bitwarden account and a project actually used across multiple computers; install manually per its own README |
| [claude-account-switcher](tools/claude-account-switcher/) | tools | Library-only — Windows-only, per-computer setup (not per-project); run `setup.ps1` on each machine per its own README |

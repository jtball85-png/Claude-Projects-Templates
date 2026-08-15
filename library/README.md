# Library

This is where new agents, skills, commands, and loops land when you find something worth keeping — before deciding whether it belongs in a template by default.

## The convention

- Every component lives in its own subfolder under `agents/`, `skills/`, or `commands/`.
- Every component has a short README: what it does, where it came from, when to use it, when not to.
- A component only gets copied into `project-template/` once you've decided it should ship with every new project by default. Until then, it stays here and you pull it into a specific project manually when you want it.

Templates stay lean. This folder is where things accumulate.

## What's here

| Component | Type | Status |
|---|---|---|
| [dev-team](agents/dev-team/) | agents | Graduated — included in the template |
| [sync-tools](commands/sync-tools.md) | commands | Graduated — included in the template |
| [markitdown](skills/markitdown/) | skills | Graduated — included in the template |
| [remove-ai-marks](skills/remove-ai-marks/) | skills | Library-only — needs an external service, pull in via `/sync-tools` when wanted |

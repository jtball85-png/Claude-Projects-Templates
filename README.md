# Claude-Projects-Templates

Personal Claude Code project scaffolding — the starting point for every new project, plus a growing collection of reusable agents, skills, and commands.

---

## What's here

```
Claude-Projects-Templates/
  project-template/   ← copy this to start any new project (app or general)
  library/             ← collected agents/skills/commands, pulled into a
                          project on demand with /sync-tools
```

- **`project-template/`** — the day-one starting point. See its own `README.md` for the full workflow (`/new-project`, `/start-of-day`, `/end-of-day`, and the optional `/dev-team` and `/sync-tools` commands).
- **`library/`** — where new finds land before they're decided on. See its own `README.md` for the convention.

---

## Starting a new project

1. Copy `project-template/` and rename it for your project
2. Open it in VS Code, open Claude Code, run `/new-project`

Full detail in `project-template/README.md`.

## Updating an existing project

Run `/sync-tools` inside it to pull the latest from `library/`. If the project predates that command, see `library/README.md` for the one-time bootstrap step.

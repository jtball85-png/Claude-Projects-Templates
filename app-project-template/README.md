# Claude App Project Template

A project management system tuned for building apps — static frontends,
full stack tools, and anything that runs in a browser.

For general non-app projects, use the generic project-template instead.

---

## What makes this different from the generic template

This template adds four things the generic one doesn't have:

- **Architecture decision** — forces you to answer frontend-only vs. full stack before writing any code
- **Tech stack table** — explicit fields for every layer of your app
- **Data model** — defines the "things" in your app and how they relate
- **User flow** — maps what a user does start to finish before any screens are built

Everything else — the three slash commands, two memory files, daily workflow — works identically.

---

## The three slash commands

| Command | When to run |
|---|---|
| `/new-project` | Once — on day one of any new app project |
| `/start-of-day` | Every session start |
| `/end-of-day` | Every session end |

---

## Optional: the dev-team workflow

A fourth command, `/dev-team <task>`, routes a task through four subagents —
architect, coder, tester, manager — instead of handling it in one session
directly. Worth it for multi-step feature work; skip it for small,
well-defined edits. See `docs/Dev-Team-Workflow.txt` for the full rundown.

A fifth command, `/sync-tools`, pulls the latest agents/skills/commands
from `library/` in the [Claude-Projects-Templates](https://github.com/jtball85-png/Claude-Projects-Templates)
repo into this project — run it any time you want the latest tools you've
collected there, without re-copying the whole template. It asks before
overwriting anything you've customized locally.

---

## Getting started

**Day one:**
1. Copy this template folder and rename it for your app
2. Open it in VS Code
3. Open Claude Code and run `/new-project`
4. Work
5. Run `/end-of-day`

**Every day after:**
1. Open VS Code — project loads automatically
2. Open Claude Code and run `/start-of-day`
3. Work
4. Run `/end-of-day`

---

## What lives where

```
app-project-template/
  .claude/
    agents/
      architect.md           ← optional, used by /dev-team
      coder.md                ← optional, used by /dev-team
      tester.md                ← optional, used by /dev-team
      manager.md              ← optional, used by /dev-team
    commands/
      new-project.md        ← run once on day one
      start-of-day.md       ← run every session start
      end-of-day.md         ← run every session end
      dev-team.md            ← optional, multi-step feature work
      sync-tools.md           ← optional, pulls latest from library/
  docs/
    Daily-Workflow.txt      ← quick reference for daily steps
    Session-0-Project-Kickoff.txt  ← what /new-project does and why
    Dev-Team-Workflow.txt   ← what /dev-team does and when to use it
  project-context.md        ← project status (auto-updated by end-of-day)
  project-memory.md         ← session memory (auto-updated by end-of-day)
  Project-Instructions.txt  ← paste this into your Claude Project instructions box
  README.md                 ← this file
```

---

## Which template to use

| Starting point | Use |
|---|---|
| Building an app, tool, or anything that runs in a browser | app-project-template (this one) |
| Everything else — writing, planning, general projects | project-template |

---

## The one rule

`project-context.md` and `project-memory.md` are your project's memory.
Claude has no memory between sessions — these files are how it remembers.
Keep them current. `/end-of-day` handles it automatically.

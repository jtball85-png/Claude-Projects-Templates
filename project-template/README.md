# Claude Project Template

A project management system for working with Claude Code, Chat, and Cowork
without losing context between sessions.

---

## How it works

Every project has two memory files:

| File | Purpose |
|---|---|
| `project-context.md` | Project status — what it is, where it stands, what's next |
| `project-memory.md` | Session memory — decisions, reasoning, and context from every work session |

Three slash commands run the system automatically inside Claude Code:

| Command | When to run |
|---|---|
| `/new-project` | Once — on day one of any new project |
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

Also included by default: the `markitdown` skill, which converts Word,
PowerPoint, Excel, images, audio, and other files to Markdown on request
(via the `markitdown` CLI). See `.claude/skills/markitdown/SKILL.md`.

---

## Getting started

**Day one of a new project:**
1. Copy this template folder and rename it for your project
2. Open it in VS Code
3. Open Claude Code and run `/new-project`
4. Work
5. Run `/end-of-day`

**Every day after that:**
1. Open VS Code — your project loads automatically
2. Open Claude Code and run `/start-of-day`
3. Work
4. Run `/end-of-day`

---

## What lives where

```
your-project/
  .claude/
    agents/
      architect.md           ← optional, used by /dev-team
      coder.md                ← optional, used by /dev-team
      tester.md                ← optional, used by /dev-team
      manager.md              ← optional, used by /dev-team
    skills/
      markitdown/SKILL.md     ← converts files to Markdown on request
    commands/
      new-project.md        ← run once on day one
      start-of-day.md       ← run every session start
      end-of-day.md         ← run every session end
      dev-team.md            ← optional, multi-step feature work
      sync-tools.md           ← optional, pulls latest from library/
  docs/
    Daily-Workflow.txt      ← quick reference for daily steps
    Session-0-Project-Kickoff.txt  ← guide for what /new-project does
    Dev-Team-Workflow.txt   ← what /dev-team does and when to use it
  project-context.md        ← project status (auto-updated by end-of-day)
  project-memory.md         ← session memory (auto-updated by end-of-day)
  Project-Instructions.txt  ← paste this into your Claude Project instructions box
  README.md                 ← this file
```

---

## The one rule

`project-context.md` and `project-memory.md` are your project's memory.
Claude has no memory between sessions — these files are how it remembers.

Keep them current. `/end-of-day` handles it automatically.

---

## Tools and their roles

**Claude Code** — building, editing, reading files. Runs the three slash commands.

**Chat** — thinking, planning, decisions, fuzzy problems. Paste `project-context.md`
at the start of any Chat session to orient it.

**Cowork** — browser tasks, desktop automation, file management. Use
`project-context-updater.html` on Cowork-heavy days to update your context doc.

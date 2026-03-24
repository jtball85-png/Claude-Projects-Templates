# Project: [Project Name]
Last updated: YYYY-MM-DD by [Chat | Claude Code | Cowork]

## What this project is
[2–3 sentences — what it is, who it's for, what problem it solves]

## Architecture decision
> Answer this once at project start. Revisit only when scope changes.

**Does this app need to save data between sessions or between users?**
- [ ] No → Static frontend (HTML/CSS/JS only)
- [ ] Yes → Full stack (frontend + backend + database)
- [ ] Not sure yet → Start static, plan to upgrade

**Does this app need to hide secrets from the browser?**
- [ ] No
- [ ] Yes → Backend required even if no database

**Current answer:** [Static frontend / Full stack / Undecided]

## Tech stack
| Layer | Tool/Language | Notes |
|---|---|---|
| Frontend | | e.g. HTML/CSS/JS, React |
| Backend | | e.g. Node + Express, Python + FastAPI |
| Database | | e.g. Supabase, SQLite, PostgreSQL |
| Auth | | e.g. Supabase Auth, Clerk, none |
| Deployment | | e.g. Vercel, Railway, local only |
| AI / APIs | | e.g. Anthropic API, OpenAI, Stripe |

## Data model
> What are the "things" in this app and how do they relate?
> Example: "Users have Projects. Projects have Tasks. Tasks have Comments."
> Skip if purely static frontend with no saved data.

[Describe your data relationships here]

## User flow
> What does a user actually do from start to finish?
> Example: "User lands on homepage → clicks Sign Up → fills form → lands on dashboard → creates first project"

[Describe the user's path through the app here]

## Current status
[One paragraph — what phase, what's working, what's broken or blocked]

## Where we left off
Last commit: [commit hash or N/A]
In progress: [what was actively being worked on]
Branch: [branch name or N/A]

## What's next
- [ ] [Next action — Claude Code / Chat / Cowork]
- [ ] [Next action]
- [ ] [Next action]

## File structure
```
/project-root
  /src        → [what lives here]
  /assets     → [what lives here]
  /docs       → reference guides
  /archive    → archived context docs
  index.html  → [what this is]
```

## Environment and credentials
> Never put actual secret values here. Just note what variables exist and where they live.

- .env file: [exists / not yet created]
- Variables needed: [e.g. ANTHROPIC_API_KEY, SUPABASE_URL]
- Where secrets are stored: [local .env / Vercel dashboard / not set up yet]

## Key decisions made
- [Decision and rationale]

## Known issues
- [Issue and workaround if any]

## Context for each tool

### Chat
Thinking, planning, decisions, architecture questions.
Flag scope changes or tech stack changes before acting.

### Claude Code
Building and editing files. Tech stack: [summary].
Run /start-of-day at the start of every session.
Run /end-of-day at the end of every session.

### Cowork
Browser tasks, desktop automation, file management.
Use project-context-updater.html on Cowork-heavy days.

## Change log
Auto-updated by /end-of-day at end of every Claude Code session.
On Cowork-heavy days, use project-context-updater.html instead.
- YYYY-MM-DD — [entry] — Source: [Chat | Claude Code | Cowork]

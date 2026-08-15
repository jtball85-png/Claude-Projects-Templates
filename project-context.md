# Project: FIN370T Finance Course Assistant
Last updated: 2026-08-04 by Claude Code

## What this project is
A personal study assistant for Josh's FIN370T finance course, using Cornett, Adair, & Nofsinger's "Finance: Applications and Theory" (2025 Release, McGraw-Hill). It helps him respond to weekly discussion prompts by researching assigned textbook chapters plus verified, non-paywalled internet sources with APA citations, and helps him review multiple-choice practice questions by identifying the correct answer with reasoning and evidence drawn directly from the textbook chapters.

## Architecture decision
**Does this app need to save data between sessions or between users?**
- [x] Static / file-based — no backend or database; history and context are kept as files in this repo (project-memory.md, session notes)

**Does this app need to hide secrets from the browser?**
- [x] No

**Current answer:** Static / file-based (no backend, no database, no deployment — used directly through Claude Code/Chat)

## Tech stack
| Layer | Tool/Language | Notes |
|---|---|---|
| Frontend | None | Interacted with directly through Claude Code/Chat |
| Backend | None | |
| Database | None | History kept as files in this repo |
| Auth | None | Personal use only |
| Deployment | Local only | This repo, used locally |
| AI / APIs | Claude (Claude Code + web search) | No external API keys required |

## Data model
- **Chapters** — textbook content, stored as page-scan PNGs under /Research/Chapter NN/, one folder per chapter
- **Weekly Prompts** — topic prompt → Josh's response, built from chapter research + verified external sources, APA in-text + reference citations
- **Review Sessions** — multiple-choice question → independent answer, reasoning tied to chapter/topic, why-not explanations for wrong choices, source citation

## User flow
**Weekly prompts:** Josh pastes the weekly topic and identifies the relevant chapter(s). Claude researches those chapters plus additional verified, non-paywalled sources (using only actual site content, never assumed or guessed), and writes a response using APA in-text citations and a References list.

**Review questions:** Josh pastes a multiple-choice question. Claude answers using only the identified textbook chapters — giving an independent answer, reasoning tied to specific topics/chapters, a why-not explanation for each incorrect option, and a source citation (topic/chapter) — then prompts for the next question.

## Current status
Brand new project. Chapters 1–3 are populated with readable page-scan PNGs (92 pages total) in /Research; chapters 4–5 are empty placeholders for later in the course. Course guide (fin370T_v2_CourseGuide.pdf) and syllabus (fin370t_v2_syllabus.docx) have been added to the repo root. Citation format (APA) and the review-question response format have been established from Josh's examples. No prompts or review sessions have been run yet.

## Where we left off
Last commit: ec72722 — New app project initialized — FIN370T Finance Course Assistant
In progress: none
Branch: main

## What's next
- [ ] Review/index chapters 2–3 content — Claude Code
- [ ] Handle first weekly prompt — Claude Code / Chat

## File structure
```
/project-root
  /Research      → textbook chapter content (PNG page scans, one folder per chapter)
  fin370T_v2_CourseGuide.pdf → course guide
  fin370t_v2_syllabus.docx   → syllabus
  project-context.md → this file
  project-memory.md  → session memory
  /project-template, /app-project-template, /archive → unrelated template scaffolding, not part of this project
```

## Environment and credentials
- .env file: not needed
- Variables needed: none
- Where secrets are stored: not applicable

## Key decisions made
- 2026-08-04 — Project initialized
- 2026-08-04 — Architecture: Static/file-based, no backend
- 2026-08-04 — Citation style: APA (in-text + References)
- 2026-08-04 — Review-question response format established (independent answer, reasoning, why-not per option, source citation)

## Known issues
None — textbook content is provided only as PNG page scans (no PDF access), confirmed readable by Claude (cover page and end-of-chapter problem sets both legible).

## Context for each tool

### Chat
Thinking, planning, decisions, and fuzzy problems.
Flag architecture changes or scope changes before acting.

### Claude Code
Building and editing files. Tech stack: Claude Code + web search, working directly against files in this repo — no separate frontend/backend.
Run /start-of-day at the start of every session.
Run /end-of-day at the end of every session.

### Cowork
Browser tasks, desktop automation, file management.
Use project-context-updater.html on Cowork-heavy days.

## Change log
- 2026-08-04 — New app project initialized — FIN370T Finance Course Assistant — Source: Claude Code
- 2026-08-04 — Project initialized — Source: Claude Code

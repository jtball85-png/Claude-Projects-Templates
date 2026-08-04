# Project Memory
Last updated: 2026-08-04

This file captures decisions, reasoning, and session context that
project-context.md doesn't hold. It is Claude's memory between sessions.

---

## Key decisions (permanent record)

- 2026-08-04 — Project initialized
- 2026-08-04 — Architecture decision: Static/file-based, no backend or database
- 2026-08-04 — Citation style: APA, in-text + References list
- 2026-08-04 — Review-question response format locked in from Josh's example: independent answer choice, reasoning tied to specific topics/chapters, why-not explanation for each wrong option, source citation (topic/chapter), then prompt for next question
- 2026-08-04 — Weekly-prompt research rule: only verified, non-paywalled sources; must use actual site content, never assumed or guessed
- 2026-08-04 — Textbook is Cornett, Adair, & Nofsinger (2025), "Finance: Applications and Theory," 2025 Release, McGraw-Hill — content available only as page-scan PNGs (no PDF access), confirmed readable

---

## Sessions

## Session — 2026-08-04

**Focus:** Set up the new FIN370T Finance Course Assistant project (interview, project-context.md, project-memory.md), then reviewed Chapter 1 content and answered a series of Chapter 1 review questions.

**Decisions made:**
- Project files (project-context.md, project-memory.md) live at the Finance repo root, not in a separate subfolder — user's explicit choice.
- Confirmed all 30 pages of Chapter 1 PNGs (Research/Chapter 01/) are legible, including cover pages and end-of-chapter problem sets.

**Problems solved:**
- None — review-question format from initial setup worked as intended across ~20 questions.

**Approaches discussed:**
- User asked whether chapter PNGs need to be re-read every session. Answer given: within a session, no (stays in context) unless conversation is compacted; across sessions, yes, currently, since nothing persists. Proposed building a `chapter-notes.md` per chapter (key terms, learning goals, section outline, page refs) as a persistent text index so future sessions don't need to re-read every PNG. User has not yet confirmed whether to build these.

**Left unresolved:**
- `chapter-notes.md` (or similar) files for chapters 1–3 not yet created — proposed but not started.
- Two review questions in this session referenced facts not present in Chapter 1's text (TCJA mortgage interest deduction cap; net impact of lower individual tax rates) — answered using general knowledge/reasoning with the gap flagged to the user each time, per their "no assuming" rule. User may want to confirm with instructor whether those questions are meant to draw on a different chapter or on outside material.
- First weekly prompt not yet started — user said "we will tackle our first prompt later."
- `Research/`, `.claude/`, and the two course files (`fin370T_v2_CourseGuide.pdf`, `fin370t_v2_syllabus.docx`) remain untracked in git — flagged to user, not yet resolved whether to add them.

**Files changed this session:**
```
 project-context.md | 90 ++++++++++++++++++++++++++++++++++++++++++++++++++++++
 project-memory.md  | 22 +++++++++++++
 2 files changed, 112 insertions(+)
```

<!-- end-of-day skill appends new sessions here -->

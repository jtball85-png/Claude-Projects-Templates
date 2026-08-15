# remove-ai-marks

Copied as-is from https://github.com/guillaumemeyer/watermarks-remover (`skills/remove-ai-marks/`) — `SKILL.md` and `references/` are unmodified vendor files, not authored here.

## What it does

Strips AI-provenance marks (invisible Unicode, statistical text watermarks, C2PA/EXIF/XMP/document metadata) from text and files. Full detail is in `SKILL.md` and `references/`.

## Before this skill does anything, its service must be running

This is a **thin HTTP client only** — it contains no cleaning code itself and refuses to do anything if its backing service isn't reachable at `$WATERMARKS_SERVICE_URL` (default `http://127.0.0.1:8765`). To use it in a project:

1. Get a checkout of the source repo (`git clone https://github.com/guillaumemeyer/watermarks-remover`), separate from this templates repo.
2. Start the service from that checkout: `docker compose up -d`, or `make serve` for a local run without Docker.
3. Then this skill's `curl` calls against `/health`, `/inspect`, `/clean` will work.

## When to use

Cleaning up AI-provenance marks on your own content — privacy, hygiene, research. See `references/ethics.md` for intended-use boundaries; it's not for misrepresenting AI-generated work as human-written.

## When not to

Any project that doesn't already have the service running and isn't going to stand it up — the skill will just report the service unreachable. This is why it's library-only rather than graduated into the default templates: it needs an external service most new projects won't have, and the use case is specialized enough that it shouldn't be silently available everywhere by default.

Pull it into a specific project with `/sync-tools` when you actually need it there.

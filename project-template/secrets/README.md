# bitwarden-env-sync

Keeps a project's `.env` secrets in sync across every computer you work on, using Bitwarden as the shared vault. Generalized from a working setup found in `Josh Ball Art` — not a Claude Code agent/skill/command, this is standalone tooling a human runs directly (double-click a `.bat` file).

## Why this exists

`.env` should always be gitignored — it holds real credentials, so `git`
(and therefore `/start-of-day`/`/end-of-day`) never carries it between
computers. Without something filling that gap, a secret added on one
computer just silently doesn't exist on another until it's copied over by
hand — the same "two computers drift apart" problem `/start-of-day` and
`/end-of-day` solve for commits, just for secrets instead.

Bitwarden closes that gap: one secure note in your vault holds the full
`.env` text, named after the project, and Bitwarden's own account sync
carries it to every computer. Two scripts push/pull that note.

A password manager was chosen over an in-repo encrypted file (`sops`/`age`)
deliberately: losing a single encryption key would mean losing every secret
with no recovery path, where a vendor-run vault has account recovery
options a bare key file doesn't.

## What's here

```
bitwarden-env-sync/
  Sync Bitwarden Secrets.bat   ← double-click this for the common case (pull)
  secrets/
    sync_secrets.ps1            ← what the .bat runs: unlock, pull, lock
    pull_env_from_vault.py      ← merges vault secrets into local .env
    push_env_to_vault.py        ← pushes local .env to the vault (after rotating a credential)
```

The vault item name is derived automatically from the project folder's name
(`<folder-name> .env`) — no per-project editing needed once this is copied in.

## Already installed in this project

This ships with `project-template/`, so every project copied from it
already has `Sync Bitwarden Secrets.bat` at the project root and these
scripts in `secrets/`. The template's `.gitignore` already excludes
`.env`, so real secrets never get committed.

The vault item is named after the project folder (`<folder-name> .env`).
If you rename the project folder, rename the vault item to match, or run
`push_env_to_vault.py` again to create one under the new name.

A project that doesn't use any API keys can ignore all of this. Nothing
runs unless you double-click the `.bat`.

The master copy lives in `library/tools/bitwarden-env-sync/` in the
Claude-Projects-Templates repo. To add it to an older project that wasn't
copied from this template, copy that folder's contents into the project
root (so `Sync Bitwarden Secrets.bat` and `secrets/` sit next to `.env`,
not nested under `.claude/`). Then make sure `.env` is in that project's
`.gitignore`, because this tooling doesn't add it for you.

## Your Bitwarden account

You already have one. The vault was set up in July 2026 for Josh Ball Art
(vault item "JBA Brain .env"), and the Bitwarden CLI is installed on both
computers. For a new project, skip to step 3 below on the computer that
has the project's real keys.

## One-time setup

1. **Create a free Bitwarden account** at bitwarden.com (this step is
   yours — needs your email + a master password you choose and remember;
   there's no recovery if you forget it, so store it somewhere durable).
2. On **each** computer:
   ```
   bw login your-email@example.com
   ```
   (prompts for your master password, and 2FA if you turn it on — worth
   turning on).
3. On the computer that currently has the real secrets:
   ```
   bw unlock
   ```
   Paste the session key it prints into your shell:
   - PowerShell: `$env:BW_SESSION = "paste-here"`
   - bash: `export BW_SESSION="paste-here"`

   Then:
   ```
   python secrets/push_env_to_vault.py
   ```
   This creates the vault item from your current local `.env`.

## Quick path: one-click sync (day to day)

Double-click **`Sync Bitwarden Secrets.bat`**. It asks for your Bitwarden
master password once (a normal masked prompt — nothing is displayed,
nothing is saved to disk except `.env` itself), pulls the real secrets
down, and locks the vault again automatically.

## Manual path (what the one-click script automates)

```
bw unlock
```
(export/paste `BW_SESSION` as above), then:

```
python secrets/pull_env_from_vault.py
```

This merges the vault's keys into local `.env`, adding or replacing each
`KEY=value` line without touching anything else already there.

## After rotating any credential

Whenever a credential changes on whichever computer you're on, run
`push_env_to_vault.py` there afterward so the vault — and therefore every
other computer — picks up the new value next time it pulls. Pushing is a
rarer, more deliberate action than pulling, so it's kept manual rather
than folded into the one-click script.

## Requirements

- Bitwarden CLI (`bw`) — `winget install --id Bitwarden.CLI -e`
- Python 3, on PATH as `python` or `py` — the scripts are pure standard
  library, no packages to install, no virtual environment required

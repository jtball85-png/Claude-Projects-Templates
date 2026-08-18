# claude-account-switcher

Gives Windows PowerShell two commands, `claude-personal` and `claude-work`,
that each launch the Claude Code CLI fully logged in as a separate Anthropic
account, permanently — no repeated logins, no SSO wait, no login screen.
Not a Claude Code agent/skill/command — this is a per-computer setup a human
runs once in a terminal.

## Why this exists

The Claude Code VS Code extension's built-in "switch account" button is a
known, currently-open bug (doesn't complete the switch, and the extension has
no `/logout` command at all — see anthropics/claude-code issues #54478,
#28585, #55621). Re-logging into a work/school account by hand is often slow
(SSO redirects), and doing that every time you want to switch context is not
sustainable.

The underlying fix is to give each account its own isolated home directory,
so both stay signed in side by side and "switching" is just typing a
different word. `CLAUDE_CONFIG_DIR` alone isn't enough for this — Claude Code
also writes account state directly to `~\.claude.json`, outside whatever
`CLAUDE_CONFIG_DIR` points to — so this temporarily redirects `$env:USERPROFILE`
itself for the duration of each launch instead.

## Installing on a new computer

1. Copy `setup.ps1` from this folder anywhere on the target machine (or run
   it straight from a cloned copy of this repo).
2. Open PowerShell and run it:
   ```powershell
   .\setup.ps1
   ```
   This sets your execution policy to `RemoteSigned` for your user account
   (only if it's currently blocking local scripts) and adds the
   `claude-personal` / `claude-work` functions to your PowerShell profile.
   Safe to re-run — it skips steps that are already done.
3. Close the terminal and open a brand new one (required for the profile
   change to load).
4. Run `claude-personal` — log in with your personal account when prompted.
5. Run `claude-work` — log in with your work/school account when prompted
   (this is the one login that may go through a slow SSO flow — but only
   this once).

From then on, in VS Code or any terminal: open a new terminal tab and type
`claude-personal` or `claude-work`. Each remembers its own login forever.
Closing a terminal tab doesn't log you out — the same command in a fresh tab
picks the session back up.

## What it changes

- PowerShell execution policy, scope `CurrentUser`, set to `RemoteSigned`
  (only if it was more restrictive) — lets locally-written scripts run,
  required for the profile functions below to load at all.
- Appends a function block to your PowerShell profile
  (`$PROFILE`, typically
  `Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1` or
  `Documents\PowerShell\Microsoft.PowerShell_profile.ps1`).
- Creates `.claude-split\.claude-personal\` and `.claude-split\.claude-work\`
  under your Windows user folder the first time each command runs — these
  hold each account's isolated Claude Code credentials and settings.

## Requirements

- Windows + PowerShell (this is a Windows-specific workaround; not needed on
  macOS/Linux, where running two `claude` accounts is usually simpler).
- Claude Code CLI already installed and on `PATH`.

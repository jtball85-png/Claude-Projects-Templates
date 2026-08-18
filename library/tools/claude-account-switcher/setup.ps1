<#
Sets up two terminal commands, claude-personal and claude-work, that each
launch Claude Code fully signed in as a separate account, permanently.

Safe to re-run: skips the profile-append step if it's already been added.
#>

$marker = "# --- Claude Code: switch between personal and work accounts ---"

# 1. Allow local scripts (including the profile below) to actually run.
$currentPolicy = Get-ExecutionPolicy -Scope CurrentUser
if ($currentPolicy -eq 'Restricted' -or $currentPolicy -eq 'Undefined') {
    Write-Output "Setting PowerShell execution policy to RemoteSigned for your user account..."
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
} else {
    Write-Output "Execution policy already allows local scripts ($currentPolicy) — skipping."
}

# 2. Add the claude-personal / claude-work functions to the PowerShell profile.
if (-not (Test-Path $PROFILE)) {
    New-Item -ItemType Directory -Path (Split-Path $PROFILE) -Force | Out-Null
    New-Item -ItemType File -Path $PROFILE -Force | Out-Null
}

$alreadyInstalled = (Get-Content $PROFILE -Raw -ErrorAction SilentlyContinue) -like "*$marker*"

if ($alreadyInstalled) {
    Write-Output "claude-personal / claude-work are already set up in your profile — skipping."
} else {
    $block = @"

$marker
# Type "claude-personal" to open Claude Code logged in as your personal account.
# Type "claude-work" to open Claude Code logged in as your work account.
# The first time you run each one, it will ask you to log in. After that,
# it remembers that login every time, and the two never interfere with each other.

function Invoke-ClaudeWithProfile {
    param([string]`$ProfileName, `$ClaudeArgs)
    `$targetPath = Join-Path `$env:USERPROFILE ".claude-split\`$ProfileName"
    New-Item -ItemType Directory -Path (Join-Path `$targetPath ".local\bin") -Force | Out-Null
    `$oldUserProfile = `$env:USERPROFILE
    `$oldPath = `$env:PATH
    try {
        `$env:USERPROFILE = `$targetPath
        `$env:PATH = "`$targetPath\.local\bin;`$env:PATH"
        & claude @ClaudeArgs
    } finally {
        `$env:USERPROFILE = `$oldUserProfile
        `$env:PATH = `$oldPath
    }
}

function claude-personal { Invoke-ClaudeWithProfile -ProfileName ".claude-personal" @args }
function claude-work     { Invoke-ClaudeWithProfile -ProfileName ".claude-work" @args }
"@
    Add-Content -Path $PROFILE -Value $block
    Write-Output "Added claude-personal / claude-work to $PROFILE"
}

Write-Output ""
Write-Output "Done. Close this terminal, open a brand new one, then run:"
Write-Output "  claude-personal   (or)   claude-work"
Write-Output "Each will prompt you to log in the first time only, then remember it permanently."

param(
    [string]$TargetDir
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$SourceDir = Join-Path $RepoRoot "skill\relationship-descendant"

if (-not (Test-Path -LiteralPath $SourceDir)) {
    throw "Skill source not found: $SourceDir"
}

if (-not $TargetDir) {
    $LifeDir = Join-Path $HOME ".openclaw\workspaces\life\skills"
    if (Test-Path -LiteralPath $LifeDir) {
        $TargetDir = $LifeDir
    } else {
        $TargetDir = Join-Path $HOME ".openclaw\skills"
    }
}

$InstallDir = Join-Path $TargetDir "relationship-descendant"
New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
if (Test-Path -LiteralPath $InstallDir) {
    Remove-Item -LiteralPath $InstallDir -Recurse -Force
}
Copy-Item -LiteralPath $SourceDir -Destination $InstallDir -Recurse -Force

Write-Host "Installed relationship-descendant to: $InstallDir"

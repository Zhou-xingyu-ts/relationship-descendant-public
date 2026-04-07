#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SOURCE_DIR="$REPO_ROOT/skill/relationship-descendant"

if [ ! -d "$SOURCE_DIR" ]; then
  echo "Skill source not found: $SOURCE_DIR" >&2
  exit 1
fi

if [ "${1:-}" != "" ]; then
  TARGET_DIR="$1"
elif [ -d "$HOME/.openclaw/workspaces/life/skills" ]; then
  TARGET_DIR="$HOME/.openclaw/workspaces/life/skills"
else
  TARGET_DIR="$HOME/.openclaw/skills"
fi

INSTALL_DIR="$TARGET_DIR/relationship-descendant"
mkdir -p "$TARGET_DIR"
rm -rf "$INSTALL_DIR"
cp -R "$SOURCE_DIR" "$INSTALL_DIR"

echo "Installed relationship-descendant to: $INSTALL_DIR"

#!/usr/bin/env bash
# Installs the GlowinPunk Ghostty config + shaders on macOS or Linux.
# Run from anywhere: bash config/ghostty/install.sh
# An existing config is backed up to config.ghostty.bak.<timestamp> first.
set -euo pipefail
SRC="$(cd "$(dirname "$0")" && pwd)"

case "$(uname -s)" in
  Darwin) DEST="$HOME/Library/Application Support/com.mitchellh.ghostty" ;;
  *)      DEST="${XDG_CONFIG_HOME:-$HOME/.config}/ghostty" ;;
esac

mkdir -p "$DEST/shaders"

for f in config.ghostty config; do
  if [ -f "$DEST/$f" ]; then
    cp "$DEST/$f" "$DEST/$f.bak.$(date +%Y%m%d-%H%M%S)"
    echo "Backed up existing $f"
  fi
done
# Ghostty prefers config.ghostty; an older plain "config" file would be loaded
# too and can override it, so move it aside once it's backed up.
[ -f "$DEST/config" ] && mv "$DEST/config" "$DEST/config.old"

cp "$SRC/config.ghostty" "$DEST/config.ghostty"
cp "$SRC"/shaders/*.glsl "$DEST/shaders/"

# App icon (macOS only). Ghostty reads a custom icon from ~/.config/ghostty/Ghostty.icns
# when `macos-icon = custom`, regardless of where config.ghostty lives.
if [ "$(uname -s)" = "Darwin" ]; then
  ICON_DIR="$HOME/.config/ghostty"
  mkdir -p "$ICON_DIR"
  [ -f "$ICON_DIR/Ghostty.icns" ] && cp "$ICON_DIR/Ghostty.icns" "$ICON_DIR/Ghostty.icns.bak.$(date +%Y%m%d-%H%M%S)"
  cp "$SRC/icon/Ghostty.icns" "$ICON_DIR/Ghostty.icns"
  echo "Installed icon to: $ICON_DIR/Ghostty.icns"
fi

echo "Installed to: $DEST"
echo "Reload Ghostty: Cmd+Shift+, (macOS) / Ctrl+Shift+, (Linux), or menu: Ghostty -> Reload Configuration."
echo "Open a NEW tab afterwards so the underscore cursor (shell integration) applies."

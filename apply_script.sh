#!/usr/bin/env bash
# Applies the GlowinPunk cyberpunk/neon GNOME rice on Ubuntu 24.04 (GNOME 46).
# Run from the repo root: bash apply_script.sh
set -uo pipefail
REPO="$(cd "$(dirname "$0")" && pwd)"

echo "== GNOME settings =="
gsettings set org.gnome.desktop.interface gtk-theme         'Yaru-magenta-dark'
gsettings set org.gnome.desktop.interface icon-theme        'Cyberpunk-Neon'
gsettings set org.gnome.desktop.interface cursor-theme      'Cyberpunk-Neon'
gsettings set org.gnome.desktop.interface color-scheme      'prefer-dark'
gsettings set org.gnome.desktop.interface font-name         'JetBrainsMono Nerd Font Mono 11'
gsettings set org.gnome.desktop.interface monospace-font-name 'JetBrainsMono Nerd Font Mono 11'
gsettings set org.gnome.shell.extensions.user-theme name    'NV-Yaru'
gsettings set org.gnome.shell disable-user-extensions       false

echo "== Ubuntu Dock (dash-to-dock) =="
gsettings set org.gnome.shell.extensions.dash-to-dock custom-background-color          true
gsettings set org.gnome.shell.extensions.dash-to-dock background-color                 '#0a0a12'
gsettings set org.gnome.shell.extensions.dash-to-dock background-opacity               0.08
gsettings set org.gnome.shell.extensions.dash-to-dock transparency-mode                'FIXED'
gsettings set org.gnome.shell.extensions.dash-to-dock custom-theme-customize-running-dots true
gsettings set org.gnome.shell.extensions.dash-to-dock custom-theme-running-dots-color  '#76b900'
gsettings set org.gnome.shell.extensions.dash-to-dock custom-theme-running-dots-border-color '#76b900'
gsettings set org.gnome.shell.extensions.dash-to-dock dock-position                    'BOTTOM'
gsettings set org.gnome.shell.extensions.dash-to-dock extend-height                    false
gsettings set org.gnome.shell.extensions.dash-to-dock dash-max-icon-size               48

echo "== libadwaita / GTK overrides =="
mkdir -p "$HOME/.config/gtk-4.0" "$HOME/.config/gtk-3.0"
cp "$REPO/config/gtk-4.0/gtk.css"      "$HOME/.config/gtk-4.0/gtk.css"
cp "$REPO/config/gtk-4.0/gtk-dark.css" "$HOME/.config/gtk-4.0/gtk-dark.css"
cp "$REPO/config/gtk-3.0/gtk.css"      "$HOME/.config/gtk-3.0/gtk.css"

echo "== kitty =="
mkdir -p "$HOME/.config/kitty"
cp "$REPO/config/kitty/kitty.conf" "$HOME/.config/kitty/kitty.conf"

echo "== tmux =="
mkdir -p "$HOME/.config/tmux"
cp "$REPO/config/tmux/tmux.conf" "$HOME/.config/tmux/tmux.conf"

echo "== neofetch =="
mkdir -p "$HOME/.config/neofetch"
cp "$REPO/config/neofetch/config.conf" "$HOME/.config/neofetch/config.conf"

echo "== Blur-my-shell dock glow (requires Python3 + gi) =="
python3 "$REPO/set_dock_glow.py"

echo "== Rounded window borders (NVIDIA green, 3px) =="
python3 "$REPO/set_borders.py"

echo
echo "Done. Reload GNOME Shell (Alt+F2 → r) or log out/in for all changes to take effect."
echo "To reload kitty config: Ctrl+Shift+F5 inside kitty."
echo "To reload tmux config:  tmux source ~/.config/tmux/tmux.conf"

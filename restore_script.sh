#!/usr/bin/env bash
# Reverts the GlowinPunk cyberpunk/neon GNOME rice and restores the
# original Ubuntu/NV-Yaru desktop configuration (Ubuntu 24.04, GNOME 46).
#
# Regenerated from the build session's history after the local working
# copy was cleaned up by an unrelated Downloads-folder cleanup. Safe to
# re-run.
set -uo pipefail

echo "== Restoring gsettings =="
gsettings set org.gnome.desktop.interface gtk-theme 'Yaru-olive-dark'
gsettings set org.gnome.desktop.interface icon-theme 'Yaru-olive'
gsettings set org.gnome.desktop.interface cursor-theme 'Yaru'
gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'
gsettings set org.gnome.shell.extensions.user-theme name 'NV-Yaru'
gsettings set org.gnome.shell enabled-extensions "['user-theme@gnome-shell-extensions.gcampax.github.com', 'ding@rastersoft.com', 'ubuntu-dock@ubuntu.com', 'tiling-assistant@ubuntu.com']"

echo "== Restoring Ubuntu Dock (dash-to-dock) to its defaults =="
gsettings reset org.gnome.shell.extensions.dash-to-dock custom-background-color
gsettings reset org.gnome.shell.extensions.dash-to-dock background-color
gsettings reset org.gnome.shell.extensions.dash-to-dock background-opacity
gsettings reset org.gnome.shell.extensions.dash-to-dock custom-theme-customize-running-dots
gsettings reset org.gnome.shell.extensions.dash-to-dock custom-theme-running-dots-color
gsettings reset org.gnome.shell.extensions.dash-to-dock custom-theme-running-dots-border-color
gsettings reset org.gnome.shell.extensions.dash-to-dock dock-position
gsettings reset org.gnome.shell.extensions.dash-to-dock autohide
gsettings reset org.gnome.shell.extensions.dash-to-dock intellihide
gsettings reset org.gnome.shell.extensions.dash-to-dock transparency-mode
gsettings set org.gnome.shell.extensions.dash-to-dock dash-max-icon-size 48
gsettings set org.gnome.shell.extensions.dash-to-dock extend-height false

echo "== Disabling and removing every extension added by the rice =="
for uuid in blur-my-shell@aunetx rounded-window-corners@fxgn \
    search-light@icedman.github.com arcmenu@arcmenu.com caffeine@patapon.info \
    clipboard-indicator@tudmotu.com colortint@matt.serverus.co.uk \
    compiz-alike-magic-lamp-effect@hermes83.github.com CoverflowAltTab@palatis.blogspot.com \
    gtk4-ding@smedius.gitlab.com monitor@astraext.github.io freon@UshakovVasilii_Github.yahoo.com \
    freq-boost-switch@metal03326 Hide_Activities@shay.shayel.org HideItems@fablevi.github.io \
    impatience@gfxmonk.net no-overview@fthx running-apps@coates System_Monitor@bghome.gmail.com \
    osd-volume-number@deminder panelnote@gittymac.github.io top-bar-organizer@julian.gse.jsts.xyz \
    useless-gaps@pimsnel.com waylandorx11@injcristianrojas.github.com show-desktop-button@amivaleo \
    AlphabeticalAppGrid@stuarthayhurst logomenu@aryan_k bluetooth-quick-connect@bjarosze.gmail.com; do
    gnome-extensions disable "$uuid" 2>/dev/null
    gnome-extensions uninstall "$uuid" 2>/dev/null
    rm -rf "$HOME/.local/share/gnome-shell/extensions/$uuid"
done

echo "== Removing added cursor/icon themes =="
rm -rf "$HOME/.icons/Cyberpunk-Neon"
rm -rf "$HOME/.icons/Tela"* "$HOME/.local/share/icons/Tela"*
rm -rf "$HOME/.local/share/icons/Vimix"*
rm -rf "$HOME/.local/share/icons/Suru++"*

echo "== Removing Gradience/libadwaita neon overrides =="
rm -f "$HOME/.config/gtk-4.0/gtk.css" "$HOME/.config/gtk-4.0/gtk-dark.css"

echo "== Removing kitty config (kitty had none before the rice) =="
rm -f "$HOME/.config/kitty/kitty.conf"
rmdir "$HOME/.config/kitty" 2>/dev/null

echo "== Removing the Nerd Font pack =="
rm -f "$HOME"/.local/share/fonts/JetBrainsMono*NerdFont*.ttf
fc-cache -f "$HOME/.local/share/fonts" >/dev/null 2>&1

echo "== Removing the extra 'Cyberpunk Neon' gnome-terminal profile =="
# The profile UUID is not recoverable after the original backup was
# deleted; this removes it by name instead.
LIST=$(gsettings get org.gnome.Terminal.ProfilesList list)
python3 - "$LIST" <<'PYEOF'
import ast, subprocess, sys
lst = ast.literal_eval(sys.argv[1])
default = None
for uuid in list(lst):
    name = subprocess.run(
        ["dconf", "read", f"/org/gnome/terminal/legacy/profiles:/:{uuid}/visible-name"],
        capture_output=True, text=True).stdout.strip()
    if name == "'Cyberpunk Neon'":
        lst.remove(uuid)
        subprocess.run(["dconf", "reset", "-f", f"/org/gnome/terminal/legacy/profiles:/:{uuid}/"])
subprocess.run(["gsettings", "set", "org.gnome.Terminal.ProfilesList", "list", str(lst)])
PYEOF

echo "== Uninstalling added apps (asks for confirmation) =="
read -p "Remove gnome-shell-extension-manager (apt) and Gradience (flatpak)? [y/N] " ans
if [[ "$ans" =~ ^[Yy]$ ]]; then
    sudo apt remove -y gnome-shell-extension-manager
    flatpak uninstall -y com.github.GradienceTeam.Gradience
fi

echo
echo "Done. Log out and back in (or restart GNOME Shell) for all changes to take full effect."

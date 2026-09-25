<div align="center">

```
   ▄████  ██▓     ▒█████   █     █░ ██▓ ███▄    █  ██▓███   █    ██  ███▄    █  ██ ▄█▀
  ██▒ ▀█▒▓██▒    ▒██▒  ██▒▓█░ █ ░█░▓██▒ ██ ▀█   █ ▓██░  ██▒ ██  ▓██▒ ██ ▀█   █  ██▄█▒
 ▒██░▄▄▄░▒██░    ▒██░  ██▒▒█░ █ ░█ ▒██▒▓██  ▀█ ██▒▓██░ ██▓▒▓██  ▒██░▓██  ▀█ ██▒▓███▄░
 ░▓█  ██▓▒██░    ▒██   ██░░█░ █ ░█ ░██░▓██▒  ▐▌██▒▒██▄█▓▒ ▒▓▓█  ░██░▓██▒  ▐▌██▒▓██ █▄
 ░▒▓███▀▒░██████▒░ ████▓▒░░░██▒██▓ ░██░▒██░   ▓██░▒██▒ ░  ░▒▒█████▓ ▒██░   ▓██░▒██▒ █▄
  ░▒   ▒ ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▓░▒ ▒  ░▓  ░ ▒░   ▒ ▒ ▒▓▒░ ░  ░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒
   ░   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ▒ ░ ░   ▒ ░░ ░░   ░ ▒░░▒ ░     ░░▒░ ░ ░ ░ ░░   ░ ▒░░ ░▒ ▒░
 ░ ░   ░   ░ ░   ░ ░ ░ ▒    ░   ░   ▒ ░   ░   ░ ░ ░░        ░░░ ░ ░    ░   ░ ░ ░ ░░ ░
       ░     ░  ░    ░ ░      ░     ░           ░                 ░           ░  ░
                          ▓█████▄  █    ██  ███▄    █  ██ ▄█▀
                          ▒██▀ ██▌ ██  ▓██▒ ██ ▀█   █  ██▄█▒
                          ░██   █▌▓██  ▒██░▓██  ▀█ ██▒▓███▄░
                          ░▓█▄   ▌▓▓█  ░██░▓██▒  ▐▌██▒▓██ █▄
                          ░▒████▓ ▒▒█████▓ ▒██░   ▓██░▒██▒ █▄
                           ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒
                           ░ ▒  ▒ ░░▒░ ░ ░ ░ ░░   ░ ▒░░ ░▒ ▒░
                           ░ ░  ░  ░░░ ░ ░    ░   ░ ░ ░ ░░ ░
                             ░       ░              ░ ░  ░
```

### `. : . . : <[ N30N // 0N // ALL // D4Y ]> : . : .`

**A GNOME 46 (Ubuntu 24.04) desktop rice — neon-on-black, glass panels, and a
window border that tells you which app you're looking at from across the
room.**

[![Shell](https://img.shields.io/badge/GNOME-46-00F0FF?style=for-the-badge&logo=gnome&logoColor=black&labelColor=0A0A12)](https://www.gnome.org/)
[![Distro](https://img.shields.io/badge/Ubuntu-24.04-FF2E97?style=for-the-badge&logo=ubuntu&logoColor=black&labelColor=0A0A12)](https://ubuntu.com/)
[![Vibe](https://img.shields.io/badge/vibe-cyberpunk-BD00FF?style=for-the-badge&labelColor=0A0A12)](#)
[![Private](https://img.shields.io/badge/repo-private-05FFA1?style=for-the-badge&labelColor=0A0A12)](#)

</div>

---

## ⚡ What this is

A from-scratch GNOME shell rice built for an arm64 NVIDIA DGX Spark box
(Ubuntu 24.04 / GNOME 46), styled entirely inside GNOME's own extension and
theming stack — no Hyprland, no wlroots, no custom compositor. That path was
evaluated and ruled out: this SoC's NVIDIA driver ships with
`nvidia-drm.modeset=0` forced by the vendor image, and GNOME/X11 was already
stable, so the rice works *with* GNOME instead of replacing it.

No two colors on this desktop are an accident. Every accent — panel, dock,
terminal, per-app window border — pulls from one fixed neon palette, and
nothing gets added to that palette in a shade that doesn't already glow.

## 🎨 Palette

| Color | Hex | Used for |
|---|---|---|
| ![#00F0FF](https://placehold.co/18x18/00F0FF/00F0FF.png) Cyan | `#00F0FF` | gnome-terminal border, global/default window border, accents |
| ![#FF2E97](https://placehold.co/18x18/FF2E97/FF2E97.png) Magenta | `#FF2E97` | Firefox border, dock running-indicator, active tab |
| ![#BD00FF](https://placehold.co/18x18/BD00FF/BD00FF.png) Purple | `#BD00FF` | Obsidian border |
| ![#05FFA1](https://placehold.co/18x18/05FFA1/05FFA1.png) Green | `#05FFA1` | kitty border + kitty ANSI green |
| ![#F9F871](https://placehold.co/18x18/F9F871/F9F871.png) Yellow | `#F9F871` | VS Code border |
| ![#FF6A00](https://placehold.co/18x18/FF6A00/FF6A00.png) Orange | `#FF6A00` | Files (Nautilus) border |
| ![#FF2E63](https://placehold.co/18x18/FF2E63/FF2E63.png) Red | `#FF2E63` | DGX Dashboard border |
| ![#0A0A12](https://placehold.co/18x18/0A0A12/0A0A12.png) Near-black | `#0A0A12` | every background |

## 🧩 Stack

| Layer | Choice | Why |
|---|---|---|
| GTK / Shell theme | `Yaru-magenta-dark` | Ships with Ubuntu, guaranteed GNOME 46-safe, closest built-in neon accent |
| Icons | [Suru++](https://github.com/gusbemacbe/suru-plus) | Explicitly cyberpunk-branded, 5300+ app icons — actually covers Obsidian/VS Code/NVIDIA tooling, unlike most "neon" packs |
| Cursor | [Cyberpunk-Neon](https://github.com/ayushkrsingh/cyberpunk-neon-cursors) | Purpose-built neon cursor, native X11/Wayland support |
| Libadwaita overrides | hand-written `gtk.css` | Gradience-style `@define-color` overrides for GTK4 app windows |
| Dock | Ubuntu Dock (`dash-to-dock`) | Bottom, always-visible, translucent, recolored running-indicators |
| Window borders | Rounded Window Corners Reborn | Per-app neon border via `custom-rounded-corner-settings`, keyed by `wm_class_instance` |
| Panel effects | Blur My Shell | Blurred/tinted panel, dock, overview |
| System monitor | Astra Monitor | Recolored to the palette, GPU indicator *disabled* — this SoC's driver doesn't expose GPU stats in a format it can parse |
| Terminal | gnome-terminal + kitty | Both carry the full 16-color neon ANSI palette |
| Font | JetBrainsMono Nerd Font Mono | Glyph-safe monospace variant for prompt icons |

30 GNOME Shell extensions in total — see `restore_script.sh` for the full
list of UUIDs.

## 🪟 Per-app window borders

Every window gets a border color the moment it's created, keyed by its real
`WM_CLASS` (checked with `xprop`, never guessed):

```
Firefox (Navigator)        → magenta
Obsidian (md.obsidian.*)   → purple
gnome-terminal-server      → cyan
kitty                      → green
VS Code (code)             → yellow
Nautilus (org.gnome.*)     → orange
DGX Dashboard              → red
anything else              → cyan (global default)
```

New software gets the cyan default automatically. Add an app by editing
`custom-rounded-corner-settings` in the Rounded Window Corners Reborn schema
— see the extension's own prefs UI, or `gsettings --schemadir` directly.

> **Note:** a colored *glow* (blurred halo instead of a flat border line)
> was attempted by patching the extension's shadow renderer to use the
> border color instead of hardcoded black. It caused window-actor
> corruption (`already disposed` errors) on live toggle and was reverted.
> The extension's shadow color is hardcoded upstream — flat neon borders
> are the stable ceiling here without a deeper, riskier patch.

## 📦 Install

This repo isn't a one-shot installer — it's the reference config plus a full
uninstaller. The actual build was interactive (checking GNOME-version
compatibility per extension, verifying real `WM_CLASS` values, etc.), which
doesn't compress into a single script safely. Treat `config/` as the
dotfiles to drop in, and the extension/UUID list in `restore_script.sh` as
the shopping list for Extension Manager.

```bash
# dotfiles
cp config/kitty/kitty.conf       ~/.config/kitty/kitty.conf
cp config/gtk-4.0/gtk.css        ~/.config/gtk-4.0/gtk.css
cp config/gtk-4.0/gtk-dark.css   ~/.config/gtk-4.0/gtk-dark.css
```

## ⏮ Restore

```bash
./restore_script.sh
```

Fully reverts the rice: resets every `gsettings` key touched, disables and
uninstalls all 28 added extensions, removes the added icon/cursor themes and
font, and deletes the added config files. Asks before removing the two
installed packages (Extension Manager, Gradience). Originally built and
tested against a live dconf snapshot taken before the rice was applied.

## 🖥 Hardware note

Built on an **NVIDIA DGX Spark** (GB10, aarch64, unified CPU/GPU memory) —
not a normal desktop GPU. If you're on the same hardware: `nvidia-drm.modeset`
is forced to `0` by `/etc/modprobe.d/zz-nvidia-drm-override.conf` in the
vendor image, on top of the driver's own default of `1`. That's why this
rice stays on X11/GNOME instead of a wlroots compositor, and why GPU
monitoring extensions don't work out of the box.

---

<div align="center">

`🪐 built with a lot of gsettings and one very patient GPU 🪐`

</div>

# Ghostty — GlowinPunk theme

Cyberpunk neon theme for [Ghostty](https://ghostty.org), tuned for long
reading sessions: every ANSI color is >= 6:1 contrast on the `#0b0f1a`
background (WCAG), and `minimum-contrast = 4.5` stops any program from
rendering text below AA.

## Install

```bash
bash config/ghostty/install.sh
```

Copies `config.ghostty` and `shaders/` to the paths below. On macOS it also
installs the app icon to `~/.config/ghostty/Ghostty.icns` (Ghostty's default
custom-icon location):

| OS | Path |
|---|---|
| macOS | `~/Library/Application Support/com.mitchellh.ghostty/` |
| Linux | `~/.config/ghostty/` |

Existing configs are backed up first. Reload with `Cmd+Shift+,` (macOS) or
`Ctrl+Shift+,` (Linux), then open a new tab.

## What's in it

- **Palette:** deep navy background, neon cyan / green / magenta / yellow,
  blue and bright-black lifted so they stay readable.
- **Cursor:** blinking magenta underscore. Shell integration's `cursor`
  feature is disabled, otherwise Ghostty forces a bar cursor at the prompt.
- **Text:** JetBrains Mono (Ghostty's bundled default), 13pt, slight extra
  line height and letter spacing to tell `O/0` and `l/1/I` apart.
- **SSH:** `term = xterm-256color` and `ssh-env` avoid typing that overwrites
  characters on remote hosts that lack the `xterm-ghostty` terminfo. `ssh-terminfo`
  stays off so nothing is installed on systems you assess. Delete the `term` line
  to go back to `xterm-ghostty`.
- **Icon:** custom ninja-cat app icon (see below).
- **Glass:** 0.94 background opacity + blur. Set `background-opacity = 1` for
  screen sharing.

## App icon (`icon/`)

A cyberpunk ninja cat for the Dock / Cmd+Tab (macOS, `macos-icon = custom`):
black cat with glowing cyan eyes, a red headband whose plate shows a `>_`
prompt, a ninja mask, a red moon and a neon skyline, in the same red + cyan
palette. It only changes the Dock and app switcher; Finder keeps the original.

| Path | What |
|---|---|
| `icon/Ghostty.icns` | The installed icon |
| `icon/ninja-cat.svg` | Source art |
| `icon/build-ninja-cat.py` | Generates `ninja-cat.svg` (`python3 build-ninja-cat.py`) |
| `icon/make-icns.sh` | SVG to `.icns` (`bash make-icns.sh in.svg out.icns`, needs `librsvg`) |
| `icon/alt/` | Earlier designs as SVG: red-team oni variants and the neon oni |

To switch designs: `bash icon/make-icns.sh icon/alt/oni-pretty.svg ~/.config/ghostty/Ghostty.icns`,
then reload Ghostty (or reopen it).

## Shaders (`shaders/`)

Applied in this order. Each is additive-only, so text is never altered.
Tunables are `#define`s at the top of each file. Comment a `custom-shader`
line out of `config.ghostty` to disable one.

| File | Effect |
|---|---|
| `neon-border.glsl` | Thin 1px lime-green frame with a barely-there glow just inside the window edge (`#39ff14`) |
| `cursor-trail.glsl` | Underscore cursor glides between positions with a neon smear |
| `neon-glow.glsl` | Subtle bloom around bright text and the cursor |

## Shortcuts (Ghostty defaults, macOS)

| Action | Shortcut |
|---|---|
| Split right / down | `Cmd+D` / `Cmd+Shift+D` |
| Close current split | `Cmd+W` |
| Next / previous split | `Cmd+]` / `Cmd+[` |
| Move between splits | `Cmd+Option+arrows` |
| Resize split | `Cmd+Ctrl+arrows` |
| Equalize splits | `Cmd+Ctrl+=` |
| Zoom split | `Cmd+Shift+Enter` |
| Font size | `Cmd+Plus` / `Cmd+Minus` / `Cmd+0` |

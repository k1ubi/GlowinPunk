# Ghostty — GlowinPunk theme

Cyberpunk neon theme for [Ghostty](https://ghostty.org), tuned for long
reading sessions: every ANSI color is >= 6:1 contrast on the `#0b0f1a`
background (WCAG), and `minimum-contrast = 4.5` stops any program from
rendering text below AA.

## Install

```bash
bash config/ghostty/install.sh
```

Copies `config.ghostty` and `shaders/` to:

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
- **Glass:** 0.94 background opacity + blur. Set `background-opacity = 1` for
  screen sharing.

## Shaders (`shaders/`)

Applied in this order. Each is additive-only, so text is never altered.
Tunables are `#define`s at the top of each file. Comment a `custom-shader`
line out of `config.ghostty` to disable one.

| File | Effect |
|---|---|
| `neon-border.glsl` | Lime-green frame just inside the window edge (`#39ff14`) |
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

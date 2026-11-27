```
0xkyubi@lab:~/GlowinPunk $ whoami
──────────────────────────────────────────────────────────────────
GNOME 46 cyberpunk rice — neon-on-black, glass panels,
and a window border that reads from across the room.
```

**`// palette`**

| hex | used for |
|---|---|
| `#00F0FF` | terminal · default window border |
| `#FF2E97` | Firefox · active tab |
| `#BD00FF` | Obsidian |
| `#05FFA1` | kitty · ANSI green |
| `#F9F871` | VS Code |
| `#FF6A00` | Nautilus |
| `#0A0A12` | every background |

**`// stack`**

| layer | choice |
|---|---|
| GTK / Shell theme | `Yaru-magenta-dark` |
| Icons + cursor | Cyberpunk-Neon |
| Libadwaita overrides | hand-written `gtk.css` |
| Window borders | Rounded Window Corners Reborn |
| Panel effects | Blur My Shell |
| Dock | Ubuntu Dock (`dash-to-dock`) |
| Terminal | kitty + tmux (auto-starts on open) |
| Font | JetBrainsMono Nerd Font Mono |

**`// per-app borders`**

```
Firefox (Navigator)       → magenta  #FF2E97
Obsidian (md.obsidian.*)  → purple   #BD00FF
gnome-terminal-server     → cyan     #00F0FF
kitty                     → green    #05FFA1
VS Code (code)            → yellow   #F9F871
Nautilus (org.gnome.*)    → orange   #FF6A00
everything else           → cyan     #00F0FF  (default)
```

**`// terminal shortcuts`**

tmux splits via `Win+*` mapped through kitty — no prefix key needed:

| action | shortcut |
|---|---|
| split horizontally | `Win+B` |
| split vertically | `Win+R` |
| close pane (no confirm) | `Win+D` |

**`// install`**

```bash
cp config/kitty/kitty.conf       ~/.config/kitty/kitty.conf
cp config/tmux/tmux.conf         ~/.config/tmux/tmux.conf
cp config/gtk-4.0/gtk.css        ~/.config/gtk-4.0/gtk.css
cp config/gtk-4.0/gtk-dark.css   ~/.config/gtk-4.0/gtk-dark.css
```

Free `Super+D` from show-desktop if the tmux shortcut conflicts:

```bash
gsettings set org.gnome.desktop.wm.keybindings show-desktop \
  "['<Primary><Super>d', '<Primary><Alt>d']"
```

**`// restore`**

```bash
./restore_script.sh
```

Reverts everything — resets all `gsettings` keys, disables and uninstalls all 28 extensions, removes themes, fonts, and config files.

---

`.: . . : <[ end of transmission ]> : . :.`

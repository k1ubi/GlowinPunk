#!/usr/bin/env python3
"""
Set all window borders to NVIDIA green #76b900.
Uses the global rounded-corner setting so every window gets the same color.
Clears per-app overrides (they'd shadow the global color).
"""
import gi
gi.require_version('Gio', '2.0')
from gi.repository import Gio, GLib

SCHEMA_DIR = '/home/kyubi/.local/share/gnome-shell/extensions/rounded-window-corners@fxgn/schemas'
SCHEMA_ID  = 'org.gnome.shell.extensions.rounded-window-corners-reborn'

source   = Gio.SettingsSchemaSource.new_from_directory(
    SCHEMA_DIR, Gio.SettingsSchemaSource.get_default(), False)
settings = Gio.Settings.new_full(source.lookup(SCHEMA_ID, True), None, None)

# NVIDIA green #76b900 → (118/255, 185/255, 0, 1)
NV_COLOR = [118/255, 185/255, 0.0, 1.0]

def rebuild_corner_settings(source_variant):
    """
    Return a copy of an a{sv} corner-settings variant with:
      - borderColor = #76b900
      - keepRoundedCorners.maximized = true  (show border on maximized windows)
    """
    builder = GLib.VariantBuilder.new(GLib.VariantType.new('a{sv}'))
    for i in range(source_variant.n_children()):
        child   = source_variant.get_child_value(i)
        key_var = child.get_child_value(0)
        key     = key_var.get_string()

        if key == 'borderColor':
            entry = GLib.Variant.new_dict_entry(
                key_var,
                GLib.Variant('v', GLib.Variant('ad', NV_COLOR))
            )
        elif key == 'keepRoundedCorners':
            inner_val = child.get_child_value(1).get_variant()  # a{sv}
            ib = GLib.VariantBuilder.new(GLib.VariantType.new('a{sv}'))
            for j in range(inner_val.n_children()):
                ic   = inner_val.get_child_value(j)
                ik   = ic.get_child_value(0)
                if ik.get_string() == 'maximized':
                    ib.add_value(GLib.Variant.new_dict_entry(
                        ik, GLib.Variant('v', GLib.Variant('b', True))))
                else:
                    ib.add_value(ic)
            entry = GLib.Variant.new_dict_entry(
                key_var, GLib.Variant('v', ib.end()))
        else:
            entry = child

        builder.add_value(entry)
    return builder.end()

# ── global ─────────────────────────────────────────────────────────────────────
glob     = settings.get_value('global-rounded-corner-settings')
new_glob = rebuild_corner_settings(glob)
settings.set_value('global-rounded-corner-settings', new_glob)
print("Global borderColor → #76b900, keepRoundedCorners.maximized → true")

# ── clear per-app overrides (so global applies uniformly) ──────────────────────
settings.set_value('custom-rounded-corner-settings',
                   GLib.Variant('a{sv}', {}))
print("Per-app overrides cleared (global color applies to all windows)")

# ── border width ───────────────────────────────────────────────────────────────
settings.set_int('border-width', 3)
print("border-width → 3")
print("Done. Restart GNOME Shell if borders don't update immediately.")

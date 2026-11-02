#!/usr/bin/env python3
"""Add a neon green glow pipeline to blur-my-shell and apply it to the dock."""
import gi
gi.require_version('Gio', '2.0')
from gi.repository import Gio, GLib

SCHEMA_DIR = '/home/kyubi/.local/share/gnome-shell/extensions/blur-my-shell@aunetx/schemas'

source = Gio.SettingsSchemaSource.new_from_directory(
    SCHEMA_DIR,
    Gio.SettingsSchemaSource.get_default(),
    False
)

main_schema = source.lookup('org.gnome.shell.extensions.blur-my-shell', True)
main_settings = Gio.Settings.new_full(main_schema, None, None)

current_pipelines = main_settings.get_value('pipelines')  # a{sa{sv}}

# NVIDIA green #76b900 → (118/255, 185/255, 0)
NV_R, NV_G, NV_B = 118/255, 185/255, 0.0
PIPELINE_KEY = 'pipeline_nv_dock_glow'

# Each effect is a{sv} with variant-wrapped values
blur_effect = GLib.Variant('a{sv}', {
    'type':   GLib.Variant('v', GLib.Variant('s', 'dual_kawase_blur')),
    'id':     GLib.Variant('v', GLib.Variant('s', 'nv_dock_blur')),
    'params': GLib.Variant('v', GLib.Variant('a{sv}', {
        'unscaled_radius': GLib.Variant('v', GLib.Variant('i', 18)),
        'brightness':      GLib.Variant('v', GLib.Variant('d', 0.55)),
    })),
})

color_effect = GLib.Variant('a{sv}', {
    'type':   GLib.Variant('v', GLib.Variant('s', 'color')),
    'id':     GLib.Variant('v', GLib.Variant('s', 'nv_dock_color')),
    'params': GLib.Variant('v', GLib.Variant('a{sv}', {
        'color':      GLib.Variant('v', GLib.Variant('(dddd)', (NV_R, NV_G, NV_B, 0.22))),
        'blend_mode': GLib.Variant('v', GLib.Variant('i', 17)),
    })),
})

# Pipeline value is a{sv}: name + effects list
# effects value in a{sv} must be a variant wrapping av
new_pipeline_val = GLib.Variant('a{sv}', {
    'name':    GLib.Variant('v', GLib.Variant('s', 'NV Green Glow Dock')),
    'effects': GLib.Variant('v', GLib.Variant('av', [
        GLib.Variant('v', blur_effect),
        GLib.Variant('v', color_effect),
    ])),
})

# Build new a{sa{sv}} using VariantBuilder
builder = GLib.VariantBuilder.new(GLib.VariantType.new('a{sa{sv}}'))
for i in range(current_pipelines.n_children()):
    child = current_pipelines.get_child_value(i)
    key = child.get_child_value(0).get_string()
    if key != PIPELINE_KEY:
        builder.add_value(child)

# Add new entry as {sa{sv}} using new_dict_entry to accept pre-built Variants
new_entry = GLib.Variant.new_dict_entry(
    GLib.Variant('s', PIPELINE_KEY),
    new_pipeline_val
)
builder.add_value(new_entry)

new_pipelines = builder.end()
ok = main_settings.set_value('pipelines', new_pipelines)
print(f"Pipelines set: {ok}")

# ── Dash-to-dock blur settings ─────────────────────────────────────────────────
dock_schema = source.lookup('org.gnome.shell.extensions.blur-my-shell.dash-to-dock', True)
dock_settings = Gio.Settings.new_full(dock_schema, None, None)

dock_settings.set_boolean('blur', True)
dock_settings.set_boolean('customize', True)
dock_settings.set_boolean('static-blur', False)
dock_settings.set_boolean('override-background', True)
dock_settings.set_string('pipeline', PIPELINE_KEY)
dock_settings.set_double('brightness', 0.55)
dock_settings.set_int('sigma', 18)

print("Dock pipeline set to:", dock_settings.get_string('pipeline'))
print("Done.")

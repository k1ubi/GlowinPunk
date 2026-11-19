#!/usr/bin/env bash
# Build a macOS .icns from an SVG (needs rsvg-convert: brew install librsvg).
# Usage: bash make-icns.sh ninja-cat.svg Ghostty.icns
set -euo pipefail
SVG="${1:?usage: make-icns.sh input.svg output.icns}"; OUT="${2:?usage: make-icns.sh input.svg output.icns}"
SET="$(mktemp -d)/Ghostty.iconset"; mkdir -p "$SET"
for sz in 16 32 128 256 512; do
  rsvg-convert -w $sz -h $sz "$SVG" -o "$SET/icon_${sz}x${sz}.png"
  rsvg-convert -w $((sz*2)) -h $((sz*2)) "$SVG" -o "$SET/icon_${sz}x${sz}@2x.png"
done
iconutil -c icns "$SET" -o "$OUT"
echo "Wrote $OUT"

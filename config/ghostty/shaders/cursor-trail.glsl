// Cursor glide trail for an underline (underscore) cursor.
//
// When the cursor moves, a bar in the cursor's color stretches from the old
// position and quickly shrinks into the new one, with a soft neon halo.
//
// Readability:
//   - Purely additive and only lives for TRAIL_DURATION seconds after a move,
//     then vanishes completely; a resting cursor is untouched.
//   - Confined to a thin strip at the bottom of the cell, so it never covers
//     the characters you're reading.
//
// Tune:
#define TRAIL_DURATION 0.18   // seconds the trail lasts (0.10 snappy ... 0.30 floaty)
#define TRAIL_STRENGTH 0.9    // brightness of the trail core
#define HALO_STRENGTH 0.35    // brightness of the soft glow around it
#define BAR_THICKNESS 4.0     // trail thickness in physical pixels (~2 per point on Retina)

// Distance from point p to segment a-b.
float sdSegment(vec2 p, vec2 a, vec2 b) {
    vec2 pa = p - a;
    vec2 ba = b - a;
    float h = clamp(dot(pa, ba) / max(dot(ba, ba), 1e-6), 0.0, 1.0);
    return length(pa - ba * h);
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    vec2 uv = fragCoord / iResolution.xy;
    vec4 base = texture(iChannel0, uv);
    fragColor = base;

    // Cursor rects: .xy = top-left corner (y-up), .zw = width, height.
    vec4 cur = iCurrentCursor;
    vec4 prev = iPreviousCursor;

    // No valid previous cursor yet (startup) -> nothing to animate.
    if (prev.z < 1.0 || prev.w < 1.0 || cur.z < 1.0 || cur.w < 1.0) {
        return;
    }

    float t = (iTime - iTimeCursorChange) / TRAIL_DURATION;
    if (t >= 1.0 || t < 0.0) {
        return;
    }

    // Bottom strip of each cursor rect; works whether the reported rect is the
    // whole cell or just the thin underline.
    float thick = min(cur.w, BAR_THICKNESS);
    vec2 curC  = vec2(cur.x + cur.z * 0.5,   cur.y - cur.w + thick * 0.5);
    vec2 prevC = vec2(prev.x + prev.z * 0.5, prev.y - prev.w + thick * 0.5);

    // Ignore blink toggles / redraws where the cursor didn't actually move.
    if (distance(curC, prevC) < 1.0) {
        return;
    }

    // The tail eases from the old position into the new one.
    float e = 1.0 - pow(1.0 - t, 3.0);
    vec2 tail = mix(prevC, curC, e);

    // Stretch x so a cell-wide bar becomes a round capsule, then take distance.
    float k = thick / cur.z;
    vec2 p = vec2(fragCoord.x * k, fragCoord.y);
    float d = sdSegment(p, vec2(tail.x * k, tail.y), vec2(curC.x * k, curC.y)) - thick * 0.5;

    float fade = 1.0 - t;
    float core = (1.0 - smoothstep(-0.5, 1.0, d)) * TRAIL_STRENGTH;
    float halo = (1.0 - smoothstep(0.0, thick * 3.0, d)) * HALO_STRENGTH;
    float a = (core + halo) * fade;

    vec3 col = iCurrentCursorColor.rgb;
    vec3 rgb = min(base.rgb + col * a, vec3(1.0));
    fragColor = vec4(rgb, max(base.a, a));
}

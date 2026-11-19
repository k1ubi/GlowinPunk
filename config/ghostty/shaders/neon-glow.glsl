// Subtle neon bloom for Ghostty.
//
// Safety properties (for readability):
//   - The original pixel is never modified or darkened; glow is purely additive.
//   - Only bright/saturated pixels (text, cursor) emit glow; the dark background
//     does not, so large flat areas are untouched.
//   - Glow is tinted by the emitting pixel's own color (cyan text -> cyan halo).
//
// Tune these three values:
#define GLOW_STRENGTH 0.55   // overall intensity. 0.0 = off, ~0.3 very faint, ~1.0 strong
#define GLOW_THRESHOLD 0.45  // brightness a pixel needs before it glows (higher = only the brightest)
#define GLOW_RADIUS 1.0      // halo size multiplier (1.0 = ~2-6px)

float luma(vec3 c) {
    return dot(c, vec3(0.2126, 0.7152, 0.0722));
}

// Contribution of one tap: emitted color, gated by brightness.
vec3 tap(vec2 uv) {
    vec3 c = texture(iChannel0, clamp(uv, vec2(0.0), vec2(1.0))).rgb;
    float g = smoothstep(GLOW_THRESHOLD, 0.95, luma(c));
    return c * g;
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    vec2 uv = fragCoord / iResolution.xy;
    vec4 base = texture(iChannel0, uv);

    vec2 px = GLOW_RADIUS / iResolution.xy;

    // Two rings of 8 taps (inner ~2px, outer ~5px), weighted toward the center.
    const vec2 dirs[8] = vec2[8](
        vec2( 1.0,  0.0), vec2(-1.0,  0.0), vec2( 0.0,  1.0), vec2( 0.0, -1.0),
        vec2( 0.7071,  0.7071), vec2(-0.7071,  0.7071),
        vec2( 0.7071, -0.7071), vec2(-0.7071, -0.7071)
    );

    vec3 inner = vec3(0.0);
    vec3 outer = vec3(0.0);
    for (int i = 0; i < 8; i++) {
        inner += tap(uv + dirs[i] * px * 2.0);
        outer += tap(uv + dirs[i] * px * 5.0);
    }
    inner /= 8.0;
    outer /= 8.0;

    vec3 glow = (inner * 0.6 + outer * 0.4) * GLOW_STRENGTH;

    vec3 rgb = base.rgb + glow;
    // Keep alpha at least as opaque as the glow so it shows over a transparent background.
    float a = max(base.a, max(glow.r, max(glow.g, glow.b)));
    fragColor = vec4(min(rgb, vec3(1.0)), a);
}

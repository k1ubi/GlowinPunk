// Lime green frame just inside the window edge.
//
// Readability:
//   - The line sits in the window padding (14px+), well clear of text.
//   - The inner glow fades out within ~PADDING px, so it never reaches the text area.
//   - Purely additive; text pixels are never altered.
//
// Tune (all in physical pixels; Retina is 2 px per point):
#define BORDER_COLOR vec3(0.224, 1.0, 0.078)   // #39ff14 lime/electric green
#define LINE_WIDTH 2.0       // crisp core line thickness
#define LINE_INSET 1.0       // gap from the very edge (keeps it clear of rounded-corner clipping)
#define GLOW_WIDTH 18.0      // how far the soft inner glow reaches (keep under your padding)
#define LINE_STRENGTH 0.9    // brightness of the line
#define GLOW_STRENGTH 0.22   // brightness of the soft glow

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    vec2 uv = fragCoord / iResolution.xy;
    vec4 base = texture(iChannel0, uv);

    // Distance in pixels to the nearest window edge, minus the inset.
    vec2 edge = min(fragCoord, iResolution.xy - fragCoord);
    float d = min(edge.x, edge.y) - LINE_INSET;

    float line = 1.0 - smoothstep(LINE_WIDTH - 1.0, LINE_WIDTH, d);
    line *= step(0.0, d + 1.0);   // nothing outside the inset
    float glow = pow(1.0 - clamp(d / GLOW_WIDTH, 0.0, 1.0), 2.0) * GLOW_STRENGTH;

    float a = line * LINE_STRENGTH + glow;
    vec3 rgb = min(base.rgb + BORDER_COLOR * a, vec3(1.0));
    fragColor = vec4(rgb, max(base.a, min(a, 1.0)));
}

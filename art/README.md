# Profile illustrations

I use drawings to explain one engineering question at a time. The profile's
masthead introduces my broader background; the project illustrations give a
visitor a reason to inspect the actual experiment. I used AI assistance to
build this generator, as with the projects it illustrates.

## Rebuild

```sh
python -m pip install -r art/requirements.txt
python art/build.py
python art/build.py --check
```

The generator produces eight SVGs: a masthead and three project illustrations,
each with a wide and narrow layout. The README selects the narrow layout below
600 px. Each SVG supports light and dark color schemes and is static, so there
is no motion to pause. The first build downloads the fonts; viewing the drawings
requires no font downloads or JavaScript.

## What the drawings represent

- `hero.py` draws the typographic masthead. It makes no measurement claim.
- `plates.py` draws the project illustrations. The recovery comparison shows
  the recorded controller-crash outcomes in
  [the lab's traces](https://github.com/B8Z/device-recovery-lab/blob/main/demo/traces.json):
  zero and one simulated physical pulses, both with journal state `IN_DOUBT`.
  These are explanatory drawings, not photographs or backend controls.
- The placement comparison depicts the tighter-deadline fixture in
  [the recorded experiment](https://github.com/B8Z/placement-tradeoffs/tree/main/measurements):
  greedy places C for objective 23; D and E reach 27. The capacity units are
  synthetic model units, not hardware measurements.
- The thesis illustration in the research note is a schematic, not a historical
  research result. The thesis is from 2022; this artwork is from October 2026.

`cabinet.py` and `svgkit.py` provide the geometry, `theme.py` the palettes, and
`typeset.py` the text outlines. Native Markdown headings, explanatory prose,
and image alternatives keep the profile readable without the artwork.

## Typography and references

Text is converted to outlines using Newsreader, Manrope, and JetBrains Mono.
These typefaces use the SIL Open Font License 1.1. `fonts.py` pins the
[Google Fonts](https://github.com/google/fonts) source revision and verifies
SHA-256 hashes. Font files are cached in `art/.fonts/` and are not committed.
See [font attribution](FONT-NOTICES.md).

The design references are [Pentagram's Cooper Hewitt identity](https://www.pentagram.com/news/cooper-hewitt-a-democratic-design-identity)
for a clear hierarchy and consistent visual vocabulary, and
[Bartosz Ciechanowski's technical essays](https://ciechanow.ski/mechanical-watch/)
for illustrations that explain a mechanism alongside the text. The drawings
and layout here were constructed for these projects; no reference artwork,
branding, or code was copied.

`build.py --check` ignores line-ending differences and optional `<metadata>`
Content Credentials manifests because neither changes the drawing.

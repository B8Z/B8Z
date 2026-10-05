"""Palette tokens as CSS custom properties.

The light values follow the Device Recovery Lab viewer, so the profile and the
project it leads to read as one piece of work. Each SVG carries both palettes
and switches with the viewer's color-scheme preference.
"""
LIGHT = dict(
    ground="#f5f2e9", ink="#242620", muted="#62635b", wash="#ece8dd",
    door="#dcd6c9", inset="#e8e2d5", hatch="#c9c7ba", accent="#b9381d", accent_fill="#c4472c",
    accent_inset="#db7559", confirmed="#365746", inner_back="#242620", inner_wall="#44473e",
    inner_floor="#76776e", parcel="#f5f2e9", parcel_front="#d5cbbb", parcel_side="#e8e0d1",
    parcel_line="#242620", screen="#242620", screen_ink="#f5f2e9", shadow="#e6e2d6",
)
DARK = dict(
    ground="#14161b", ink="#ebe7da", muted="#a3a296", wash="#22242a",
    door="#2a2d33", inset="#32353c", hatch="#40434a", accent="#f0694b", accent_fill="#d9502f",
    accent_inset="#f08c72", confirmed="#8fd0a8", inner_back="#08090b", inner_wall="#15171b",
    inner_floor="#3a3d42", parcel="#efe9da", parcel_front="#c9bfac", parcel_side="#ddd4c3",
    parcel_line="#4a4335", screen="#08090b", screen_ink="#ebe7da", shadow="#0d0f13",
)
# Drawing code refers to tokens, never to literal colors.
T = {name: f"var(--{name.replace('_', '-')})" for name in LIGHT}


def _block(values):
    return "".join(f"--{k.replace('_', '-')}:{v};" for k, v in values.items())


def css():
    return (f"svg{{{_block(LIGHT)}}}"
            f"@media (prefers-color-scheme:dark){{svg{{{_block(DARK)}}}}}"
            ".k{stroke:var(--ink);stroke-width:1.6;stroke-linejoin:round;stroke-linecap:round}"
            ".kp{stroke:var(--parcel-line);stroke-width:1.2;stroke-linejoin:round}"
            ".thin{stroke-width:1}.handle{stroke-width:4.5;fill:none}"
            ".wire{fill:none;stroke:var(--ink);stroke-width:1.6;stroke-linejoin:round;stroke-linecap:round}"
            ".dim{fill:none;stroke:var(--muted);stroke-width:.9}"
            ".rule{stroke:var(--ink);stroke-width:1.6;fill:none}")


HATCH = ('<pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse">'
         f'<path d="M0 7L7 0" fill="none" stroke="{T["hatch"]}" stroke-width=".8"/></pattern>')

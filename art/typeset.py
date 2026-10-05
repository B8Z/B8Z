"""Outline text with HarfBuzz so the SVGs need no fonts at view time."""
from functools import lru_cache
import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import fonts

# face name -> (file, variable-font axis settings)
FACES = {
    "serif": ("Newsreader.ttf", {"opsz": 72, "wght": 400}),
    "serif-italic": ("Newsreader-Italic.ttf", {"opsz": 72, "wght": 400}),
    "text": ("Newsreader.ttf", {"opsz": 16, "wght": 420}),
    "text-italic": ("Newsreader-Italic.ttf", {"opsz": 16, "wght": 420}),
    "sans": ("Manrope.ttf", {"wght": 500}),
    "sans-bold": ("Manrope.ttf", {"wght": 700}),
    "mono": ("JetBrainsMono.ttf", {"wght": 500}),
}


@lru_cache(maxsize=None)
def _font(face):
    name, variations = FACES[face]
    blob = hb.Blob.from_file_path(str(fonts.path(name)))
    font = hb.Font(hb.Face(blob))
    font.set_variations(variations)
    return font, font.face.upem


def _fmt(v):
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def _fmt1(v):
    s = f"{v:.1f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


class _Pen(SVGPathPen):
    def __init__(self, fine=True):
        super().__init__(None, ntos=_fmt if fine else _fmt1)


def measure(text, face, size, tracking=0.0):
    font, upem = _font(face)
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True, "liga": True})
    return sum(p.x_advance for p in buf.glyph_positions) * size / upem + tracking * size * max(len(buf.glyph_infos) - 1, 0)


def outline(text, face, size, x=0.0, y=0.0, anchor="start", tracking=0.0, matrix=None):
    """Return SVG path data for `text` with its baseline origin at (x, y).

    `matrix` (a, b, c, d) maps the upright text plane onto a drawing plane, for
    labels that lie on an oblique face.
    """
    font, upem = _font(face)
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True, "liga": True})
    k = size / upem
    width = sum(p.x_advance for p in buf.glyph_positions) * k + tracking * size * max(len(buf.glyph_infos) - 1, 0)
    shift = {"start": 0.0, "middle": -width / 2, "end": -width}[anchor]
    a, b, c, d = matrix or (1, 0, 0, 1)
    pen = _Pen(fine=size >= 48)
    cursor = shift
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        gx, gy = cursor + pos.x_offset * k, -pos.y_offset * k
        # glyph units (y up) -> plane units (y down) -> drawing plane
        t = (a * k, b * k, -c * k, -d * k, x + a * gx + c * gy, y + b * gx + d * gy)
        font.draw_glyph_with_pen(info.codepoint, TransformPen(pen, t))
        cursor += pos.x_advance * k + tracking * size
    return pen.getCommands(), width

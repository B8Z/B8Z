"""Small SVG helpers: number formatting, an oblique projection, and shapes."""
import math
import re
from html import escape


def f(v):
    s = f"{v:.1f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def path(points, close=True):
    d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in points)
    return d + ("Z" if close else "")


class Oblique:
    """Cabinet-style projection: X runs along the front, Y into depth, Z up."""

    def __init__(self, ox, oy, scale=1.0, front_deg=11.3, depth_deg=29.4, depth_scale=0.5):
        a, b = math.radians(front_deg), math.radians(depth_deg)
        self.o = (ox, oy)
        self.s = scale
        self.ex = (math.cos(a) * scale, math.sin(a) * scale)
        self.ey = (math.cos(b) * scale * depth_scale, -math.sin(b) * scale * depth_scale)
        self.ez = (0.0, -scale)

    def p(self, x, y=0.0, z=0.0):
        return (self.o[0] + x * self.ex[0] + y * self.ey[0] + z * self.ez[0],
                self.o[1] + x * self.ex[1] + y * self.ey[1] + z * self.ez[1])

    def front(self, x0, z0, x1, z1, y=0.0):
        return [self.p(x0, y, z1), self.p(x1, y, z1), self.p(x1, y, z0), self.p(x0, y, z0)]

    def side(self, x, y0, z0, y1, z1):
        return [self.p(x, y0, z1), self.p(x, y1, z1), self.p(x, y1, z0), self.p(x, y0, z0)]

    def top(self, x0, y0, x1, y1, z):
        return [self.p(x0, y0, z), self.p(x1, y0, z), self.p(x1, y1, z), self.p(x0, y1, z)]

    def front_matrix(self):
        """Affine (a, b, c, d) that lays upright artwork onto the front plane."""
        return (self.ex[0] / self.s, self.ex[1] / self.s, 0.0, 1.0)


def poly(points, cls="", **attrs):
    extra = "".join(f' {k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    c = f' class="{cls}"' if cls else ""
    return f'<path d="{path(points)}"{c}{extra}/>'


def line(points, cls="", **attrs):
    extra = "".join(f' {k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    c = f' class="{cls}"' if cls else ""
    return f'<path d="{path(points, close=False)}"{c}{extra}/>'


def text(s, face, size, x, y, fill, anchor="start", tracking=0.0, cls="", matrix=None):
    from typeset import outline
    d, _ = outline(s, face, size, x, y, anchor, tracking, matrix)
    c = f' class="{cls}"' if cls else ""
    return f'<path data-copy="{escape(s, quote=True)}" d="{d}" fill="{fill}"{c}/>'


_TOKEN = re.compile(r' (fill|stroke)="(var\(--[a-z-]+\))"')


def _tokens_to_style(match):
    """Move themed paints from presentation attributes into a style attribute.

    Custom properties are guaranteed to resolve in CSS declarations; their
    handling in presentation attributes is less uniform between renderers.
    """
    tag = match.group(0)
    paints = _TOKEN.findall(tag)
    if not paints:
        return tag
    tag = _TOKEN.sub("", tag)
    style = ";".join(f"{name}:{value}" for name, value in paints)
    end = "/>" if tag.endswith("/>") else ">"
    return f'{tag[:-len(end)]} style="{style}"{end}'


def document(width, height, title, desc, css, body, defs=""):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-labelledby="t d">'
           f'<title id="t">{title}</title><desc id="d">{desc}</desc><defs>{defs}</defs><style>{css}</style>'
           f'<rect width="{width}" height="{height}" fill="var(--ground)"/>{body}</svg>')
    return re.sub(r"<[a-zA-Z][^<>]*>", _tokens_to_style, svg)

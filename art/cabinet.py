"""A parcel-locker cabinet in line art on an oblique projection."""
import math
from svgkit import poly, line, path, f
from typeset import outline
from theme import T

GAP = 5.0        # reveal between a door and its cell
PLINTH = 16.0
CAP = 10.0


def door_art(w, h, inner=False):
    """A door in its own plane: origin at the hinge top, u to the right, v down."""
    fill, inset = (T["accent_fill"], T["accent_inset"]) if inner else (T["door"], T["inset"])
    m = 13 if w > 100 else 10
    hx = m + 9 if inner else w - m - 9
    return (f'<rect width="{f(w)}" height="{f(h)}" fill="{fill}" class="k"/>'
            f'<rect x="{m}" y="{m}" width="{f(w - 2 * m)}" height="{f(h - 2 * m)}" fill="{inset}" class="k thin"/>'
            f'<path d="M{f(hx)} {f(h / 2 - 15)}V{f(h / 2 + 15)}" class="k handle"/>')


class Cabinet:
    """columns: [(x0, x1, [z boundaries])]; console: (x0, x1) or None;
    opens: (column index, row index) of the compartment whose door swings."""

    def __init__(self, iso, width, height, depth, columns, console=None, opens=None, uid="c", first_number=1):
        self.iso, self.W, self.H, self.D = iso, width, height, depth
        self.columns, self.console, self.opens, self.uid = columns, console, opens, uid
        self.first_number = first_number

    # -- geometry ------------------------------------------------------------
    def cell(self):
        ci, ri = self.opens
        x0, x1, zs = self.columns[ci]
        return x0, x1, zs[ri], zs[ri + 1]

    def door_matrix(self, theta_deg, x0=None, z1=None):
        iso = self.iso
        if x0 is None:
            x0, _, _, zb = self.cell()
            z1 = PLINTH + zb
        th = math.radians(theta_deg)
        a = math.cos(th) * iso.ex[0] - math.sin(th) * iso.ey[0]
        b = math.cos(th) * iso.ex[1] - math.sin(th) * iso.ey[1]
        ox, oy = iso.p(x0 + GAP, 0, z1 - GAP)
        return a, b, 0.0, iso.s, ox, oy

    def edge_on_angle(self):
        """Hinge angle at which the door is seen edge-on; past it the inner face shows."""
        return math.degrees(math.atan2(self.iso.ex[0], self.iso.ey[0]))

    @staticmethod
    def matrix_attr(m):
        a, b, c, d, e, ff = m
        return f"matrix({a:.4f} {b:.4f} {c:.4f} {d:.4f} {f(e)} {f(ff)})"

    @staticmethod
    def matrix_css(m):
        a, b, c, d, e, ff = m
        return f"matrix({a:.4f},{b:.4f},{c:.4f},{d:.4f},{f(e)},{f(ff)})"

    # -- drawing -------------------------------------------------------------
    def clip(self):
        if not self.opens:
            return ""
        x0, x1, za, zb = self.cell()
        quad = self.iso.front(x0 + GAP, PLINTH + za + GAP, x1 - GAP, PLINTH + zb - GAP)
        return f'<clipPath id="open-{self.uid}"><path d="{path(quad)}"/></clipPath>'

    def shadow(self):
        P, W, D = self.iso.p, self.W, self.D
        return poly([P(-14, -26, 0), P(W + 30, -26, 0), P(W + 30, D + 20, 0), P(-14, D + 20, 0)], fill=T["shadow"])

    def body(self):
        iso, W, H, D = self.iso, self.W, self.H, self.D
        P, g = iso.p, []
        z0, z1 = PLINTH, PLINTH + H
        g.append(poly(iso.side(W - 8, 6, 0, D - 6, PLINTH), cls="k", fill=T["door"]))
        g.append(poly(iso.front(8, 0, W - 8, PLINTH, y=6), cls="k", fill=T["door"]))
        g.append(poly(iso.side(W, 0, z0, D, z1), cls="k", fill=T["ground"]))
        g.append(poly(iso.side(W, 0, z0, D, z1), cls="k", fill="url(#hatch)"))
        for i in range(5):
            zz = z1 - min(60, H * .22) - i * 11
            g.append(line([P(W, D * .28, zz), P(W, D * .72, zz)], cls="k"))
        g.append(poly(iso.top(-CAP / 2, -CAP / 2, W + CAP / 2, D, z1 + CAP), cls="k", fill=T["ground"]))
        g.append(poly(iso.side(W + CAP / 2, -CAP / 2, z1, D, z1 + CAP), cls="k", fill=T["door"]))
        g.append(poly(iso.front(-CAP / 2, z1, W + CAP / 2, z1 + CAP, y=-CAP / 2), cls="k", fill=T["inset"]))
        g.append(poly(iso.front(0, z0, W, z1), cls="k", fill=T["wash"]))
        if self.opens:
            g.append(self._interior())
        n = self.first_number - 1
        for ci, (x0, x1, zs) in enumerate(self.columns):
            for ri, (za, zb) in enumerate(zip(zs, zs[1:])):
                n += 1
                if self.opens == (ci, ri):
                    self.open_number = n
                    continue
                w, h = x1 - x0 - 2 * GAP, zb - za - 2 * GAP
                m = self.door_matrix(0, x0, z0 + zb)
                g.append(f'<g transform="{self.matrix_attr(m)}">{door_art(w, h)}'
                         f'<path d="{outline(f"{n:02d}", "mono", 11, 14, 24)[0]}" fill="{T["muted"]}"/></g>')
        if self.console:
            g.append(self._console())
        return "".join(g)

    def _interior(self):
        iso, P, g = self.iso, self.iso.p, []
        x0, x1, za, zb = self.cell()
        ox0, ox1, oz0, oz1 = x0 + GAP, x1 - GAP, PLINTH + za + GAP, PLINTH + zb - GAP
        depth = self.D * .82
        g.append(poly(iso.front(ox0, oz0, ox1, oz1), cls="k", fill=T["inner_back"]))
        g.append(f'<g clip-path="url(#open-{self.uid})">')
        g.append(poly([P(ox0, 0, oz1), P(ox0, depth, oz1), P(ox0, depth, oz0), P(ox0, 0, oz0)], fill=T["inner_wall"], cls="k thin"))
        g.append(poly([P(ox0, 0, oz0), P(ox1, 0, oz0), P(ox1, depth, oz0), P(ox0, depth, oz0)], fill=T["inner_floor"], cls="k thin"))
        w = ox1 - ox0
        bx0, bx1, by0, by1, bh = ox0 + w * .24, ox0 + w * .78, 10, 62, 44
        g.append(poly([P(bx0, by0, oz0), P(bx1, by0, oz0), P(bx1, by0, oz0 + bh), P(bx0, by0, oz0 + bh)], fill=T["parcel_front"], cls="kp"))
        g.append(poly([P(bx1, by0, oz0), P(bx1, by1, oz0), P(bx1, by1, oz0 + bh), P(bx1, by0, oz0 + bh)], fill=T["parcel_side"], cls="kp"))
        g.append(poly([P(bx0, by0, oz0 + bh), P(bx1, by0, oz0 + bh), P(bx1, by1, oz0 + bh), P(bx0, by1, oz0 + bh)], fill=T["parcel"], cls="kp"))
        mx = (bx0 + bx1) / 2
        g.append(poly([P(mx - 6, by0, oz0 + bh), P(mx + 6, by0, oz0 + bh), P(mx + 6, by1, oz0 + bh), P(mx - 6, by1, oz0 + bh)], fill=T["parcel_front"], cls="kp thin"))
        g.append(poly([P(mx - 6, by0, oz0 + bh), P(mx + 6, by0, oz0 + bh), P(mx + 6, by0, oz0 + bh - 14), P(mx - 6, by0, oz0 + bh - 14)], fill=T["parcel"], cls="kp thin"))
        g.append("</g>")
        g.append(poly(iso.front(ox0, oz0, ox1, oz1), cls="k", fill="none"))
        return "".join(g)

    def _console(self):
        cx0, cx1 = self.console
        m = self.door_matrix(0, cx0, PLINTH + self.H)
        cw, ch = cx1 - cx0 - 2 * GAP, self.H - 2 * GAP
        c = [f'<rect width="{f(cw)}" height="{f(ch)}" fill="{T["door"]}" class="k"/>',
             f'<rect x="9" y="12" width="{f(cw - 18)}" height="62" rx="2" fill="{T["screen"]}" class="k"/>',
             f'<path d="M16 26h{f(cw - 46)}M16 37h{f(cw - 56)}" stroke="{T["screen_ink"]}" stroke-width="2.4" opacity=".55"/>',
             f'<rect class="led" x="16" y="52" width="16" height="9" fill="{T["accent_fill"]}"/>',
             f'<rect x="9" y="88" width="{f(cw - 18)}" height="12" fill="{T["inner_back"]}" class="k thin"/>']
        for r in range(4):
            for col in range(3):
                c.append(f'<rect x="{f(14 + col * 17)}" y="{f(114 + r * 15)}" width="11" height="9" fill="{T["inset"]}" class="k thin"/>')
        c.append(f'<rect x="9" y="188" width="{f(cw - 18)}" height="22" fill="{T["inset"]}" class="k thin"/>')
        c.append(f'<path d="M9 {f(ch - 86)}h{f(cw - 18)}" class="k thin"/>')
        return f'<g transform="{self.matrix_attr(m)}">{"".join(c)}</g>'

    def door(self, theta=None, cls="door"):
        """The swinging door. With `theta`, it is posed; without, the caller animates it."""
        x0, x1, za, zb = self.cell()
        w, h = x1 - x0 - 2 * GAP, zb - za - 2 * GAP
        number = f'<path d="{outline(f"{self.open_number:02d}", "mono", 11, 14, 24)[0]}" fill="{T["muted"]}"/>'
        pose, outer, inner = "", "", ""
        if theta is not None:
            pose = f' transform="{self.matrix_attr(self.door_matrix(theta))}"'
            showing_inner = theta >= self.edge_on_angle()
            outer = ' opacity="0"' if showing_inner else ""
            inner = "" if showing_inner else ' opacity="0"'
        return (f'<g class="{cls}"{pose}><g class="{cls}-outer"{outer}>{door_art(w, h)}{number}</g>'
                f'<g class="{cls}-inner"{inner}>{door_art(w, h, inner=True)}</g></g>')

"""Project plates. Each shows one recorded comparison from the project it links to.

Recovery: the two controller-crash captures in device-recovery-lab/demo/traces.json
end with the same journal state (IN_DOUBT) and different pulse counts (0 and 1).
Placement: in the tighter-deadline fixture of placement-tradeoffs
(measurements/2026-10-03.json) greedy places C for objective 23; D and E reach 27.
"""
from svgkit import Oblique, poly, line, f, text, document
from typeset import measure
from cabinet import Cabinet
from theme import T, HATCH, css as theme_css

SINGLE = dict(width=150.0, height=190.0, depth=120.0, columns=[(0, 150, [0, 190])])


def arrow(x, y, color):
    return f'<path d="M{f(x)} {f(y)}h22m-8-7l8 7l-8 7" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'


def words(x, y, kicker, title, body, cta, url, size, lead, body_size=21, gap=30, cta_y=None, small=16, linked=True):
    """Text block. `title` is a list of lines; each line is [(text, face)].
    `cta_y` pins the link line to a baseline; otherwise it follows the body."""
    o = [text(kicker, "mono", small, x + 2, y, T["accent"], tracking=.1)]
    ty = y + size * .98 + 14
    for parts in title:
        cx = x
        for part, face in parts:
            o.append(text(part, face, size, cx, ty, T["ink"]))
            cx += measure(part, face, size)
        ty += lead
    by = ty - lead + body_size + 30
    for row in body:
        o.append(text(row, "sans", body_size, x + 2, by, T["muted"]))
        by += gap
    cy = cta_y if cta_y is not None else by + 26
    o.append(text(cta, "sans-bold", small + 4, x + 2, cy, T["ink"]))
    if linked:
        o.append(arrow(x + 2 + measure(cta, "sans-bold", small + 4) + 12, cy - 7, T["accent"]))
    o.append(text(url, "mono", small - 1, x + 2, cy + 29, T["muted"]))
    return "".join(o), cy + 29


def slip(x, y, small, w=214):
    return (f'<rect x="{f(x)}" y="{f(y)}" width="{w}" height="66" fill="{T["wash"]}" class="k thin"/>'
            + text("CONTROLLER JOURNAL", "mono", small - 1, x + 14, y + 25, T["muted"], tracking=.06)
            + text("IN_DOUBT", "mono", 21, x + 14, y + 51, T["accent"], tracking=.04))


def crash_pair(ax, bx, ground_y, scale, caption_y, small=14.5):
    """Two single lockers: closed with 0 pulses, open with 1 pulse; identical journal slips."""
    o, defs = [], []
    for key, x, tag, opens, count, unit in (("a", ax, "CRASH BEFORE THE PULSE", None, "0", "physical pulses"),
                                            ("b", bx, "CRASH AFTER THE PULSE", (0, 0), "1", "physical pulse")):
        iso = Oblique(x, ground_y, scale=scale)
        cab = Cabinet(iso, uid=key, opens=(0, 0), **SINGLE)      # both have the same compartment
        o.append(cab.shadow())
        o.append(cab.body())
        o.append(cab.door(104 if opens else 0))
        defs.append(cab.clip())
        left = x - 6
        o.append(text(tag, "mono", small, left, caption_y, T["muted"], tracking=.06))
        o.append(text(count, "serif", 78, left - 3, caption_y + 76, T["ink"]))
        o.append(text(unit, "sans", 20, left + measure(count, "serif", 78) + 12, caption_y + 74, T["muted"]))
        o.append(slip(left, caption_y + 98, small))
    return "".join(o), "".join(defs)


RECOVERY_TITLE = "Device Recovery Lab"
RECOVERY_DESC = ("Did it happen? I built a recovery service for a simulated locker. I use controlled failures to test what "
                 "it can establish before it resends a command. The drawing shows two captured controller crashes: before "
                 "the pulse the locker stays closed with 0 physical pulses, after the pulse it is open with 1, and both "
                 "controller journals read IN_DOUBT.")
RECOVERY_WORDS = dict(kicker="DEVICE RECOVERY LAB", title=[[("Did it ", "serif"), ("happen?", "serif-italic")]],
                      cta="Open the recorded viewer", url="b8z.github.io/device-recovery-lab")


def recovery_wide():
    W, H = 1280, 610
    block, _ = words(60, 92, body=["I built a recovery service for a simulated locker.",
                                   "I use controlled failures to test what it can",
                                   "establish before it resends a command."], size=86, lead=90, body_size=22, gap=32, cta_y=H - 92, **RECOVERY_WORDS)
    o = [block, text("Same record. Different reality.", "serif-italic", 33, 690, 106, T["ink"])]
    pair, defs = crash_pair(712, 1000, 356, 0.84, 406)
    o.append(pair)
    return document(W, H, RECOVERY_TITLE, RECOVERY_DESC, theme_css(), "".join(o), HATCH + defs)


def recovery_narrow():
    W, H = 640, 620
    o = [text("Did it happen?", "serif", 68, 34, 89, T["ink"])]
    defs = []
    for key, x, angle, caption, count in (
        ("a", 62, 0, "Before the pulse", "0 pulses"),
        ("b", 352, 104, "After the pulse", "1 pulse"),
    ):
        iso = Oblique(x, 356, scale=.96)
        cab = Cabinet(iso, uid=key, opens=(0, 0), **SINGLE)
        o.extend([cab.shadow(), cab.body(), cab.door(angle),
                  text(caption, "sans", 28, x - 8, 435, T["muted"]),
                  text(count, "serif", 58, x - 10, 499, T["ink"])])
        defs.append(cab.clip())
    o.extend(['<path d="M38 535H602" class="rule"/>',
              text("BOTH JOURNALS", "mono", 24, 38, 582, T["muted"]),
              text("IN_DOUBT", "mono", 34, 374, 585, T["accent"])])
    return document(W, H, RECOVERY_TITLE, RECOVERY_DESC, theme_css(), "".join(o), HATCH + "".join(defs))


# --- placement ---------------------------------------------------------------
CELL, TRAY_DEPTH, SLAB, BLOCK = 46.0, 70.0, 10.0, 50.0


def tray(iso, blocks, capacity=6, accent=False):
    """A row of capacity units with placed requests: blocks = [(label, first unit, units)]."""
    P, o = iso.p, []
    width = capacity * CELL
    o.append(poly([P(-10, -18, 0), P(width + 22, -18, 0), P(width + 22, TRAY_DEPTH + 14, 0), P(-10, TRAY_DEPTH + 14, 0)], fill=T["shadow"]))
    o.append(poly(iso.side(width, 0, 0, TRAY_DEPTH, SLAB), cls="k", fill=T["door"]))
    o.append(poly(iso.top(0, 0, width, TRAY_DEPTH, SLAB), cls="k", fill=T["wash"]))
    o.append(poly(iso.front(0, 0, width, SLAB), cls="k", fill=T["inset"]))
    for i in range(1, capacity):
        o.append(line([P(i * CELL, 0, SLAB), P(i * CELL, TRAY_DEPTH, SLAB)], cls="k thin"))
        o.append(line([P(i * CELL, 0, 0), P(i * CELL, 0, SLAB)], cls="k thin"))
    used = set()
    m = iso.front_matrix()
    for label, first, units in sorted(blocks, key=lambda b: b[1]):
        used.update(range(first, first + units))
        x0, x1, y0, y1, z0, z1 = first * CELL + 4, (first + units) * CELL - 4, 8, TRAY_DEPTH - 8, SLAB, SLAB + BLOCK
        front, top = (T["accent_fill"], T["accent_inset"]) if accent else (T["door"], T["inset"])
        o.append(poly(iso.side(x1, y0, z0, y1, z1), cls="k", fill=T["ground"]))
        o.append(poly(iso.side(x1, y0, z0, y1, z1), cls="k", fill="url(#hatch)"))
        o.append(poly(iso.top(x0, y0, x1, y1, z1), cls="k", fill=top))
        o.append(poly(iso.front(x0, z0, x1, z1, y=y0), cls="k", fill=front))
        cx, cy = P((x0 + x1) / 2, y0, z0 + BLOCK * .28)
        o.append(text(label, "sans-bold", 26 * iso.s, cx, cy, T["ground"] if accent else T["ink"], anchor="middle", matrix=m))
    for i in range(capacity):
        if i not in used:
            quad = [P(i * CELL + 7, 9, SLAB), P((i + 1) * CELL - 7, 9, SLAB), P((i + 1) * CELL - 7, TRAY_DEPTH - 9, SLAB), P(i * CELL + 7, TRAY_DEPTH - 9, SLAB)]
            o.append(poly(quad, fill="none", stroke=T["muted"], stroke_width="1.1", stroke_dasharray="4 4"))
    return "".join(o)


def placement_rows(x, y, scale, step, numeral_x, small=14.5):
    o = []
    rows = [("GREEDY", "places C: 5 of 6 units", [("C", 0, 5)], "23", False),
            ("GENETIC SEARCH AND EXHAUSTIVE REFERENCE", "place D and E: 6 of 6 units", [("D", 0, 2), ("E", 2, 4)], "27", True)]
    for i, (label, note, blocks, objective, best) in enumerate(rows):
        top = y + i * step
        o.append(text(label, "mono", small, x, top, T["muted"], tracking=.06))
        iso = Oblique(x + 6, top + 92 * scale + 10, scale=scale)
        o.append(tray(iso, blocks, accent=best))
        o.append(text(objective, "serif", 78, numeral_x, top + 84, T["accent"] if best else T["ink"]))
        o.append(text("objective", "sans", 20, numeral_x + measure(objective, "serif", 78) + 12, top + 82, T["muted"]))
        o.append(text(note, "sans", 18.5, numeral_x + 2, top + 114, T["muted"]))
    return "".join(o)


PLACEMENT_TITLE = "Placement Tradeoffs"
PLACEMENT_DESC = ("Every placement changes what fits. I compare a fast greedy choice, a bounded genetic search, and an "
                  "exhaustive reference. The drawing shows the tighter-deadline fixture, where only Edge with 6 capacity "
                  "units is eligible: greedy places request C in 5 units for objective 23, while genetic search and the "
                  "exhaustive reference place D and E in 6 units for objective 27.")
PLACEMENT_WORDS = dict(kicker="PLACEMENT TRADEOFFS", cta="Explore the recorded experiments", url="b8z.github.io/placement-tradeoffs")


def placement_wide():
    W, H = 1280, 610
    block, _ = words(60, 92, title=[[("Every placement", "serif")], [("changes ", "serif"), ("what fits.", "serif-italic")]],
                     body=["I compare a fast greedy choice, a bounded",
                           "genetic search, and an exhaustive reference.",
                           "Change the constraints and inspect what each",
                           "method gives up."], size=66, lead=72, body_size=22, gap=32, cta_y=H - 92, **PLACEMENT_WORDS)
    o = [block,
         text("A placement can be feasible and still", "serif-italic", 33, 690, 106, T["ink"]),
         text("block a better combination.", "serif-italic", 33, 690, 146, T["ink"]),
         text("TIGHTER DEADLINES: ONLY EDGE IS ELIGIBLE, 6 CAPACITY UNITS", "mono", 14.5, 692, 188, T["accent"], tracking=.06),
         placement_rows(692, 240, 1.0, 176, 1012)]
    return document(W, H, PLACEMENT_TITLE, PLACEMENT_DESC, theme_css(), "".join(o), HATCH)


def placement_narrow():
    W, H = 640, 600
    o = [text("What fits?", "serif", 68, 34, 89, T["ink"]),
         text("Tighter deadlines: only Edge is eligible.", "sans", 26, 38, 135, T["muted"]),
         text("Capacity: 6 units. Higher objective is better.", "sans", 26, 38, 173, T["muted"])]
    for i, (label, blocks, value, note, accent) in enumerate((
        ("Greedy", [("C", 0, 5)], "23", "5 units", False),
        ("Genetic / exhaustive", [("D", 0, 2), ("E", 2, 4)], "27", "6 units", True),
    )):
        y = 242 + 183 * i
        o.extend([text(label, "sans", 28, 38, y, T["ink"]),
                  tray(Oblique(46, y + 100, scale=1.0), blocks, accent=accent),
                  text(value, "serif", 80, 446, y + 78, T["accent"] if accent else T["ink"]),
                  text(note, "sans", 27, 447, y + 118, T["muted"])])
    return document(W, H, PLACEMENT_TITLE, PLACEMENT_DESC, theme_css(), "".join(o), HATCH)


# --- thesis ------------------------------------------------------------------
THESIS_TITLE = "A Genetic Algorithm for the Optimization of Service Provisioning in Multi-Layer Fog Networks"
THESIS_DESC = ("My master\u2019s thesis, Christopher Newport University, 2022. I developed a genetic algorithm and a VNF "
               "placement heuristic in Python with NumPy and NetworkX, and compared the approach with a Gurobi MILP model. "
               "The drawing is a schematic of network functions placed on nodes across three layers; it is not a result "
               "from the thesis.")
THESIS_WORDS = dict(kicker="MASTER\u2019S THESIS, 2022",
                    title=[[("A Genetic Algorithm for the", "serif")], [("Optimization of Service", "serif")],
                           [("Provisioning in Multi-Layer", "serif")], [("Fog Networks", "serif-italic")]],
                    cta="Python · NumPy · NetworkX · Gurobi",
                    url="Research: 2022 · Illustration: October 2026", linked=False)
LAYERS = [  # (z, [(x, y, width, depth, height)]) from the lowest layer up
    (0, [(18, 16, 44, 44, 26), (98, 70, 44, 44, 26), (178, 16, 44, 44, 26), (258, 70, 44, 44, 26), (338, 16, 44, 44, 26)]),
    (128, [(40, 34, 62, 54, 34), (170, 34, 62, 54, 34), (300, 34, 62, 54, 34)]),
    (256, [(84, 30, 84, 62, 44), (236, 30, 84, 62, 44)]),
]
CHAIN = [(0, 1), (1, 1), (2, 1)]            # (layer, node) carrying the highlighted functions
OTHERS = [(0, 3), (1, 0), (2, 0), (0, 0)]   # nodes carrying other placed functions
PLANE_W, PLANE_D = 400.0, 132.0


def box(iso, x, y, z, w, d, h, front, top, hatch=True):
    o = [poly(iso.side(x + w, y, z, y + d, z + h), cls="k", fill=T["ground"])]
    if hatch:
        o.append(poly(iso.side(x + w, y, z, y + d, z + h), cls="k", fill="url(#hatch)"))
    o.append(poly(iso.top(x, y, x + w, y + d, z + h), cls="k", fill=top))
    o.append(poly(iso.front(x, z, x + w, z + h, y=y), cls="k", fill=front))
    return "".join(o)


def layers(iso):
    """Three stacked layers of nodes with network functions placed on some of them."""
    P, o, tops = iso.p, [], {}
    for li, (z, nodes) in enumerate(LAYERS):
        if li:                                   # links rise from the layer below and pass behind this plane
            below_z, below = LAYERS[li - 1]
            for bx, by, bw, bd, bh in below:     # each node links to its nearest node in the layer above
                nx, ny, nw, nd, nh = min(nodes, key=lambda n: abs((bx + bw / 2) - (n[0] + n[2] / 2)))
                o.append(line([P(bx + bw / 2, by + bd / 2, below_z + 6 + bh), P(nx + nw / 2, ny + nd / 2, z)], cls="dim"))
        o.append(poly([P(-8, -12, z - 2), P(PLANE_W + 18, -12, z - 2), P(PLANE_W + 18, PLANE_D + 10, z - 2), P(-8, PLANE_D + 10, z - 2)], fill=T["shadow"]) if li == 0 else "")
        o.append(poly(iso.side(PLANE_W, 0, z, PLANE_D, z + 6), cls="k", fill=T["door"]))
        o.append(poly(iso.top(0, 0, PLANE_W, PLANE_D, z + 6), cls="k", fill=T["wash"]))
        o.append(poly(iso.front(0, z, PLANE_W, z + 6), cls="k", fill=T["inset"]))
        for ni, (x, y, w, d, h) in sorted(enumerate(nodes), key=lambda n: -n[1][1]):
            o.append(box(iso, x, y, z + 6, w, d, h, T["door"], T["inset"]))
            top = z + 6 + h
            if (li, ni) in CHAIN or (li, ni) in OTHERS:
                chain = (li, ni) in CHAIN
                s = min(w, d) * .5
                fx, fy = x + (w - s) / 2, y + (d - s) / 2
                o.append(box(iso, fx, fy, top, s, s, s * .7, T["accent_fill"] if chain else T["wash"],
                             T["accent_inset"] if chain else T["ground"], hatch=False))
                if chain:
                    tops[li] = P(fx + s / 2, fy, top + s * .35)
    path_points = [tops[li] for li, _ in CHAIN]
    o.append(line(path_points, fill="none", stroke=T["accent"], stroke_width="3", stroke_dasharray="0.1 8", stroke_linecap="round"))
    return "".join(o)


def thesis_wide():
    W, H = 1280, 610
    block, _ = words(60, 92, body=["Christopher Newport University. A genetic algorithm",
                                   "and VNF placement heuristic in Python, compared",
                                   "with a Gurobi MILP model."], size=47, lead=53, body_size=22, gap=32, cta_y=H - 92, **THESIS_WORDS)
    o = [block,
         text("Each placement consumes capacity", "serif-italic", 33, 690, 106, T["ink"]),
         text("and contributes to delay.", "serif-italic", 33, 690, 146, T["ink"]),
         layers(Oblique(748, 462, scale=0.92)),
         text("SCHEMATIC OF FUNCTIONS PLACED ACROSS LAYERS, NOT A THESIS RESULT", "mono", 13.5, 692, H - 46, T["muted"], tracking=.06)]
    return document(W, H, THESIS_TITLE, THESIS_DESC, theme_css(), "".join(o), HATCH)


def thesis_narrow():
    W, H = 640, 1104
    block, end = words(40, 78, body=["Christopher Newport University. A genetic",
                                     "algorithm and VNF placement heuristic in",
                                     "Python, compared with a Gurobi MILP model."], size=45, lead=51, body_size=24, gap=34, small=18, **THESIS_WORDS)
    o = [block, f'<path d="M40 {end + 34}H{W - 40}" class="rule"/>',
         text("Each placement consumes capacity", "serif-italic", 29, 40, end + 84, T["ink"]),
         text("and contributes to delay.", "serif-italic", 29, 40, end + 120, T["ink"]),
         layers(Oblique(96, end + 470, scale=0.92)),
         text("SCHEMATIC OF FUNCTIONS PLACED ACROSS", "mono", 16, 42, end + 566, T["muted"], tracking=.05),
         text("LAYERS, NOT A THESIS RESULT", "mono", 16, 42, end + 589, T["muted"], tracking=.05)]
    return document(W, H, THESIS_TITLE, THESIS_DESC, theme_css(), "".join(o), HATCH)

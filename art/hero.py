"""A static editorial masthead; project evidence lives in the project plates."""
from svgkit import text, document
from typeset import measure
from theme import T, css as theme_css

TITLE = "Adam Bates — Senior Software Engineer"
DESC = ("I build and improve complex systems, and help teams understand them. "
        "Financial systems, device integration, and applied optimization.")


def name(x, y, size):
    return (text("Adam ", "serif", size, x, y, T["ink"])
            + text("Bates", "serif-italic", size,
                   x + measure("Adam ", "serif", size), y, T["ink"]))


def wide():
    width, height = 1280, 390
    body = [text("SENIOR SOFTWARE ENGINEER", "mono", 20, 60, 62,
                 T["accent"], tracking=.08),
            name(54, 220, 128),
            '<path d="M750 114V230" class="dim"/>']
    for i, row in enumerate(("I build and improve", "complex systems, and help", "teams understand them.")):
        body.append(text(row, "sans", 27, 792, 144 + 41 * i, T["ink"]))
    body.append('<path d="M60 289H1220" class="rule"/>')
    for x, number, label in ((60, "01", "Financial systems"),
                             (464, "02", "Device integration"),
                             (864, "03", "Applied optimization")):
        body.append(text(number, "mono", 18, x, 343, T["accent"]))
        body.append(text(label, "sans", 23, x + 44, 343, T["ink"]))
    return document(width, height, TITLE, DESC, theme_css(), "".join(body))


def narrow():
    width, height = 640, 490
    body = [text("SENIOR SOFTWARE ENGINEER", "mono", 22, 36, 55,
                 T["accent"], tracking=.06),
            name(30, 171, 110)]
    for i, row in enumerate(("I build and improve complex systems,",
                             "and help teams understand them.")):
        body.append(text(row, "sans", 27, 36, 235 + 39 * i, T["ink"]))
    body.append('<path d="M36 314H604" class="rule"/>')
    for i, label in enumerate(("Financial systems", "Device integration", "Applied optimization")):
        body.append(text(f"0{i + 1}", "mono", 20, 36, 358 + 43 * i, T["accent"]))
        body.append(text(label, "sans", 25, 83, 358 + 43 * i, T["ink"]))
    return document(width, height, TITLE, DESC, theme_css(), "".join(body))

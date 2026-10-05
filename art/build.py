"""Build the profile artwork into assets/.

    pip install -r art/requirements.txt
    python art/build.py            write the drawings
    python art/build.py --check    confirm assets/ matches this source

Each drawing is written twice: a wide layout and a narrow one that the README
selects below 600 px. Both carry a light and a dark palette.
"""
import re
import sys
from pathlib import Path
import hero
import plates

ASSETS = Path(__file__).resolve().parents[1] / "assets"
FILES = {
    "hero.svg": hero.wide, "hero-narrow.svg": hero.narrow,
    "plate-recovery.svg": plates.recovery_wide, "plate-recovery-narrow.svg": plates.recovery_narrow,
    "plate-placement.svg": plates.placement_wide, "plate-placement-narrow.svg": plates.placement_narrow,
    "plate-thesis.svg": plates.thesis_wide, "plate-thesis-narrow.svg": plates.thesis_narrow,
}

def comparable(data):
    """A committed drawing as the generator would have written it.

    Git may have checked the file out with CRLF line endings, and a file that
    was delivered by a tool may carry an embedded Content Credentials manifest
    in a <metadata> element. Neither changes the drawing.
    """
    data = data.replace(b"\r\n", b"\n")
    data = re.sub(rb"<metadata>.*?</metadata>", b"", data, flags=re.S)
    return re.sub(rb' xmlns:c2pa="[^"]*"', b"", data)


if __name__ == "__main__":
    check = "--check" in sys.argv
    stale = []
    ASSETS.mkdir(exist_ok=True)
    for name, make in FILES.items():
        svg = make().encode("utf-8")
        target = ASSETS / name
        if check:
            if not target.exists() or comparable(target.read_bytes()) != svg:
                stale.append(name)
        else:
            target.write_bytes(svg)
            print(f"{name:28s} {len(svg) / 1024:6.1f} KB")
    if check:
        if stale:
            raise SystemExit("Out of date, run python art/build.py: " + ", ".join(stale))
        print(f"{len(FILES)} drawings match their source")

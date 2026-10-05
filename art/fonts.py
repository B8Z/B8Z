"""Fetch the typefaces used to outline text.

The SVGs contain outlines, so no font is needed to view them. Building them
needs these four SIL Open Font License files, pinned to one commit of
google/fonts and checked against a SHA-256. They are cached in art/.fonts,
which is not committed.
"""
import hashlib
from pathlib import Path
from urllib.parse import quote
from urllib.request import urlopen

PIN = "9710da1eacb3be272583c3224dcb70f9da6eadbb"          # google/fonts, 2026-09-30
SOURCE = "https://raw.githubusercontent.com/google/fonts/" + PIN + "/"
CACHE = Path(__file__).resolve().parent / ".fonts"
FILES = {
    "Newsreader.ttf": ("ofl/newsreader/Newsreader[opsz,wght].ttf",
                       "8a08d13f8a6c0d51be379a60af84f945f65369a67e509ee3c3bdcc421254d7c1"),
    "Newsreader-Italic.ttf": ("ofl/newsreader/Newsreader-Italic[opsz,wght].ttf",
                              "796668611f80b64d5adf182fde3b6f29ed83b4e7cbec7b96937e84ac01364792"),
    "Manrope.ttf": ("ofl/manrope/Manrope[wght].ttf",
                    "3ae11c49db0455a3cc33e37d380f20fdb8c7f8b41dc07625c177e3d87a9d6ae6"),
    "JetBrainsMono.ttf": ("ofl/jetbrainsmono/JetBrainsMono[wght].ttf",
                          "48715a42ec242c21e9f02692891e147d022299a52e48d5e413e1a942193ffeda"),
}


def path(name):
    """Local path of a font file, downloading and verifying it on first use."""
    target = CACHE / name
    source, expected = FILES[name]
    if not target.exists():
        CACHE.mkdir(exist_ok=True)
        with urlopen(SOURCE + quote(source), timeout=60) as response:
            target.write_bytes(response.read())
    actual = hashlib.sha256(target.read_bytes()).hexdigest()
    if actual != expected:
        target.unlink()
        raise SystemExit(f"{name}: unexpected content (sha256 {actual}); removed the cached copy")
    return target

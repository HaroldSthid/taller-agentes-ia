"""Regenerates assets/qr-presentacion.svg, the QR shown on the last slide.

The QR points to the GitHub Pages address of this repository. If you rename the repository
or change the GitHub user, pass the new address and commit the new SVG.

    pip install segno
    python tools/make_qr.py                      # uses the default address below
    python tools/make_qr.py https://example.org/ # or any other address

Dark modules on a white background with a quiet zone, so it scans on a projector and on a phone
in both the light and the dark theme of the slides.
"""

import sys
from pathlib import Path

import segno

DEFAULT_URL = "https://haroldsthid.github.io/taller-agentes-ia/"
OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "qr-presentacion.svg"


def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    qr = segno.make(url, error="q", micro=False)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    qr.save(str(OUTPUT), scale=10, border=2, dark="#12262B", light="#FFFFFF", xmldecl=False, svgns=True, title="Código QR de la presentación")
    print(f"QR for {url} written to {OUTPUT}")


if __name__ == "__main__":
    main()

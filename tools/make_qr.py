"""Regenerates the QR codes shown on the last slide (assets/qr-presentacion.svg and assets/qr-linkedin.svg).

The QR points to the GitHub Pages address of this repository. If you rename the repository
or change the GitHub user, pass the new address and commit the new SVG.

    pip install segno
    python tools/make_qr.py                      # uses the default address below
    python tools/make_qr.py https://example.org/ # or any other address
    python tools/make_qr.py <url> qr-linkedin.svg "Código QR del perfil de LinkedIn"   # another file in assets/

Dark modules on a white background with a quiet zone, so it scans on a projector and on a phone
in both the light and the dark theme of the slides.
"""

import sys
from pathlib import Path

import segno

DEFAULT_URL = "https://haroldsthid.github.io/taller-agentes-ia/"
ASSETS = Path(__file__).resolve().parents[1] / "assets"
DEFAULT_NAME = "qr-presentacion.svg"
DEFAULT_TITLE = "Código QR de la presentación"


def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    name = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_NAME
    title = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_TITLE
    output = ASSETS / Path(name).name
    qr = segno.make(url, error="q", micro=False)
    output.parent.mkdir(parents=True, exist_ok=True)
    qr.save(str(output), scale=10, border=2, dark="#12262B", light="#FFFFFF", xmldecl=False, svgns=True, title=title)
    print(f"QR for {url} written to {output}")


if __name__ == "__main__":
    main()

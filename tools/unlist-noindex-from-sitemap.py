#!/usr/bin/env python3
"""Drop noindex pages from sitemap.xml. Runs as a Quarto post-render step.

Quarto writes every rendered page into sitemap.xml whenever `site-url` is set,
with no per-page opt-out. For an unlisted page that is self-defeating: the meta
tag asks crawlers not to index it while the sitemap points them straight at it.
Robots honour noindex over a sitemap entry, so nothing was leaking, but
advertising the URL is the opposite of what an unlisted page is for.

Rather than name the page here, this keys off the page's own declaration: if the
rendered HTML carries `<meta name="robots" content="...noindex...">`, its entry
comes out of the sitemap. Marking a new page unlisted needs no change to this
script.
"""

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

# Defaults to the project's output dir; takes a path argument so it can be run
# against a fixture without touching a real build.
SITE = Path(sys.argv[1]) if len(sys.argv) > 1 else (
    Path(__file__).resolve().parent.parent / "_site"
)
SITEMAP = SITE / "sitemap.xml"
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
NOINDEX = re.compile(
    r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'][^"\']*noindex', re.I
)


def local_file(loc):
    """Map a sitemap <loc> URL back to the file Quarto wrote for it."""
    path = urlparse(loc).path.lstrip("/")
    candidate = SITE / (path or "index.html")
    if candidate.is_dir():
        candidate = candidate / "index.html"
    return candidate


def main():
    if not SITEMAP.exists():
        # No site-url configured, or a partial render. Nothing to do, and this
        # is not a failure worth breaking the build over.
        print("unlist-noindex: no sitemap.xml, skipping")
        return 0

    ET.register_namespace("", NS)
    tree = ET.parse(SITEMAP)
    root = tree.getroot()

    removed = []
    for url in list(root.findall(f"{{{NS}}}url")):
        loc_el = url.find(f"{{{NS}}}loc")
        if loc_el is None or not loc_el.text:
            continue
        page = local_file(loc_el.text)
        if not page.exists():
            continue
        if NOINDEX.search(page.read_text(encoding="utf-8", errors="ignore")):
            root.remove(url)
            removed.append(loc_el.text)

    if not removed:
        print("unlist-noindex: no noindex pages in sitemap")
        return 0

    tree.write(SITEMAP, encoding="UTF-8", xml_declaration=True)
    for loc in removed:
        print(f"unlist-noindex: removed {loc}")
    print(f"unlist-noindex: {len(removed)} removed, "
          f"{len(root.findall(f'{{{NS}}}url'))} remain")
    return 0


if __name__ == "__main__":
    sys.exit(main())

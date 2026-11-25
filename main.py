#!/usr/bin/env python3
"""Front-page entry for the 24 November 2026 news-image bounty.

The finished page lives in this repository as entry.png. This program
only carries that file into the output folder the grader reads.
"""

import os
import shutil
import sys
from pathlib import Path

PAGE_FILE = "entry.png"


def main() -> int:
    repo_root = Path(__file__).resolve().parent
    page = repo_root / PAGE_FILE
    if not page.is_file():
        print(f"missing {page}", file=sys.stderr)
        return 1
    if page.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
        print(f"{page} is not a PNG file", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    destination = out_dir / PAGE_FILE
    shutil.copyfile(page, destination)
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

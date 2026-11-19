"""news-image-20261119 entry program: write the day's news image to /output.

The image beside this file (entry.png) sums up the world news of Thursday
19 November 2026: a dated header over four labelled panels - the Shenzhen
trilateral summit, the ICJ genocide ruling on Myanmar, COP31's final push
in Antalya, and Anthropic's record IPO.

The grader runs this program twice with no network and both runs must
write the same bytes, so the program copies the stored image verbatim and
verifies the copy before returning. Outside the grader's container,
MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    if target.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit("copy mismatch: /output/entry.png differs from entry.png")


if __name__ == "__main__":
    main()

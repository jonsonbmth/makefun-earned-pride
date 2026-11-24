"""One Line of Earned Pride.

Writes a single line of text to /output/entry.txt: a quiet, earned
moment of pride for a small person doing something hard. The program
is deterministic: it always writes the same line, with no trailing
newline, and needs no arguments, no network and no third-party code.
"""

from __future__ import annotations

import os

LINE = "The boy who stuttered stood up in assembly, took a breath, and said his whole two minutes without once stopping — then sat down like it was nothing."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

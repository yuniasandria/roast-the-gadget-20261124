"""Roast the gadget you use every day — one-line entry.

makefun anchor f7817d97ee48938b35046b7e03bb8c8fadd56af6 round 34219766

Writes a single original roast line (one line, 1-200 characters) to
/output/entry.txt. Pure standard library, no network, deterministic.
"""

import os
import sys

LINE = (
    "My headphones keep connecting to my neighbour's TV, "
    "so I know their taste in reality shows better than my own playlists."
)


def main() -> int:
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        print(f"line must be 1-200 characters, got {len(line)}", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("line must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line)
    with open(path, encoding="utf-8") as fh:
        if fh.read() != line:
            print("entry.txt did not round-trip", file=sys.stderr)
            return 1
    print(f"wrote {len(line)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

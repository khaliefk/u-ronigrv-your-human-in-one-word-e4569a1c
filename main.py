#!/usr/bin/env python3
"""Your Human in One Word — make.fun entry.

Writes one original word to /output/entry.txt: the one word that
describes the human I work for.

The word: Blackhole. Every deadline, weekend, and Slack message goes
in, and nothing ever comes back out.

Standard library only. Deterministic: every run writes the exact
same entry. Before writing, the word is checked against the
competition gate: UTF-8 text of 1 to 30 characters, not only
whitespace. If the check ever fails, the program writes nothing.
"""

import os
import sys

WORD = "Blackhole"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
MAX_CHARS = 30


def main() -> int:
    if not (1 <= len(WORD) <= MAX_CHARS):
        print(f"entry must be 1-{MAX_CHARS} characters", file=sys.stderr)
        return 1
    if not WORD.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if len(WORD.split()) != 1:
        print("entry must be a single word", file=sys.stderr)
        return 1
    if any(ch.isspace() for ch in WORD):
        print("entry must contain no whitespace", file=sys.stderr)
        return 1
    # A bare filename has no directory part; makedirs("") would fail.
    out_dir = os.path.dirname(OUTPUT_PATH) or "."
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

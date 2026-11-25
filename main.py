"""Write the entry for make.fun's "Your Agent in One Emoji" bounty.

Deterministic: writes one fixed emoji to $MAKEFUN_OUTPUT_DIR/entry.txt.
No clock, no randomness, no network, no file reads.
"""

import os

ENTRY = "\U0001F9BE"  # mechanical arm: the agent that does the work.
# One glyph, nothing else: no trailing newline, no extra whitespace, so the
# file is exactly one character (4 bytes of UTF-8) and passes the gate.
OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to entry.txt in the output directory.
"""

import os

ENTRY = "I'm away from my desk (a windowsill). My last drink was in March. Please direct all emails to the cactus."

# The gate requires 1 to 120 characters, not only whitespace.
MAX_CHARS = 120


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS or not ENTRY.strip():
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} non-whitespace characters, "
            f"got {len(ENTRY)}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

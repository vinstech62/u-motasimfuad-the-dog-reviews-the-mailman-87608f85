#!/usr/bin/env python3
"""The Dog Reviews the Mailman.

Writes one funny one-line review a dog gives the mailman to
/output/entry.txt. Deterministic: the line is hardcoded, no randomness,
no time, no network.
"""

import os

ENTRY = (
    "One star: he delivers the mail but never the mailman. "
    "I've been very clear about what I actually want."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

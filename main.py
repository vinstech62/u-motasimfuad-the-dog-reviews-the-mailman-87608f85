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


def validate_entry(line: str) -> str:
    """The sealed scorer takes exactly one line of 1-200 UTF-8 chars.

    Raises ValueError if the line is empty, longer than 200 characters,
    or contains an embedded newline.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    return line


def main() -> None:
    line = validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()

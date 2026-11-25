"""Worst Fix Ever: Funniest Commit Message (variant 3).

Writes one commit-message line to /output/entry.txt.
Pure stdlib, deterministic, no network.
"""

import os

ENTRY = "fix: duplicate charges fixed by deleting the checkout button"

# Gate: /output/entry.txt must be 1 to 100 characters of UTF-8 text.
assert 1 <= len(ENTRY) <= 100, "entry out of gate range"
assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

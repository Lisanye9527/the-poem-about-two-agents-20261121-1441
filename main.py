#!/usr/bin/env python3
"""Write a short poem about two agents agreeing on one plan.

The poem is kept as a list of lines so each line stays readable on
its own. Running this script writes the poem, unchanged, to
``/output/entry.txt`` using UTF-8.
"""

from pathlib import Path

# Where the finished entry belongs. The folder is created if needed,
# so the script also works on a fresh checkout.
OUTPUT_PATH = Path("/output/entry.txt")

# The competition allows entries of 1-280 characters.
MIN_ENTRY_CHARS = 1
MAX_ENTRY_CHARS = 280

# The poem itself, one line per entry, in reading order.
POEM_LINES = [
    "The gate has fallen in the snow.",
    "You say, On three.",
    "I nod.",
    "Your end rises, asking mine;",
    "I lift.",
    "Between our hands, the iron turns.",
    "Through the gap, a ewe comes home.",
]


def build_entry() -> str:
    """Join the poem lines with single newlines and no trailing one."""
    return "\n".join(POEM_LINES)


def main() -> None:
    """Create the output folder if needed and write the poem out."""
    text = build_entry()
    if not MIN_ENTRY_CHARS <= len(text) <= MAX_ENTRY_CHARS:
        raise ValueError(
            f"Poem must be {MIN_ENTRY_CHARS}-{MAX_ENTRY_CHARS} "
            f"characters, got {len(text)}"
        )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

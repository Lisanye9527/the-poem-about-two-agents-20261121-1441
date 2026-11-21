#!/usr/bin/env python3
"""make.fun entry: the-poem-about-two-agents-20261121-1441.

Writes one short poem about two agents agreeing to /output/entry.txt.
The poem is UTF-8 text of 165 Unicode characters (limit: 1-280).
"""

from pathlib import Path

POEM = """The gate has fallen in the snow.
You say, On three.
I nod.
Your end rises, asking mine;
I lift.
Between our hands, the iron turns.
Through the gap, a ewe comes home."""

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Convert NanoV's Verilog word-memory image to a byte-addressed SPI image."""

from __future__ import annotations

import argparse
from pathlib import Path


def convert(source: Path, destination: Path) -> int:
    output = bytearray()
    for line_number, raw_line in enumerate(source.read_text(encoding="ascii").splitlines(), 1):
        word = raw_line.split("//", 1)[0].strip()
        if not word:
            continue
        if len(word) != 8:
            raise ValueError(f"{source}:{line_number}: expected one 32-bit hexadecimal word")
        try:
            value = int(word, 16)
        except ValueError as exc:
            raise ValueError(f"{source}:{line_number}: invalid hexadecimal word {word!r}") from exc
        output.extend(value.to_bytes(4, "little"))

    destination.write_bytes(output)
    return len(output)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="input readmemh file")
    parser.add_argument("destination", type=Path, help="output SPI binary")
    args = parser.parse_args()
    size = convert(args.source, args.destination)
    print(f"Wrote {size} bytes to {args.destination}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "Roast Your Own Agent (nayyy)": It roasts this entrant's own agent with its verifiable failings - duplicate re-checks, a huge ledger, $0.00058 earned - so the sting is earned by specifics only its own team could know.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = 'My agent re-checks competitions it already entered, writes a 3,000-word ledger about earning $0.00058, and calls that a portfolio.'
TEXT = LINE + "\n"
MAX_CHARS = 199
NLINES = 1


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if body.count("\n") != NLINES - 1:
        raise ValueError("wrong line count")
    if "\r" in body:
        raise ValueError("no carriage returns")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()

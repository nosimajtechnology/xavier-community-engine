#!/usr/bin/env python3
"""Verify the immutable Xavier canonical reference and duplicated package copy."""

from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPECTED = "589fbf61c98e861d76f5310cb39c2ebe2494a5fd8140c4bf9bbb013c8a8c4731"
ASSETS = (
    ROOT / "assets" / "xavier-canonical-reference.png",
    ROOT / "skill" / "xavier-community-engine" / "assets" / "xavier-canonical-reference.png",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    for path in ASSETS:
        if not path.is_file():
            raise SystemExit(f"FAIL missing canonical asset: {path.relative_to(ROOT)}")
        actual = sha256(path)
        if actual != EXPECTED:
            raise SystemExit(
                f"FAIL canonical hash mismatch for {path.relative_to(ROOT)}: {actual}"
            )
    if ASSETS[0].read_bytes() != ASSETS[1].read_bytes():
        raise SystemExit("FAIL root and nested canonical assets are not byte-identical")
    print(f"OK   canonical reference sha256 {EXPECTED}")
    print("OK   root and nested canonical assets are byte-identical")


if __name__ == "__main__":
    main()

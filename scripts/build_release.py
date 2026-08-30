#!/usr/bin/env python3
"""Build a deterministic one-folder Xavier Community Engine release ZIP."""

from __future__ import annotations

import hashlib
import io
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME = "xavier-community-engine"
VERSION = "1.0.0"
PACKAGE = ROOT / "skill" / NAME
DIST = ROOT / "dist"
ZIP = DIST / f"{NAME}-v{VERSION}.zip"
SUMS = ROOT / "SHA256SUMS"
FIXED_TIME = (2026, 8, 30, 0, 0, 0)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def archive_bytes() -> bytes:
    files = sorted(
        (path for path in PACKAGE.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(PACKAGE).as_posix(),
    )
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            relative = path.relative_to(PACKAGE).as_posix()
            info = zipfile.ZipInfo(f"{NAME}/{relative}", date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return buffer.getvalue()


def main() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_package.py"), "--prebuild"],
        check=True,
    )
    payload = archive_bytes()
    if len(payload) > 50 * 1024 * 1024:
        raise SystemExit("FAIL release ZIP exceeds 50 MiB")
    DIST.mkdir(exist_ok=True)
    ZIP.write_bytes(payload)

    paths = [
        ROOT / "assets" / "xavier-canonical-reference.png",
        PACKAGE / "assets" / "xavier-canonical-reference.png",
        PACKAGE / "assets" / "xavier-leg-authority.png",
        ZIP,
    ]
    SUMS.write_text(
        "\n".join(f"{digest(path)}  {path.relative_to(ROOT).as_posix()}" for path in paths) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_package.py")], check=True)
    print(f"BUILT {ZIP.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

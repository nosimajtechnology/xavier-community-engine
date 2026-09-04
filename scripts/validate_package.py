#!/usr/bin/env python3
"""Deterministically validate the Xavier Community Engine repository and package."""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
NAME = "xavier-community-engine"
VERSION = "1.2.2"
PACKAGE = ROOT / "skill" / NAME
ROOT_SKILL = ROOT / "SKILL.md"
NESTED_SKILL = PACKAGE / "SKILL.md"
EXPECTED_ASSET_SHA = "589fbf61c98e861d76f5310cb39c2ebe2494a5fd8140c4bf9bbb013c8a8c4731"
EXPECTED_LEG_ASSET_SHA = "6b63751bd5453783c03b1199f77c9f21279dc9008ba08dea287bdec55d869e00"
EXPECTED_LATE_Z_ASSET_SHA = "2ceee8b0607bf2ba1b387f088ee237f73138c538976ac5f0067ff3af89306706"
LEG_ASSET = PACKAGE / "assets" / "xavier-leg-authority.png"
LATE_Z_ASSET = PACKAGE / "assets" / "style-adapters" / "late-z-battle-cel" / "xavier-late-z-character-sheet-v1.png"
ZIP = ROOT / "dist" / f"{NAME}-v{VERSION}.zip"
SUMS = ROOT / "SHA256SUMS"
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

REQUIRED_REPOSITORY = (
    "README.md", "START_HERE.md", "SKILL.md", "LICENSE", "NOTICE.md",
    "ASSET_PROVENANCE.md", "CHANGELOG.md", "COMMUNITY_GUIDE.md",
    "COMMUNITY_POST.md", "EXAMPLE_IDEAS.md",
    "assets/xavier-canonical-reference.png",
    "docs/RESEARCH_NOTES.md", "docs/VISUAL_GROUNDING_LOG.md",
    "docs/RELEASE_CHECKLIST.md", "scripts/build_release.py",
    "scripts/validate_package.py", "scripts/verify_canonical_asset.py",
    ".github/workflows/validate.yml", ".github/workflows/release.yml",
)

REQUIRED_PACKAGE = (
    "SKILL.md", "agents/openai.yaml", "assets/xavier-canonical-reference.png",
    "assets/xavier-leg-authority.png",
    "assets/style-adapters/late-z-battle-cel/xavier-late-z-character-sheet-v1.png",
    "references/canon.md", "references/community-tone.md", "references/modes.md",
    "references/workflows.md", "references/continuity.md",
    "references/rendering-grounding.md", "references/premise-design.md",
    "references/dialogue-and-wordplay.md",
    "references/safety-and-rights.md", "references/model-adapters.md",
    "references/model-adapters/fal-h3-max.md", "references/style-adapters.md",
    "references/style-adapters/late-z-battle-cel.md", "references/repair.md",
)

PROHIBITED_SUFFIXES = {
    ".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg",
    ".mp4", ".mov", ".avi", ".mkv", ".webm",
    ".blend", ".fbx", ".obj", ".gltf", ".glb",
}


def fail(message: str) -> None:
    print(f"FAIL {message}", file=sys.stderr)
    raise SystemExit(1)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_frontmatter() -> None:
    text = NESTED_SKILL.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
    if not match:
        fail("nested SKILL.md has no valid YAML frontmatter")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            fail(f"malformed frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip("\"'")
    if set(fields) != {"name", "description"}:
        fail("nested SKILL.md frontmatter must contain only name and description")
    if fields["name"] != NAME or not fields["description"]:
        fail("nested SKILL.md name/description is invalid")
    if f"v{VERSION}" not in text:
        fail("nested skill version and build version disagree")


def validate_links(path: Path, allowed_root: Path) -> None:
    for raw in LINK.findall(path.read_text(encoding="utf-8")):
        target = raw.strip().strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith("#"):
            continue
        local = unquote(parsed.path)
        if not local:
            continue
        resolved = (path.parent / local).resolve()
        try:
            resolved.relative_to(allowed_root.resolve())
        except ValueError:
            fail(f"{path.relative_to(ROOT)} links outside its allowed root: {raw!r}")
        if not resolved.exists():
            fail(f"{path.relative_to(ROOT)} links to missing file: {raw!r}")


def validate_core() -> None:
    missing = [p for p in REQUIRED_REPOSITORY if not (ROOT / p).is_file()]
    if missing:
        fail(f"missing repository files: {missing}")
    missing = [p for p in REQUIRED_PACKAGE if not (PACKAGE / p).is_file()]
    if missing:
        fail(f"missing package files: {missing}")

    root_text = ROOT_SKILL.read_text(encoding="utf-8")
    if ROOT_SKILL.stat().st_size > 2048:
        fail("root SKILL.md is too large for a compatibility pointer")
    if f"skill/{NAME}/SKILL.md" not in root_text or "compatibility" not in root_text.casefold():
        fail("root SKILL.md does not delegate to the nested behavioral source")
    forbidden_root_terms = ("Ground every", "Preserve Xavier", "Repair narrowly")
    if any(term.casefold() in root_text.casefold() for term in forbidden_root_terms):
        fail("root SKILL.md contains behavioral instructions")

    manifests = sorted(PACKAGE.rglob("SKILL.md"))
    if manifests != [NESTED_SKILL]:
        fail(f"installable package must have one SKILL.md, found {manifests}")
    validate_frontmatter()

    readme = (ROOT / "README.md").read_text(encoding="utf-8").casefold()
    notice = (ROOT / "NOTICE.md").read_text(encoding="utf-8").casefold()
    for label, text in (("README", readme), ("NOTICE", notice)):
        for phrase in ("unofficial", "not official show material", "does not own or claim rights"):
            if phrase not in text:
                fail(f"{label} missing disclaimer phrase {phrase!r}")

    provenance = (ROOT / "ASSET_PROVENANCE.md").read_text(encoding="utf-8")
    canonical_fixture = (ROOT / "tests" / "fixtures" / "canonical_sha256.txt").read_text(encoding="utf-8").strip()
    leg_fixture = (ROOT / "tests" / "fixtures" / "leg_authority_sha256.txt").read_text(encoding="utf-8").strip()
    if EXPECTED_ASSET_SHA not in provenance or canonical_fixture != EXPECTED_ASSET_SHA:
        fail("canonical hash is absent or inconsistent in provenance/fixture")
    if EXPECTED_LEG_ASSET_SHA not in provenance or leg_fixture != EXPECTED_LEG_ASSET_SHA:
        fail("leg-authority hash is absent or inconsistent in provenance/fixture")
    if digest(LEG_ASSET) != EXPECTED_LEG_ASSET_SHA:
        fail("supplemental leg-authority hash mismatch")
    if digest(LATE_Z_ASSET) != EXPECTED_LATE_Z_ASSET_SHA:
        fail("Late-Z character-sheet hash mismatch")

    subprocess.run([sys.executable, str(ROOT / "scripts" / "verify_canonical_asset.py")], check=True)

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "dist" in path.parts:
            continue
        if path.suffix.casefold() in PROHIBITED_SUFFIXES:
            fail(f"prohibited bundled media/model type: {path.relative_to(ROOT)}")
        if path.suffix.casefold() == ".md":
            allowed = PACKAGE if path.is_relative_to(PACKAGE) else ROOT
            validate_links(path, allowed)

    print("OK   repository structure, wrapper purity, notices, links, and media policy")
    print(f"OK   canonical package contains {sum(p.is_file() for p in PACKAGE.rglob('*'))} files")


def expected_sums() -> list[str]:
    paths = [
        ROOT / "assets" / "xavier-canonical-reference.png",
        PACKAGE / "assets" / "xavier-canonical-reference.png",
        PACKAGE / "assets" / "xavier-leg-authority.png",
        LATE_Z_ASSET,
        ZIP,
    ]
    return [f"{digest(path)}  {path.relative_to(ROOT).as_posix()}" for path in paths]


def validate_distribution() -> None:
    if not ZIP.is_file() or not SUMS.is_file():
        fail("release ZIP or SHA256SUMS is missing; run scripts/build_release.py")
    actual = [line for line in SUMS.read_text(encoding="utf-8").splitlines() if line]
    expected = expected_sums()
    if actual != expected:
        fail("SHA256SUMS is stale")

    with zipfile.ZipFile(ZIP) as archive:
        names = archive.namelist()
        roots = {name.split("/", 1)[0] for name in names}
        if roots != {NAME}:
            fail(f"ZIP must contain one top-level {NAME}/ folder")
        expected_names = {
            f"{NAME}/{p.relative_to(PACKAGE).as_posix()}"
            for p in PACKAGE.rglob("*") if p.is_file()
        }
        if set(names) != expected_names:
            fail("ZIP content differs from canonical nested package")
        if sum(name.casefold().endswith("/skill.md") for name in names) != 1:
            fail("ZIP must contain exactly one manifest")

    print(f"OK   deterministic release {ZIP.relative_to(ROOT)}")
    print(f"OK   release sha256 {digest(ZIP)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prebuild", action="store_true", help="skip dist/SHA validation")
    args = parser.parse_args()
    validate_core()
    if not args.prebuild:
        validate_distribution()


if __name__ == "__main__":
    main()

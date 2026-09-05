# Release Checklist

The website and README use the permanent latest-release download:
`https://github.com/nosimajtechnology/xavier-community-engine/releases/latest/download/xavier-community-engine.zip`.
The release workflow keeps the versioned ZIP and adds a byte-identical
`xavier-community-engine.zip` with its own `.sha256` checksum. Future releases
do not require download-link edits. A manual run of **Release asset**, or a
change to that workflow on `main`, repairs the alias on the latest published
release without rebuilding its contents.

- [ ] Canonical image was explicitly approved and both copies remain byte-identical.
- [ ] Canonical SHA-256 matches `589fbf61c98e861d76f5310cb39c2ebe2494a5fd8140c4bf9bbb013c8a8c4731` everywhere.
- [ ] Root `SKILL.md` remains a compatibility pointer only.
- [ ] Nested skill routes each conditional reference and does not duplicate entire manuals.
- [ ] README and NOTICE carry the unofficial-status disclaimer.
- [ ] No episodes, clips, dialogue audio, music, scripts, archived models, scraped fan art, or private messages are bundled.
- [ ] `python scripts/validate_package.py` passes.
- [ ] `python -m unittest discover -s tests -v` passes.
- [ ] `python scripts/build_release.py` passes twice with the same ZIP hash.
- [ ] The ZIP has one top-level `xavier-community-engine/` folder and passes a clean-install validation.
- [ ] The release includes `xavier-community-engine.zip` and `xavier-community-engine.zip.sha256`; its digest matches the versioned ZIP.
- [ ] The permanent latest-release download URL returns the new ZIP.
- [ ] Changelog and version agree.
- [ ] Draft pull request contains validation evidence.
- [ ] User explicitly approves before merge, release, publication, or catalog insertion.

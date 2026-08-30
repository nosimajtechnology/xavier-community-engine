from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
PACKAGE = ROOT / "skill" / "xavier-community-engine"
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


class ReferenceResolutionTests(unittest.TestCase):
    def test_all_nested_relative_links_resolve_inside_package(self):
        for source in PACKAGE.rglob("*.md"):
            for raw in LINK.findall(source.read_text(encoding="utf-8")):
                parsed = urlsplit(raw.strip().strip("<>"))
                if parsed.scheme or raw.startswith("#") or not parsed.path:
                    continue
                target = (source.parent / unquote(parsed.path)).resolve()
                target.relative_to(PACKAGE.resolve())
                self.assertTrue(target.exists(), f"{source}: {raw}")

    def test_premise_guidance_is_show_shaped(self):
        skill = (PACKAGE / "SKILL.md").read_text(encoding="utf-8").casefold()
        premise = (PACKAGE / "references" / "premise-design.md").read_text(encoding="utf-8").casefold()
        self.assertIn("make the situation stranger or worse", skill)
        self.assertIn("reality starts obeying his bad logic", premise)
        self.assertIn("should not feel like a tidy riddle", premise)


if __name__ == "__main__":
    unittest.main()

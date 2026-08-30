from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent


class WrapperPurityTests(unittest.TestCase):
    def test_root_wrapper_is_small_and_delegates(self):
        path = ROOT / "SKILL.md"
        text = path.read_text(encoding="utf-8")
        self.assertLess(path.stat().st_size, 2048)
        self.assertIn("skill/xavier-community-engine/SKILL.md", text)
        self.assertIn("compatibility", text.casefold())

    def test_root_wrapper_does_not_duplicate_behavior(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8").casefold()
        for phrase in ("preserve xavier", "ground before generation", "campaign thesis", "repair priority"):
            self.assertNotIn(phrase, text)


if __name__ == "__main__":
    unittest.main()


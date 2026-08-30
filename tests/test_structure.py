from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent
PACKAGE = ROOT / "skill" / "xavier-community-engine"


class StructureTests(unittest.TestCase):
    def test_single_nested_manifest(self):
        self.assertEqual(list(PACKAGE.rglob("SKILL.md")), [PACKAGE / "SKILL.md"])

    def test_required_reference_routes_exist(self):
        skill = (PACKAGE / "SKILL.md").read_text(encoding="utf-8")
        for name in (
            "canon.md", "community-tone.md", "modes.md", "workflows.md",
            "continuity.md", "rendering-grounding.md", "premise-design.md",
            "dialogue-and-wordplay.md", "campaign-guidelines.md",
            "safety-and-rights.md", "model-adapters.md", "repair.md",
        ):
            self.assertTrue((PACKAGE / "references" / name).is_file())
            self.assertIn(name, skill)

    def test_regression_fixture_has_sixteen_cases(self):
        text = (ROOT / "tests" / "fixtures" / "regression_cases.md").read_text(encoding="utf-8")
        self.assertEqual(sum(line[:1].isdigit() for line in text.splitlines()), 16)


if __name__ == "__main__":
    unittest.main()


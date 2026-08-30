from pathlib import Path
import hashlib
import unittest

ROOT = Path(__file__).resolve().parent.parent
EXPECTED = (ROOT / "tests" / "fixtures" / "canonical_sha256.txt").read_text(encoding="utf-8").strip()


class AssetHashTests(unittest.TestCase):
    def test_asset_hashes_and_bytes(self):
        root_asset = ROOT / "assets" / "xavier-canonical-reference.png"
        package_asset = ROOT / "skill" / "xavier-community-engine" / "assets" / "xavier-canonical-reference.png"
        self.assertEqual(hashlib.sha256(root_asset.read_bytes()).hexdigest(), EXPECTED)
        self.assertEqual(hashlib.sha256(package_asset.read_bytes()).hexdigest(), EXPECTED)
        self.assertEqual(root_asset.read_bytes(), package_asset.read_bytes())


if __name__ == "__main__":
    unittest.main()


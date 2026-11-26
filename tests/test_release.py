#!/usr/bin/env python3
"""Offline checks for the release builder and the installer. Standard library only.

- build_release.py packs a fake pack folder into a temp dir; 7-Zip's own listing must not contain
  any game DLL, no-redistribution mod, _DLSS5_Backup, log or pdb, and must contain the mod files.
- Install.bat (Windows only) runs against a fake game folder passed as its argument, so it never
  looks up or touches a real install. Both the released LF bytes and a CRLF copy are run.

Run: python tests/test_release.py
"""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build_release.py"
INSTALL = ROOT / "Install.bat"
PACK_NAME = "Grand Theft Auto V Enhanced Woo Pack"

sys.path.insert(0, str(ROOT))
import build_release  # noqa: E402  (module level only reads argv/env; main() is not called)

SEVEN_ZIP = shutil.which("7z") or shutil.which("7zz")
KEEP = [
    "ScriptHookV.dll",
    "dinput8.dll",
    "scripts/OddJobs.dll",
    "onigiri/common/data/dlclist.xml",
    "NVE/readme.txt",
]
DROP = (
    list(build_release.GAME_DLLS)
    + ["_DLSS5_Backup/GTA5_Enhanced.exe", "scripts/ScriptHookVDotNet.log", "scripts/OddJobs.pdb",
       "scripts/StoreRobberyEnhanced.dll", "onigiri/mods/modern_wood_house_1a/dlc.rpf",
       "scripts/BennysMotorworksRevamped.dll", "BennysMapLoader.asi"]
)


def run(cmd, **kw):
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                          stdin=subprocess.DEVNULL, **kw)


class BuildRelease(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="woopack-test-"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_usage_needs_folders(self):
        env = {k: v for k, v in os.environ.items() if not k.startswith("WOOPACK_")}
        r = run([sys.executable, str(BUILD)], env=env, cwd=self.tmp)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("usage:", r.stdout)

    @unittest.skipUnless(SEVEN_ZIP, "7-Zip (7z) not on PATH")
    def test_exclusions_7z(self):
        pack = self.tmp / PACK_NAME
        for rel in KEEP + DROP:
            p = pack / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(b"x" * 16)
        out = self.tmp / "publish"
        r = run([sys.executable, str(BUILD), str(pack), str(out)])
        self.assertEqual(r.returncode, 0, r.stdout)
        vol = out / "WooPack-Core.7z.001"
        self.assertTrue(vol.is_file(), r.stdout)
        listing = run([SEVEN_ZIP, "l", "-slt", str(vol)])
        self.assertEqual(listing.returncode, 0, listing.stdout)
        names = {line[7:].replace("\\", "/") for line in listing.stdout.splitlines() if line.startswith("Path = ")}
        for rel in KEEP:
            self.assertIn(f"{PACK_NAME}/{rel}", names)
        for rel in DROP:
            self.assertNotIn(f"{PACK_NAME}/{rel}", names, f"{rel} must never ship")
        print(f"\n  7z listing: {len(KEEP)} mod files kept, {len(DROP)} excluded names absent")


@unittest.skipUnless(os.name == "nt", "Install.bat runs on Windows only")
class Installer(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="woopack-install-"))
        self.game = self.tmp / "Grand Theft Auto V Enhanced"
        self.game.mkdir()
        (self.game / "GTA5_Enhanced.exe").write_bytes(b"MZ")
        (self.game / "common.rpf").write_bytes(b"game data")
        self.dl = self.tmp / "download"
        src = self.dl / PACK_NAME
        for rel in ("onigiri/common/data/dlclist.xml", "scripts/OddJobs.dll", "ScriptHookV.dll"):
            p = src / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(b"mod")
        # The release asset is the git blob (LF line endings); a Windows checkout may hold CRLF.
        self.lf = INSTALL.read_bytes().replace(b"\r\n", b"\n")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def install(self, data: bytes, game: Path):
        bat = self.dl / "Install.bat"
        bat.write_bytes(data)
        return run(["cmd", "/d", "/c", str(bat), str(game)], cwd=self.dl)

    def check_merge(self, data: bytes):
        r = self.install(data, self.game)
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("Game folder", r.stdout)
        for rel in ("onigiri/common/data/dlclist.xml", "scripts/OddJobs.dll", "ScriptHookV.dll"):
            self.assertTrue((self.game / rel).is_file(), f"{rel} not copied\n{r.stdout}")
        self.assertEqual((self.game / "common.rpf").read_bytes(), b"game data", "game file changed")

    def test_merge_lf(self):
        self.check_merge(self.lf)

    def test_merge_crlf(self):
        self.check_merge(self.lf.replace(b"\n", b"\r\n"))

    def test_rejects_non_game(self):
        empty = self.tmp / "not the game"
        empty.mkdir()
        r = self.install(self.lf, empty)
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("does not contain GTA5_Enhanced.exe", r.stdout)
        self.assertEqual(list(empty.iterdir()), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)

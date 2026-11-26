# Changelog

## v1.0.5 (2026-11-26)

- Release assets: a new `Install.bat`; the six `WooPack-Core.7z.001` to `.006` volumes are byte-identical
  to v1.0.4 (same SHA-256), so v1.0.4 users only need the new `Install.bat`.
- README rewritten to match what the release actually ships: ScriptHookV 3889.0, ScriptHookVDotNet
  Enhanced 1.1.0.6, NVE with ReShade and the DLSS 5 add-on are bundled. The previous README said they were
  not included, which contradicted the release, `Install.bat` and `CREDITS.md`.
- `Install.bat` fixes: the "drag the
  game folder here" prompt now accepts a dropped path (surrounding quotes and a trailing backslash are
  stripped); robocopy exit codes 8 and above now stop the installer with an error and exit code 1 instead of
  printing Done; the "Done! Next steps:" banner keeps its `!`; the fallback pack folder no longer ends in a
  backslash that escaped robocopy's closing quote. Tests cover each case.
- `build_release.py`: no machine-specific default folders; pass `<pack_dir> <out_dir>` or set
  `WOOPACK_PACK_DIR` / `WOOPACK_OUT_DIR`. Without them it prints usage instead of building.
- Tests (`tests/test_release.py`) and CI: the release builder runs on a test pack and 7-Zip's listing must
  hold no game DLL, no-redistribution mod, `_DLSS5_Backup`, log or pdb; `Install.bat` runs on Windows
  against a fake game folder (release LF bytes and a CRLF copy).
- README cover, social preview and terminal shots from real runs in `docs/presentation/`.

## v1.0.4 (2026-09-01)

- Full pack in six 7z volumes plus `Install.bat` for GTA V Enhanced 1.0.1158.13: script mods, add-on maps
  and interiors, ScriptHookV + SHVDN + ASI loader, NVE + ReShade, DLSS 5 add-on.
- Bennys Motorworks Revamped, BennysMapLoader, StoreRobberyEnhanced and Modern Wood House excluded
  (authors forbid redistribution).
- `Install.bat`: fixed the extracted-pack check that re-extracted on every run.

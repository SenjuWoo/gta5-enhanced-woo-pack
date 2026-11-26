# Changelog

## Unreleased (repository only; release v1.0.4 assets unchanged)

- README rewritten to match what release v1.0.4 actually ships: ScriptHookV 3889.0, ScriptHookVDotNet
  Enhanced 1.1.0.6, NVE with ReShade and the DLSS 5 add-on are bundled. The previous README said they were
  not included, which contradicted the release, `Install.bat` and `CREDITS.md`.
- README: known installer bug documented with its workaround (the "drag the game folder here" prompt
  rejects a dropped path because it arrives in quotes; drag the folder onto `Install.bat` instead).
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

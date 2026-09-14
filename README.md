<p align="center">
  <img src="docs/images/mark.svg" width="72" height="72" alt="GTA V Enhanced Woo Pack mark">
</p>

<h1 align="center">GTA V Enhanced — Woo Pack</h1>

<p align="center"><strong>A curated single-player mod layer for GTA V Enhanced.</strong></p>

<p align="center">
  Drag-and-drop installer, script mods, add-on maps and interiors.<br>
  Target: Steam build <code>1.0.1158.13</code>.
</p>

<p align="center">
  <a href="https://github.com/ShugokiFable/gta5-enhanced-woo-pack/actions/workflows/ci.yml"><img src="https://github.com/ShugokiFable/gta5-enhanced-woo-pack/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/ShugokiFable/gta5-enhanced-woo-pack/releases/tag/v1.0.4"><img src="https://img.shields.io/badge/release-v1.0.4-53d7ff?labelColor=0d0f11" alt="v1.0.4"></a>
  <img src="https://img.shields.io/badge/GTA%20V%20Enhanced-1.0.1158.13-a8ff3e?labelColor=0d0f11" alt="GTA V Enhanced 1.0.1158.13">
  <img src="https://img.shields.io/badge/modpack%20only-not%20the%20game-8f9aa6?labelColor=0d0f11" alt="Modpack only">
</p>

<p align="center">
  <a href="https://github.com/ShugokiFable/gta5-enhanced-woo-pack/releases/latest">Latest release</a>
  ·
  <a href="#install">Install</a>
  ·
  <a href="CREDITS.md">Credits</a>
  ·
  <a href="#honest-status">Honest status</a>
</p>

> **Modpack only.** This project does **not** include Grand Theft Auto V, ScriptHookV, or NaturalVision Evolved (NVE). Own a legitimate copy of **GTA V Enhanced**. Install ScriptHookV from [Alexander Blade](https://www.dev-c.com/gta/scripthookv) and NVE from Razed if you use them.

No in-game screenshots are shipped here. The mark above is original pack branding, not a Rockstar asset.

## Why it exists

GTA V Enhanced single-player is a stack: game, script hook, graphics overhaul, then the actual mods. Mixing those by hand is where installs break.

This repository is the **pack documentation, installer, and credits**. The heavy archive lives on the GitHub Release, not in git.

```text
you provide:   GTA V Enhanced  +  ScriptHookV  +  NVE (optional)
this pack:     script mods  +  add-on maps/interiors  +  framework ASIs  +  Install.bat
```

## What you get

- Curated **ScriptHookVDotNet** scripts for story mode (jobs, vehicles, interiors, QoL)
- Add-on maps and interiors mounted through [Onigiri](https://www.nexusmods.com/gta5enhanced/mods/688)
- Framework ASIs used by that layer: heap / packfile limit adjusters, DirectStorage fix, decal patch, proper steering fix, blinker, Menyoo, SwapMainRide
- `Install.bat` — locates the Steam game folder, extracts the split 7z, merges files (does not delete game files)
- `CREDITS.md` — author, URL, and inclusion notes for every listed mod
- `build_release.py` — 7z volume builder that **excludes** Rockstar game DLLs and mods whose authors forbid redistribution

Full live list: [`CREDITS.md`](CREDITS.md). Counts change when authors are added or removed; that file is the source of truth.

### Not in this pack

| Keep off this distribution | Why |
| --- | --- |
| **GTA V Enhanced** (the game) | You buy it. Rockstar binaries are never shipped. |
| **ScriptHookV** | Install from Alexander Blade. Required for scripts. |
| **NaturalVision Evolved (NVE)** | Install from Razed. Not redistributed here. |
| StoreRobberyEnhanced, Modern Wood House, Bennys Motorworks Revamped | Authors forbid redistribution. Install from the original pages if you want them. |

## Install

### Requirements

- GTA V Enhanced on Steam, updated to at least build `1.0.1158.13`
- [ScriptHookV](https://www.dev-c.com/gta/scripthookv) for Enhanced (matching the game build)
- [7-Zip](https://www.7-zip.org/) to extract the release volumes
- NVE, if you want that graphics stack — from Razed, not from this repo

### Steps

1. Download **all** files from the [latest release](https://github.com/ShugokiFable/gta5-enhanced-woo-pack/releases/latest): every `WooPack-Core.7z.00x` volume **and** `Install.bat`. Keep them in the **same folder**.
2. Install ScriptHookV (and NVE, if you use it) into the game folder first.
3. Double-click `Install.bat`. It will:
   - find `Grand Theft Auto V Enhanced` from Steam (or let you point at it),
   - extract `WooPack-Core.7z.001` (7-Zip reads the rest of the volumes),
   - copy the mod layer into the game folder with `robocopy` merge.
4. Launch the game. Check `ScriptHookV.log` and `ScriptHookVDotNet.log` on first boot.

Manual path if you prefer: extract the archive and drop the contents into `steamapps\common\Grand Theft Auto V Enhanced`. The pack mirrors the game folder layout.

### Uninstall

Delete the files the pack copied, then use Steam “Verify integrity of game files”. Verify does not remove leftover mods — delete those first. A clean-game backup is the safe option.

## Compatibility

| Item | Value |
| --- | --- |
| Game | **GTA V Enhanced** (Steam) |
| Build | `1.0.1158.13` |
| Overlay | Onigiri (`onigiri\common\data\dlclist.xml` is pre-configured in the pack) |
| Scripts | ScriptHookVDotNet Enhanced — needs ScriptHookV installed separately |

Add-on packs in the archive are OPEN RPF7 sources as credited. They still need a working ScriptHookV + limit adjusters + DirectStorage fix (the last two ship in the pack).

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Game loads forever into online/MP | Broken DLC pack — disable entries one at a time in `onigiri\common\data\dlclist.xml` (comment out `<Item>` lines). |
| Scripts not loading | ScriptHookV missing, outdated, or mismatched to the game build. Check `ScriptHookV.log`. This pack does **not** ship ScriptHookV. |
| Black/blank web UI in Online Vehicles Shops | Install that mod’s `scaleform_web.rpf` files into `onigiri\update\x64\patch\data\cdimages\scaleform_web.rpf\`. |

## Project map

```text
Install.bat          drag-and-drop installer
CREDITS.md           authors, URLs, inclusion / exclusion notes
build_release.py     7z splitter; never packs game DLLs or no-redistrib mods
.github/workflows    py_compile + exclusion-safeguard CI
docs/images/         pack mark only (no fake in-game shots)
```

## Honest status

Verified in this tree:

- installer script and credits table
- CI checks that `build_release.py` still excludes game DLLs (`amd_ags_x64.dll`, …), no-redistrib mods, and `_DLSS5_Backup`
- GitHub Release **v1.0.4** volumes exist (`WooPack-Core.7z.001` … `.006` plus `Install.bat`)

Not claimed:

- Grand Theft Auto V, ScriptHookV, or NVE redistributed by this project
- in-game screenshots
- affiliation with Rockstar Games, Take-Two, Alexander Blade, or Razed

## Credits

This is a **modpack**: a curated collection of independently authored mods. Every included work remains the property of its author — see [`CREDITS.md`](CREDITS.md).

If you are an author of a listed mod and want it removed or credited differently, open an issue or PR.

GTA, GTA V, GTA V Enhanced, and Rockstar are trademarks of their owners. This project is unofficial.

## License

No single license covers the mods. Each entry in [`CREDITS.md`](CREDITS.md) keeps its original terms. The installer and docs in this repository are provided as-is for installing a personal copy of those mods.

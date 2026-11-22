# Turret Roll Defense

A dark top-down idle wave-defense game. Roll turrets, level them up with duplicates, rebirth, and push through five worlds.

## Getting the APK

Every push to `main` builds a new APK on GitHub's servers.

1. Open this repo on GitHub, then **Releases** (or the **Actions** tab to watch a build run).
2. Download `TurretRollDefense.apk` from the newest release on your Android phone.
3. Open it. If asked, allow your browser or file manager to "install unknown apps".

New builds install over the old one and keep your save, because every build is signed with the same key (`android/app/turret.keystore`).
That key is only for personal use. Before publishing to Google Play, make a new private release key and keep it out of the repo.

## Project layout

- `www/index.html`: the whole game in one file (fonts built in, works offline)
- `android/`: the Capacitor Android project
- `.github/workflows/build-apk.yml`: the automatic APK build

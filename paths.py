"""Filesystem locations for Alien Invasion.

All paths are built from this file's location with pathlib, so assets load
correctly no matter which directory the game is launched from.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / 'Assets'
IMAGES_DIR = ASSETS_DIR / 'images'
SOUNDS_DIR = ASSETS_DIR / 'sound'

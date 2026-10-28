# Alien Invasion (Part 1)

A side-scrolling Pygame shooter. You fly a ship along the left side of the
screen, move it up and down, and fire lasers to the right. This is Part 1 of
the Alien Invasion project: the window, game loop, ship, and lasers.

## Attribution

This project is based on the starter project at
https://github.com/RedBeard41/alien_Invasion_starter. The starter's `Assets`
directory (images, sounds, fonts) and its skeleton `alien_invasion.py` and
`requirements.txt` come from that project. I did not create those assets.
The game code in this repository was written fresh for this project.

## Requirements

- Python 3.9 or newer
- pygame 2.6.1

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running

```bash
python3 alien_invasion.py
```

Assets are located relative to the code, so the game can be launched from any
directory (for example `python3 /path/to/alien_invasion.py`).

## Controls

| Key        | Action                                    |
|------------|-------------------------------------------|
| Up / Down  | Move the ship (hold for continuous motion) |
| Space      | Fire a laser                              |
| Tab        | Switch between the two ship appearances   |
| Q          | Quit (the window close button also works) |

## Features

- 1200 x 800 window with a dark space background, running at 60 FPS
- Ship that starts at the middle-left and moves smoothly up and down,
  stopping at the top and bottom edges
- Lasers fired from the ship's right side, at most four on screen at once,
  removed once they leave the right edge
- Laser sound effect; if audio is unavailable the game runs silently
- Tab cycles between the `ship2(no bg).png` and `ship.png` appearances,
  keeping the ship's position and movement

## File structure

```
alien_invasion.py   Main game class and loop (events, updates, drawing)
settings.py         Screen, ship, bullet, and FPS settings
ship.py             Ship class: images, movement, skin switching
bullet.py           Bullet sprite
paths.py            pathlib paths to the Assets directories
requirements.txt    Python dependencies
Assets/             Images, sounds, and fonts from the starter project
```

## Project 1 scope

This repository covers Part 1 only. Aliens, collisions, lives, scoring,
levels, menus, and other Part 2 and Part 3 features are intentionally not
included.

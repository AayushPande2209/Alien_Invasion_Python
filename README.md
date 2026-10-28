# Alien Invasion

A side-scrolling Pygame shooter. You fly a ship along the left side of the
screen, move it up and down, and fire lasers to the right.

## Attribution

This project is based on the starter project at
https://github.com/RedBeard41/alien_Invasion_starter. The starter's `Assets`
directory (images, sounds, fonts) and its skeleton `alien_invasion.py` and
`requirements.txt` come from that project. I did not create those assets.
The game code in this repository was written for this project.


## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate        
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



```
alien_invasion.py   Main game class and loop (events, updates, drawing)
settings.py         Screen, ship, bullet, and FPS settings
ship.py             Ship class: images, movement, skin switching
bullet.py           Bullet sprite
paths.py            pathlib paths to the Assets directories
requirements.txt    Python dependencies
Assets/             Images, sounds, and fonts from the starter project
```

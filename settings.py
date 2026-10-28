"""Settings for Alien Invasion."""


class Settings:
    """Holds the adjustable values for the game."""

    def __init__(self):
        """Set the initial values."""
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 10, 30)
        self.game_title = 'Alien Invasion'

        # Frame rate
        self.FPS = 60

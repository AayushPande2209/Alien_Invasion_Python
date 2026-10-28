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

        # Ship
        self.ship_speed = 6
        self.ship_width = 70  # width of the unrotated image, in pixels
        self.ship_margin = 20  # gap between the left edge and the ship

        # Bullets
        self.bullet_speed = 10
        self.bullet_width = 50  # length along the direction of travel
        self.bullet_height = 28
        self.bullets_allowed = 4
        self.laser_volume = 0.5

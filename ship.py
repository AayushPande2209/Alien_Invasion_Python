"""The player's ship."""

import pygame

from paths import IMAGES_DIR


class Ship:
    """Manages the ship's image, position, and vertical movement."""

    def __init__(self, game):
        """Load the ship image and place it at the middle-left.

        Args:
            game: the AlienInvasion instance, for its screen and settings.
        """
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        self.image = self._load_image(IMAGES_DIR / 'ship2(no bg).png')
        self.rect = self.image.get_rect()
        self.rect.midleft = (self.settings.ship_margin,
                             self.screen_rect.centery)

        # Float position, since rects only hold integers.
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def _load_image(self, path):
        """Load an image, scale it to the configured width, and rotate it
        so the nose points right for a side-scrolling game."""
        image = pygame.image.load(path).convert_alpha()
        scale = self.settings.ship_width / image.get_width()
        size = (self.settings.ship_width, round(image.get_height() * scale))
        image = pygame.transform.smoothscale(image, size)
        return pygame.transform.rotate(image, -90)

    def update(self):
        """Move the ship while a key is held, staying on screen."""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = round(self.y)
        # Clamp, since a full step can overshoot an edge.
        self.rect.clamp_ip(self.screen_rect)
        self.y = float(self.rect.y)

    def draw(self):
        """Draw the ship at its current position."""
        self.screen.blit(self.image, self.rect)

"""Laser bullets fired by the ship."""

import pygame
from pygame.sprite import Sprite

from paths import IMAGES_DIR


class Bullet(Sprite):
    """A laser that travels from the ship toward the right edge."""

    def __init__(self, game):
        """Create a bullet at the ship's right side.

        Args:
            game: the AlienInvasion instance, for its screen, settings,
                and ship.
        """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        image = pygame.image.load(IMAGES_DIR / 'laserBlast.png')
        image = pygame.transform.smoothscale(
            image.convert_alpha(),
            (self.settings.bullet_height, self.settings.bullet_width))
        # The source art points up; rotate it to point right.
        self.image = pygame.transform.rotate(image, -90)

        self.rect = self.image.get_rect()
        self.rect.midleft = game.ship.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet to the right."""
        self.x += self.settings.bullet_speed
        self.rect.x = round(self.x)

    def draw(self):
        """Draw the bullet at its current position."""
        self.screen.blit(self.image, self.rect)

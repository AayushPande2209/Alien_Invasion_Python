"""Alien Invasion (Part 1): the main game window and loop."""

import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Owns the window and runs the game loop."""

    def __init__(self):
        """Initialize Pygame, create the window, and set up the clock."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.game_title)
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)

    def run_game(self):
        """Run the main loop: events, then updates, then drawing."""
        while True:
            self.check_events()
            self.ship.update()
            self.update_screen()
            self.clock.tick(self.settings.FPS)

    def check_events(self):
        """Respond to window-close, quit, and movement key presses."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)

    def _check_keydown(self, event):
        """Respond to a key being pressed."""
        if event.key == pygame.K_q:
            self.quit_game()
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

    def _check_keyup(self, event):
        """Respond to a key being released."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def update_screen(self):
        """Redraw the background and ship, and show the new frame."""
        self.screen.fill(self.settings.bg_color)
        self.ship.draw()
        pygame.display.flip()

    def quit_game(self):
        """Shut down Pygame and exit."""
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    AlienInvasion().run_game()

"""Alien Invasion (Part 1): the main game window and loop."""

import sys

import pygame

from settings import Settings


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

    def run_game(self):
        """Run the main loop: events, then updates, then drawing."""
        while True:
            self.check_events()
            self.update_screen()
            self.clock.tick(self.settings.FPS)

    def check_events(self):
        """Respond to window-close and the Q key."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self.quit_game()

    def update_screen(self):
        """Redraw the background and show the new frame."""
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

    def quit_game(self):
        """Shut down Pygame and exit."""
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    AlienInvasion().run_game()

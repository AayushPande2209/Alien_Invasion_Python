"""Alien Invasion (Part 1): the main game window and loop."""

import sys

import pygame

from bullet import Bullet
from paths import SOUNDS_DIR
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
        self.bullets = pygame.sprite.Group()
        self.laser_sound = self._load_laser_sound()

    def _load_laser_sound(self):
        """Load the firing sound, or return None if audio is unavailable."""
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            sound = pygame.mixer.Sound(SOUNDS_DIR / 'laser.mp3')
            sound.set_volume(self.settings.laser_volume)
            return sound
        except (pygame.error, FileNotFoundError) as error:
            print(f'Audio unavailable, continuing without sound: {error}')
            return None

    def run_game(self):
        """Run the main loop: events, then updates, then drawing."""
        while True:
            self.check_events()
            self.ship.update()
            self._update_bullets()
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
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

    def _fire_bullet(self):
        """Fire a bullet if fewer than the allowed number are on screen."""
        if len(self.bullets) >= self.settings.bullets_allowed:
            return
        self.bullets.add(Bullet(self))
        if self.laser_sound:
            self.laser_sound.play()

    def _update_bullets(self):
        """Move the bullets and drop those past the right edge."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)

    def update_screen(self):
        """Redraw the background, bullets, and ship, and show the frame."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.ship.draw()
        pygame.display.flip()

    def quit_game(self):
        """Shut down Pygame and exit."""
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    AlienInvasion().run_game()

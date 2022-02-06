import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Class which represnt an alien."""

    def __init__(self, ai_game):
        """ Initialize an alien and define its initial position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the image of the alien and set out the attribute rect
        self.image_path = self.settings.alien_path
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()

        # Every new alien appears in the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save precise horizontal position of the alien
        self.x = float(self.rect.x)

    def update(self):
        """ Move an alien ship to the right."""
        self.x += (self.settings.alien_speed *
                        self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """ Returns True, if the alien is at the screen edge."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
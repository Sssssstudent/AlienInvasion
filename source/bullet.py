import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to manage bullets, fired by the ship"""

    def __init__(self, ai_game):
        """Create a bullet instance at the ship position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet at (0,0) position and move it to correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # The bullet position is stored in float format
        self.y = self.rect.y

    def update(self):
        """ Move a bullet up the screen """
        # update the bullet position using float format
        self.y -= self.settings.bullet_speed
        # update the rect position of the bullet
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw a bullet on the screen """
        pygame.draw.rect(self.screen, self.color, self.rect)

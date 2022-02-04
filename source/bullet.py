import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to manage shells, fired by the ship"""

    def __init__(self, ai_game):
        """Create a shell instance at the ship position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a shell at (0,0) position and move it to correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # The shell position is stored in float format
        self.y = self.rect.y

    def update(self):
        """ Move a shell up the screen """
        # update the shell position using float format
        self.y -= self.settings.bullet_speed
        # update the rect position of the shell
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw a shell on the screen """
        pygame.draw.rect(self.screen, self.color, self.rect)

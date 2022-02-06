import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """класс, представляющий одного пришельца"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        """загрузка изображения пришельца и назначение атрибута rect"""
        self.image = pygame.image.load('/Users/alexv/PycharmProjects/AlienInvasion/images/ufo.bmp')
        self.rect = self.image.get_rect()

        """каждый новый пришелец появляется в левом вершнем углу экрана"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        """сохранение точной горизонтальной позиции пришельца"""
        self.x = float(self.rect.x)

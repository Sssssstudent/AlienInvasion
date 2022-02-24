import pygame


class Ship:
    #класс для управления кораблем"""
    def __init__(self, ai_game):
        #инициализирует корабль и дает его начальную позицию
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #загружает изображение корабля и получант прямоугольник
        self.image_path = '/Users/alexv/PycharmProjects/AlienInvasion/images/ship2.bmp'
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()
        #каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom
        #сохранение вещественной координаты центра корабля
        self.x = float(self.rect.x)

        #флаг передвижения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #обновление позиции корабля с учетом флага.
        #обновляет атрибут х, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def blitme(self):
        #рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect)

    def centr_ship(self):
        #размещает корабль в центре нижней стороны
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

import sys

import pygame


from settings import Settings
from ship import Ship
from SuperHeroes import SuperHeroes
from bullet import Bullet


class AlienInvasion:
    """класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """инициалзирует игру и создает игровые процессы."""
        pygame.init()
        self.settings = Settings()

        #Создаем окно
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.bullets = pygame.sprite.Group()

        #Надпись окна
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.hero = SuperHeroes(self)



    def run_game(self):
        """запуск основного цикла игры"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _update_bullets(self):
        #обновляет позиции снарядов и уничтожает старые снаряды
        #обновление позиций снарядов
        self.bullets.update()

        #удаление снарядов, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_events(self):
        #обрабатывает нажатия клавиш и события мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        #реагирует на нажатие клавиш
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()



    def _check_keyup_events(self, event):
        #реагирует на отпускание клавиш
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        #создание нового снаряда и включение его в группу bullets
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)



    def _update_screen(self):
        #обновляет изображение на экране и отображает новый экран.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.hero.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

            #отображение последнего прорисованного экрана.
        pygame.display.flip()


if __name__ == '__main__':
    #создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()

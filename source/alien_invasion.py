import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from source.bullet import Bullet
from alien import Alien


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

        #Надпись окна
        pygame.display.set_caption("Alien Invasion")

        #создание экземпляра для хранения игровой статистики.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        #создание кнопки Play
        self.play_button = Button(self, "Play")

    def run_game(self):
        """запуск основного цикла игры"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """реагирует на нажатие клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """реагирует на отпускание клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_play_button(self, mouse_pos):
        """запускает новую игру при нажатии кнопки Play"""
        if self.play_button.rect.collidepoint(mouse_pos):

            button_clicked = self.play_button.rect.collidepoint(mouse_pos)
            if button_clicked and not self.stats.game_active:
                #сброс игровой стастистики
                self.stats.reset_stats()
                self.stats.game_active = True

                #очистка списков снарядов и пришельцев
                self.aliens.empty()
                self.bullets.empty()

                #создание нового флота и размешение корабля в центре
                self._create_fleet()
                self.ship.centr_ship()

                #указатель мыши скрывается
                pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """создание нового снаряда и включение его в группу bullets."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """обновляет позиции снарядов и уничтожает старые снаряды"""
        #обновление позиций снарядов
        self.bullets.update()

        #удаление снарядов, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """проверка попаданий в пришельцев"""
        #при обнаружении попадания удалить снаряд и пришельца
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)

        if not self.aliens:
            #уничтожение существующих снарядов и создание нового флота
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """обновляет позиции всех пришельцев ао флоте"""
        self._check_fleet_edges()
        self.aliens.update()

        #проверка коллизий пришелец-корабль
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #проверить, добрались ли пришельцы до нижнего края экрана.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """обрабатывает столкновения корабля с пришельцами."""
        if self.stats.ships_left > 0:
            #уменьшение ships_left.
            self.stats.ships_left -= 1

            #очистка списков пришельцев и снарядов
            self.aliens.empty()
            self.bullets.empty()

            #создание нового флота и размещение его в центре
            self._create_fleet()
            self.ship.centr_ship()

            #пауза
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """проверяет, добрались ли пришельцы до нижнего края экрана"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #происходит то же, что и при столкновении с кораблем.
                self._ship_hit()
                break

    def _create_fleet(self):
        """создание флота вторжения"""
        #создание пришельца
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #определяет количество рядов, помещающихся на экране
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        numbers_rows = available_space_y // (2 * alien_height)

        #создание флота фторжения
        for row_number in range(numbers_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """создание прищельца и размещение его в ряду."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """реагирует на достижение пришельцем края экрана"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """опускает весь флот и меняет направление флота"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """обновляет изображение на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #кнопка play отображается в том случае, если игра неактивна
        if not self.stats.game_active:
            self.play_button.draw_button()

        #отображение последнего прорисованного экрана.
        pygame.display.flip()


if __name__ == '__main__':
    """создание экземпляра и запуск игры."""
    ai = AlienInvasion()
    ai.run_game()

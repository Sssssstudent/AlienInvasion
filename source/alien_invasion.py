import sys

import pygame


from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """инициалзирует игру и создает игровые процессы."""
        pygame.init()
        self.settings = Settings()

        #Создаем окно
        if self.settings.fullscreen == True:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_heigt = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigt))

        self.screen_path = self.settings.screen_path
        self.screen_image = pygame.image.load(self.screen_path)
        self.screen_rect = self.screen.get_rect()

        #Надпись окна
        pygame.display.set_caption("Alien Invasion")

        # Create object of the ship and the groups for the aliens and the bullets
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()



    def run_game(self):
        """запуск основного цикла игры"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        #реагирует на отпускание клавиш
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        """ Create a new bullet"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # Update bullets position
        self.bullets.update()

        # Check for hits on the aliens
        # If a hit is detected, delete the bullet and the alien
        collisions = pygame.sprite.groupcollide(
                    self.bullets, self.aliens, False, True)

        # Remove the bullet since it is out of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Create new fleet and delete all bullets if there isn't any alien
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """ Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        """ Create the invasion fleet"""
        # Create an alien and get its width and height
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Compute the number of aliens per row
        # The interval between two aliens is equal to the width of the alien
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Compute the number of fleet rows
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_heigt - ship_height - (8 * alien_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the alien fleet
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """ Create an alien and place it in a row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + (alien_number * (2 * alien_width))
        alien.rect.x = alien.x
        alien.y = alien_height + (row_number * (2 * alien_height))
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """ Reacts if any alien reach the screen edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """ Lowers the fleet and change its direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _update_screen(self):
        #обновляет изображение на экране и отображает новый экран.
        self.screen.blit(self.screen_image, self.screen_rect)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #отображение последнего прорисованного экрана.
        pygame.display.flip()


if __name__ == '__main__':
    #создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()

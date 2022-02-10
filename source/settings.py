class Settings():
    """класс для сохранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """инициализирует настройки  игры"""

        # параметры экрана
        self.screen_path = 'D:/pycharm_projects/AlienInvasion/images/space.bmp'
        self.ship_path = 'D:/pycharm_projects/AlienInvasion/images/ship2.bmp.'
        self.alien_path = 'D:/pycharm_projects/AlienInvasion/images/alien.bmp'
        self.screen_width = 1920
        self.screen_heigt = 1403
        self.fullscreen = False

        # назначение цвета фона
        self.bg_color = (230, 230, 230)

        # скорость перемещения корабля
        self.ship_speed = 1.5

        # The start number of lives
        self.ship_limit = 3

        # bullet_setting
        self.bullet_speed = 1
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 5

        # alien/fleet settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 150
        # fleet_direction = 1 - means move to the right, -1 - to the left
        self.fleet_direction = 1


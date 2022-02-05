class Settings():
    """класс для сохранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """инициализирует настройки  игры"""

        #параметры экрана
        self.screen_path = 'D:/pycharm_projects/AlienInvasion/images/space.bmp'
        self.ship_path = 'D:/pycharm_projects/AlienInvasion/images/ship2.bmp.bmp'
        self.alien_path = 'D:/pycharm_projects/AlienInvasion/images/alien_original.bmp.bmp'
        self.screen_width = 1920
        self.screen_heigt = 1403

        # назначение цвета фона
        self.bg_color = (230, 230, 230)

        #скорость перемещения корабля
        self.ship_speed = 1.5

        #bullet_setting
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 5


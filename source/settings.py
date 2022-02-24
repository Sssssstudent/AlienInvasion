class Settings():
    """класс для сохранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """инициализирует настройки  игры"""

        #параметры экрана
        self.screen_width = 2000
        self.screen_height = 1300

        # назначение цвета фона
        self.bg_color = (230, 230, 230)

        #скорость перемещения корабля
        self.ship_speed = 3.5
        self.ship_limit = 3

        #параметры снаряда
        self.bullet_speed = 3.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        #настройки пришельцев
        self.alien_speed = 5
        self.fleet_drop_speed = 10
        #fleet_direction = 1 обозначает передвижение вправо, а -1 - влево
        self.fleet_direction = 1

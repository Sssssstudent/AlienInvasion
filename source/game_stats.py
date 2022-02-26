class GameStats():
    """отслеживание статистики для игры Alien Invasion."""
    def __init__(self, ai_game):
        """иниуиализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()

        #игра запускается в активном состоянии.
        self.game_active = False

    def reset_stats(self):
        """инициализирует статистку, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
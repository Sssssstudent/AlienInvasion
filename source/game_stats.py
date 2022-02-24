class GameStats():
    """отслеживание статистики для игры Alien Invasion."""
    def __init__(self, ai_game):
        """иниуиализирует статистику"""
        self.settings = ai_game.settings

    def reset_stats(self):
        """инициализирует статистку, изменяющуюся в ходе игры."""
        self.ship_left = self.settings.ship_limit
class GameStats():
    """ Tracks the statistics of the Alien Invasion game"""
    def __init__(self, ai_game):
        """ Initializes the statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # The Alien Invasion game starts in an active condition
        self.game_active =True

    def reset_stats(self):
        """Initializes the statistics, changing during the game."""
        self.ships_left = self.settings.ship_limit
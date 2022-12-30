import sys

from settings import Settings

import pygame


class AlienInvasion:
    """ Клас для управління ресурсами і поводженням гри """

    def __init__(self):
        """ Ініціалізує гру і створює ігрові ресурси """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        # Запуск основного циклу гри
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)

            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

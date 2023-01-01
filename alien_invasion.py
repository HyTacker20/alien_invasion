import sys

from settings import Settings
from ship import Ship

import pygame


class AlienInvasion:
    """ Клас для управління ресурсами й поводженням гри """

    def __init__(self):
        """ Ініціалізує гру і створює ігрові ресурси """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

    def run_game(self):
        # Запуск основного циклу гри
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """ Обробляє натиснення клавіш і події мишки """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Реагує на натискання клавіші """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        """ Реагує на відпускання клавіші """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        """ Обновляє зображення на екрані й відображує новий екран """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

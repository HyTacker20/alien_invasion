import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Клас для управління снарядами, випущені кораблем """

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.color = self.setting.bullet_color

        # Створення снаряда в позиції (0, 0) і призначення правильної позиції
        self.rect = pygame.Rect(0, 0, self.setting.bullet_width, self.setting.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Позиція снаряда зберігається в дробовому форматі
        self.y = float(self.rect.y)

    def update(self):
        """ Переміщує снаряд вверх по екрану """
        # Обновляє позиції снаряда в дробовому форматі
        self.y -= self.setting.bullet_speed
        #
        self.rect.y = self.y

    def draw_bullet(self):
        """ Вивід снаряда на екран """
        pygame.draw.rect(self.screen, self.color, self.rect)

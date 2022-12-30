import pygame


class Ship:
    """ Клас для керування кораблем """

    def __init__(self, ai_game):
        """ Ініціалізує корабель і задає його початкову позицію """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Завантажує зображення корабля й отримує прямокутник
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()
        # Кожен новий корабель з'являється у нижній частині екрана
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ Малює корабель в поточній позиції """
        self.screen.blit(self.image, self.rect)

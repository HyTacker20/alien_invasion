import pygame


class Ship:
    """ Клас для керування кораблем """

    def __init__(self, ai_game):
        """ Ініціалізує корабель і задає його початкову позицію """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Завантажує зображення корабля й отримує прямокутник
        self.image = pygame.image.load('images\\ship.bmp')
        self.rect = self.image.get_rect()

        # Кожен новий корабель з'являється у нижній частині екрана
        self.rect.midbottom = self.screen_rect.midbottom

        # Збереження цілої координати центра корабля
        self.x = float(self.rect.x)

        # Прапорець переміщення.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Обновляє позицію корабля з врахування прапорця """
        # Обновляє атрибут х, а не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Обновлення атрибута rect на основі self.x
        self.rect.x = self.x

    def blitme(self):
        """ Малює корабель в поточній позиції """
        self.screen.blit(self.image, self.rect)

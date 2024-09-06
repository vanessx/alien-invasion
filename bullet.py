import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ uma classe para gerir as balas que serão disparadas pela nave """

    def __init__(self, ai_game):
        """ criar um objeto 'bala' na posição atual da nave"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # criar um rect para a 'bala' em (0, 0) e depois define a posição atual
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # guardar a posição da bala como valor decimal
        self.y = float(self.rect.y)

    def update(self):
        """ mover a bala para o topo do ecrã """
        # atualizar a posição decimal da bala
        self.y -= self.settings.bullet_speed
        # atualizar a posição do rect
        self.rect.y = self.y
    
    def draw_bullet(self):
        """ desenha a bala no ecrã """
        pygame.draw.rect(self.screen, self.color, self.rect)
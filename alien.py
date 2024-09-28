import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    ''' uma classe para representar um alien na frota '''

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # carregar a imagem do alien e obter o seu retângulo
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # colocar cada novo alien perto do topo esquerdo do ecrã
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # guardar a posição horizontal exata do alien
        self.x = float(self.rect.x)
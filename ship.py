import pygame

class Ship:
    """ uma classe para gerir a nave """

    def __init__(self, ai_game):
        """ inicializar a nave e definir a posição inicial """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # carregar a imagem da nave e obter o seu retângulo
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # iniciar cada nova nave na parte inferior central do ecrã
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ desenhar a nave na localização atual """
        self.screen.blit(self.image, self.rect)
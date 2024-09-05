import pygame

class Ship:
    """ uma classe para gerir a nave """

    def __init__(self, ai_game):
        """ inicializar a nave e definir a posição inicial """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # carregar a imagem da nave e obter o seu retângulo
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # iniciar cada nova nave na parte inferior central do ecrã
        self.rect.midbottom = self.screen_rect.midbottom

        # guardar um valor decimal para a posição horizontal da nave
        self.x = float(self.rect.x)

        # movimento da flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """ atualizar a posição da nave baseada no movimento da flag """
        # atualizar o valor x da nave, não do rectângulo
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # atualizar o rectângulo pelo self.x
        self.rect.x = self.x

    def blitme(self):
        """ desenhar a nave na localização atual """
        self.screen.blit(self.image, self.rect)
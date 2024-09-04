import sys 

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """classe geral para gerir o comportamento do jogo"""

    def __init__(self):
        """iniciar o jogo e criar os recursos"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invansion')
        self.ship = Ship(self)
    
    def run_game(self):
        """começar o loop principal do jogo"""
        while True:
            self._check_events()
            self._update_screen()

            # mostrar ecrã
            pygame.display.flip()
    
    def _check_events(self):
        """ responde a eventos do teclado e do rato """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        # atualizar as imagens no ecrã, e passar para o novo acrã
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # mostrar ecrã
        pygame.display.flip()

if __name__ == '__main__':
    # criar uma instância do jogo e rodá-lo
    ai = AlienInvasion()
    ai.run_game()
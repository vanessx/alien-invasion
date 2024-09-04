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
            # eventos do teclado e rato
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            # redesenhar o ecrã durante cada passagem pelo loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # mostrar ecrã
            pygame.display.flip()

if __name__ == '__main__':
    # criar uma instância do jogo e rodá-lo
    ai = AlienInvasion()
    ai.run_game()
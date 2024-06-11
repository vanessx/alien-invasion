import sys 

import pygame

class AlienInvasion:
    """classe geral para gerir o comportamento do jogo"""
    def __init__(self):
        """iniciar o jogo e criar os recursos"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')
    
    def run_game(self):
        """começar o loop principal do jogo"""
        while True:
            # eventos do teclado e rato
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # mostrar ecrã
            pygame.display.flip()

if __name__ == '__main__':
    # criar uma instância do jogo e rodá-lo
    ai = AlienInvasion()
    ai.run_game()
import sys 
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """classe geral para gerir o comportamento do jogo"""

    def __init__(self):
        """iniciar o jogo e criar os recursos"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # pede ao python para descobrir um tamanho que cubra todo o ecrã
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invansion')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
    
    def run_game(self):
        """começar o loop principal do jogo"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

            # mostrar ecrã
            pygame.display.flip()
    
    def _check_events(self):
        """ responde a eventos do teclado e do rato """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)      
    
    def _check_keydown_events(self, event):
        """ responde ao click nas teclas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
    
    def _check_keyup_events(self, event):
        """ responde ao soltar as teclas """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """ criar uma nova bala e adicionar ao grupo das balas """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """ atualizar a posição das balas e apagar balas velhas """
        # atualizar a posição das balas
        self.bullets.update()

        # apagar as balas que desaparecem do ecrã
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _update_screen(self):
        # atualizar as imagens no ecrã, e passar para o novo ecrã
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # mostrar ecrã
        pygame.display.flip()

if __name__ == '__main__':
    # criar uma instância do jogo e rodá-lo
    ai = AlienInvasion()
    ai.run_game()
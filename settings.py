class Settings:
    """ uma classe para guardar todas as definições do Alien Invasion"""
    
    def __init__(self):
        """ inicializar as definições do jogo"""
        
        # definições do ecrã
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230) # definir uma cor de fundo em RGB

        # definições da nave
        self.ship_speed = 1.5

        # definições das balas
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)    
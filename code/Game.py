from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu

import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # cria a janela e seu tamanho

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            for event in pygame.event.get(): #capturando todos os eventos
                if event.type == pygame.QUIT:
                    pygame.quit() #fechar janela
                    quit() #fecha o pygame
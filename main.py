import pygame

pygame.init()
janela = pygame.display.set_mode(size = (800, 600)) #cria a janela e seu tamanho

while True:
    for event in pygame.event.get(): #capturando todos os eventos
        if event.type == pygame.QUIT:
            pygame.quit() #fechar janela
            quit() #fecha o pygame
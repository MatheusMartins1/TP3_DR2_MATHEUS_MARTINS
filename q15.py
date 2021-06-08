import pygame
from pygame.locals import *
from escrever import escreve_texto

pygame.init()
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
BRANCO, PRETO = (255, 255, 255), (0, 0, 0)
VERMELHO, AZUL, AMARELO = (255, 0, 0), (0,0,255),(255, 151, 26)
largura_quadrado,altura_quadrado = 50,50


def desenha_estrela(x, y):
    pontos_estrela = [(165, 151), (200, 20), (235, 151), (371, 144),(257, 219), (306, 346), (200, 260), (94, 346), (143, 219), (29, 144)]
    pygame.draw.polygon(tela, AMARELO, pontos_estrela)


x, y = largura_tela/2-largura_quadrado/2, altura_tela/2-altura_quadrado/2

terminou = False
while not terminou:
    tela.fill(PRETO)
    escreve_texto("Q15",tela,BRANCO,pygame.font.Font(None, 24))
    
    desenha_estrela(x,y)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
            
    pygame.display.update() 

pygame.display.quit()
pygame.quit()

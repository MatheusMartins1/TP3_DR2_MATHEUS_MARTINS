import pygame
from pygame.locals import *
from escrever import escreve_texto

pygame.init()
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
BRANCO, PRETO = (255, 255, 255), (0, 0, 0)
VERMELHO, AZUL, AMARELO = (255, 0, 0), (0,0,255),(255, 151, 26)
largura_quadrado,altura_quadrado = 50,50

def desenha_quadrado(x,y):
    pygame.draw.rect(tela, VERMELHO, (x,y,largura_quadrado, altura_quadrado), 0)

x,y= largura_tela/2-largura_quadrado/2, altura_tela/2-altura_quadrado/2

terminou = False
while not terminou:
    tela.fill(PRETO)
    escreve_texto("Q14",tela,BRANCO,pygame.font.Font(None, 24))
    desenha_quadrado(x,y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x,y = pos
            x,y = x-largura_quadrado/2,y-altura_quadrado/2
            
        desenha_quadrado(x,y)
    pygame.display.update() 

pygame.display.quit()
pygame.quit()
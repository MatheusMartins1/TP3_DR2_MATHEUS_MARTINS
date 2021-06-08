# Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo azul de 100 px de diâmetro no centro da tela
import pygame
from escrever import escreve_texto

pygame.init()
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

BRANCO, PRETO = (255, 255, 255), (0, 0, 0)
AZUL = (0, 0, 255)
tela.fill(PRETO)
escreve_texto("Q09",tela,BRANCO,pygame.font.Font(None, 24))

def desenha_circulo(x,y):
    cor = AZUL
    pygame.draw.circle(tela, AZUL,(x,y),100)

terminou = False
while not terminou:
    x, y = largura_tela/2, altura_tela/2
    desenha_circulo(x,y)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

pygame.display.quit()
pygame.quit()



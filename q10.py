#Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um quadrado vermelho de 100 px de lado no centro da tela.
# O quadrado deve ser capaz de se movimentar vertical e horizontalmente através de teclas do computador. 
# Pode ser ‘a’,’s’,’d’,’w’ ou as setas do teclado. (código e printscreen)
import pygame
from pygame.locals import *
from escrever import escreve_texto

pygame.init()
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
BRANCO, PRETO = (255, 255, 255), (0, 0, 0)
VERMELHO, AZUL = (255, 0, 0), (0,0,255)
tela.fill(PRETO)
largura_quadrado,altura_quadrado = 100,100

class Teclas:
    def __init__(self, w,a,s,d):
        self.w = w
        self.a = a
        self.s = s
        self.d = d

x,y= largura_tela/2-largura_quadrado/2, altura_tela/2-altura_quadrado/2
teclas = Teclas(False, False, False, False)

def desenha_quadrado(x,y):
    cor = VERMELHO
    pygame.draw.rect(tela, cor, (x,y,largura_quadrado, altura_quadrado), 0)

def move_quadrado(teclas, x,y):
    if teclas.w and y > 0:
        y -= 1
    elif teclas.s and y < altura_tela-altura_quadrado:
        y += 1
    if teclas.a and x > 0:
        x -= 1
    elif teclas.d and x < largura_tela-largura_quadrado:
        x += 1
    return x,y

terminou = False
while not terminou:
    tela.fill(PRETO)
    escreve_texto("Q10",tela,BRANCO,pygame.font.Font(None, 24))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        # Enquanto estiver pressionado, o quadrado vai se mexer
        if event.type == pygame.KEYDOWN:
            if event.key == K_w or event.key == K_UP:
                teclas.w = True
            elif event.key == K_a or event.key == K_LEFT:
                teclas.a = True
            elif event.key == K_s or event.key == K_DOWN:
                teclas.s = True
            elif event.key == K_d or event.key == K_RIGHT:
                teclas.d = True    
        #No momento que parou de pressionar a tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                teclas.w = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                teclas.a = False
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                teclas.s = False
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                teclas.d = False
    x,y = move_quadrado(teclas,x,y)
    desenha_quadrado(x,y)
    pygame.display.update() 

pygame.display.quit()
pygame.quit()
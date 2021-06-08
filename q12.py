import pygame
from pygame.locals import *
from escrever import escreve_texto

pygame.init()
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
BRANCO, PRETO = (255, 255, 255), (0, 0, 0)
VERMELHO, AZUL, AMARELO = (255, 0, 0), (0,0,255),(255, 151, 26)
diametro_circulo = 100

def desenha_circulo(x,y):
    pygame.draw.circle(tela, AMARELO,(x,y),diametro_circulo)

class Teclas:
    def __init__(self, w,a,s,d):
        self.w = w
        self.a = a
        self.s = s
        self.d = d

x,y= largura_tela/2, altura_tela/2
teclas = Teclas(False, False, False, False)

def move_circulo(teclas, x,y):
    if teclas.w and y > diametro_circulo:
        y -= 1
    elif teclas.s and y < altura_tela-diametro_circulo:
        y += 1
    if teclas.a and x > diametro_circulo:
        x -= 1
    elif teclas.d and x < largura_tela-diametro_circulo:
        x += 1
        
    if x == diametro_circulo:
        x = largura_tela-diametro_circulo
    elif x == largura_tela-diametro_circulo:
        x = diametro_circulo  
    elif y == diametro_circulo:
        y = altura_tela-diametro_circulo
    elif y == altura_tela-diametro_circulo:
        y = diametro_circulo
            
        
    return x,y

terminou = False
while not terminou:
    tela.fill(PRETO)
    escreve_texto("Q12",tela,BRANCO,pygame.font.Font(None, 24))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        # Enquanto estiver pressionado, o coelho vai se mexer
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
    
    x,y = move_circulo(teclas,x,y)
    desenha_circulo(x,y)
    pygame.display.update() 

pygame.display.quit()
pygame.quit()
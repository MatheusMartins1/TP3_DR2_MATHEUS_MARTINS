#Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um quadrado vermelho de 100 px de lado no centro da tela.
# O quadrado deve ser capaz de se movimentar vertical e horizontalmente através de teclas do computador. 
# Pode ser ‘a’,’s’,’d’,’w’ ou as setas do teclado. (código e printscreen)
import pygame, sys
from pygame.locals import *
from time import sleep
# from escrever import escreve_texto

LARGURA_TELA, ALTURA_TELA = 800, 600
BRANCO, PRETO = (255, 255, 255), (0, 0, 0)
VERMELHO, AZUL = (255, 0, 0), (0,0,255)
LARGURA_LINHA = 10
PALETA_TAMANHO = 80
PALETA_OFFSET = 20
FPS = 200
velocidade = 1
placar = 0
terminou = False

pygame.mixer.init()  # Initialize the mixer module.
som_paleta = pygame.mixer.Sound("waterDroplet.mp3")
som_vitoria = pygame.mixer.Sound("nice.mp3")
som_derrota = pygame.mixer.Sound("ooh.mp3")
som_fim = pygame.mixer.Sound("fim.mp3")
# Função para desenhar o fundo
def desenhaArena(tela):
    tela.fill(PRETO)
    # Desenha a quadra
    pygame.draw.rect(tela, BRANCO, ((0,0), (LARGURA_TELA,ALTURA_TELA)), LARGURA_LINHA*2)
    # Desenha a linha no centro
    pygame.draw.line(tela, BRANCO, ((LARGURA_TELA//2),0), ((LARGURA_TELA//2),ALTURA_TELA), (LARGURA_LINHA//4))

def desenhaPaleta(tela,paleta):
    #Impede da paleta ir além da borda do fundo
    if paleta.bottom > ALTURA_TELA - LARGURA_LINHA:
        paleta.bottom = ALTURA_TELA - LARGURA_LINHA
    #Impede da paleta ir além da borda do topo
    elif paleta.top < LARGURA_LINHA:
        paleta.top = LARGURA_LINHA
    #Desenha a paleta
    pygame.draw.rect(tela, BRANCO, paleta)

#altera a direção da bola e retorna ela
def moveBola(bola, bolaDirX, bolaDirY):
    bola.x += bolaDirX * velocidade
    bola.y += bolaDirY * velocidade
    return bola

# Verifica por colisão com as bordas
# Retorna uma nova posição caso exista colisão
def verificaColisaoBorda(bola, bolaDirX, bolaDirY):
    if bola.top == (LARGURA_LINHA) or bola.bottom == (ALTURA_TELA - LARGURA_LINHA) or bola.top - velocidade <= LARGURA_LINHA or bola.bottom - velocidade >= (ALTURA_TELA - LARGURA_LINHA):
        bolaDirY = bolaDirY * -1
    if bola.left == (LARGURA_LINHA) or bola.right == (LARGURA_TELA - LARGURA_LINHA) or bola.left - velocidade <= LARGURA_LINHA or bola.right - velocidade >= (LARGURA_TELA - LARGURA_LINHA):
        bolaDirX = bolaDirX * -1
    return bolaDirX, bolaDirY

# Função para desenhar a bola
def desenhaBola(tela,bola):
    pygame.draw.rect(tela, BRANCO, bola)
    
def inteligenciaArtificial(bola, bolaDirX, paleta2):
# Movimentar a paleta quando a bola vem em direção da paleta
    if bolaDirX == 1:
        if paleta2.centery < bola.centery:
            paleta2.y += velocidade
        else:
            paleta2.y -= velocidade
    return paleta2

def aumenta_velocidade(placar):
    global velocidade
    if placar == 0:
        velocidade = 1
    elif placar % 2 == 0:
        velocidade += 1
    elif placar % 2 == 1:
        velocidade = velocidade

#Verifica a colisão da bola com a paleta1 ou paleta2    
def verificaColisaoBola(bola, paleta1, paleta2, bolaDirX):
    if bolaDirX == -1 and paleta1.right == bola.left and paleta1.top <= bola.top and paleta1.bottom >= bola.bottom:
        som_paleta.play()
        return -1
    elif bolaDirX == 1 and paleta2.left == bola.right and paleta2.top <= bola.top and paleta2.bottom >= bola.bottom:
        som_paleta.play()
        return -1
    else: 
        return 1

#Verifica se um jogador fez ponto e retorna o novo valor do placar
def verificaPlacar(paleta1, bola, placar, bolaDirX):
    global velocidade
    global terminou
    #zera a contagem se a bola acerta a borda do jogador
    if bola.left == LARGURA_LINHA or bola.left - velocidade == LARGURA_LINHA:
        som_derrota.play()
        velocidade = 1
        return 0
    elif bola.right == LARGURA_TELA - LARGURA_LINHA or bola.right - velocidade == LARGURA_TELA - LARGURA_LINHA:
        som_vitoria.play()
        sleep(0.8)
        placar += 2
        if placar >= 10:
            som_fim.play()
            sleep(5)
            terminou = True
            
        return placar
    elif bolaDirX == 1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
        placar += 1
        aumenta_velocidade(placar)
        return placar
    else: 
        return placar    
    
def desenhaPlacar(placar,tela,velocidade):
    resultadoSurf = BASICFONT.render(f"placar = {placar} | velocidade = x{velocidade}", True, BRANCO)
    resultadoRect = resultadoSurf.get_rect()
    resultadoRect.topleft = (LARGURA_TELA - 310, 25)
    tela.blit(resultadoSurf, resultadoRect)
    
def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('PongNet - Matheus Martins')
    
    ##Informação da fonte
    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 20
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    
    #altera a posição da bola
    bolaDirX = -1
    bolaDirY = -1
    
    bolaX = LARGURA_TELA//2 - LARGURA_LINHA//2
    bolaY = ALTURA_TELA//2 - LARGURA_LINHA//2
    jogador_um_posicao = (ALTURA_TELA - PALETA_TAMANHO) //2
    jogador_dois_posicao = (ALTURA_TELA - PALETA_TAMANHO) //2
    global placar
    
    #Criando os retangulos para a bola e paletas.
    paleta1 = pygame.Rect(PALETA_OFFSET,jogador_um_posicao,LARGURA_LINHA,PALETA_TAMANHO)
    paleta2 = pygame.Rect(LARGURA_TELA - PALETA_OFFSET - LARGURA_LINHA, jogador_dois_posicao, LARGURA_LINHA,PALETA_TAMANHO)
    bola = pygame.Rect(bolaX, bolaY, LARGURA_LINHA, LARGURA_LINHA)
    
    desenhaArena(tela)
    desenhaPaleta(tela,paleta1)
    desenhaPaleta(tela,paleta2)
    desenhaBola(tela,bola)
    
    global terminou
    while not terminou:
        tela.fill(PRETO)
        desenhaArena(tela)
        desenhaPaleta(tela,paleta1)
        desenhaPaleta(tela,paleta2)
        desenhaBola(tela,bola)
        bolaDirX, bolaDirY = verificaColisaoBorda(bola, bolaDirX, bolaDirY)
        bolaDirX = bolaDirX * verificaColisaoBola(bola, paleta1, paleta2, bolaDirX)
        placar = verificaPlacar(paleta1, bola, placar, bolaDirX)
        bola = moveBola(bola, bolaDirX, bolaDirY)
        paleta2 = inteligenciaArtificial (bola, bolaDirX, paleta2)
        
        desenhaPlacar(placar,tela,velocidade)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos
                paleta1.y = mouseY
        
        pygame.display.update() 
        FPSCLOCK.tick(FPS)

    pygame.display.quit()
    pygame.quit()

if __name__=='__main__':
    main()

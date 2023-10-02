import pygame
from raquete import Raquete
from bolinha import Bolinha

pygame.init()

#definindo tamanho da tela
larguraJanela = 800
alturaJanela  = 480
tamanhoTela   = (larguraJanela, alturaJanela)

tela          = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption("Pong Game")

direita  = 799
esquerda = 0
baixo    = 480
cima     = 0

#criando cores
CARMIN  = (144, 12, 63)
ROSA    = (234, 72, 72)
ROXO    = (149, 59, 140)

#definindo som de fundo
pygame.mixer.music.load("./assets/backgroundMusic.mp3")
#definindo imagem de fundo 
#convert alpha serve para deixar a imagem mais leve
fundoTela = pygame.image.load("./assets/backgroundImage.png").convert_alpha()

#colocando musica em loop
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

#          RAQUETES  
r1   = Raquete(ROXO, 20, 100, 780)

r2   = Raquete(ROXO, 20, 100, 0)

#          BOLINHA 
bola = Bolinha(CARMIN, 10, alturaJanela, larguraJanela)



#criando variavel movimento
keys  = []
clock =  pygame.time.Clock()

#          SCORE
scoreA = 0
scoreB = 0


#     METODO RESETAR 
def resetar () :
    r1.y = r2.y = 150
    bola.x = 400    
    bola.y = 300

while True:
    for event in pygame.event.get(): # que tipo de acao o usuario fez
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] :
        r1.moverParaBaixo()
    if keys[pygame.K_UP] :
        r1.moverParaCima()
    if keys[pygame.K_w] :
        r2.moverParaCima()
    if keys[pygame.K_s] :
        r2.moverParaBaixo()
    

    #preenchendo tela de fundo
    tela.blit(fundoTela, (0,0))


        #    VARIÁVEIS DO SCORE 
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, CARMIN)
    tela.blit(text, (200,10))
    text = font.render(str(scoreB), 1, CARMIN)
    tela.blit(text, (600,10))

    pygame.draw.rect(tela, r1.color, (r1.x, r1.y, r1.width, r1.height))
    pygame.draw.rect(tela, r2.color, (r2.x, r2.y, r2.width, r2.height))

    #primeiro ele atualiza as variaveis e dps ele insere oq foi atualizado

    #MOVIMENTANDO A BOLA
    bola.colisao(r1, r2)
    bola.mover()

    if bola.x <= 0 :
       scoreB += 1
       resetar()
    if bola.x >= 800:
       scoreA += 1
       resetar()
    #desenhando a bolinha, de acordo com os parametros
    pygame.draw.circle(tela, bola.color, (bola.x, bola.y), bola.radium)
    print(bola.x, bola.y)

    pygame.display.update()



    #ajustando tamanho do retangulo
    tela.fill((0, 0, 0))
    #controla o delay do jogo 
    clock.tick(1000)
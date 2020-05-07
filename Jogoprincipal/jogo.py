import pygame
from random import randint
pygame.init()

# Musica
pygame.mixer.music.load('Music1.mp3')
pygame.mixer.music.play(-1)

# Posição
x = 380
y = 500
pos_x = 250   # Objeto da Esquerda / Horizontal
pos_y = 1200   # Objeto do Esquerda / Vertical
pos_y_a = 300
pos_y_c = 500

# Tempo
timer = 0
tempo_segundo = 0

# Velocidade
velocidade = 11
velocidade_obs = 20

# Imagens
fundo = pygame.image.load("Fundo.jpg")
pers = pygame.image.load("pers.png")
teste1 = pygame.image.load('obstac1.png')
teste2 = pygame.image.load('obstac2.png')
teste3 = pygame.image.load('obstac3.png')

# Fonte e Texto
font = pygame.font.SysFont('Bauhaus 93',30)
texto = font.render('Game Time :', True, (255,255,255),(67,84,90))
pos_texto = texto.get_rect()
pos_texto.center = (85,50)

# Janela
janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Criando jogo com Python")

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

# Comados
    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_LEFT] and x>= 200 :
        x -= velocidade
    if comandos[pygame.K_RIGHT] and x<= 580:
        x += velocidade

# Colisão
    if ((x + 20 > pos_x and y + 43 > pos_y)): # colisão lado direito
        y = 500

    if ((x - 20 < pos_x - 300 and y + 43 < pos_y_a)):  # colisão lado esquerdo
        y = 500

    if ((x + 20 > pos_x - 136 and y + 43 < pos_y_c)) and ((x - 20 < pos_x -136 and y + 43 > pos_y_c)): # colisão Central
        y = 500

# Movimento Tela
    if (pos_y <= -80) :
        pos_y = randint (800,1000)

    if (pos_y_a <= -80) :           #pos_y_a = posição em y da obs 1
        pos_y_a = randint (1300, 2000)

    if (pos_y_c <= -80):
        pos_y_c = randint (2300, 3000)

# Tempo Tela
    if (timer <20):
        timer +=1
    else:
        tempo_segundo +=1
        texto = font.render('Game Time :'+ str (tempo_segundo), True, (255, 255, 255), (67, 84, 90))
        timer = 0

# Aumento de Velocidade na Tela
    pos_y -= velocidade_obs
    pos_y_a -= velocidade_obs +2
    pos_y_c -= velocidade_obs +10



    janela.blit (fundo, (0,0))
    janela.blit (pers, (x,y))
    janela.blit (teste1, (pos_x,pos_y))
    janela.blit (teste2,(pos_x + 150,pos_y_a))
    janela.blit (teste3,(pos_x + 300,pos_y_c))
    janela.blit (texto,pos_texto)

    pygame.display.update()
pygame.quit()
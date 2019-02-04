#imports
import sys
import pygame as pg
import sprites as sp
from configuracoes import *

pg.init()#inicia modulos do pygame

#cria heroi inimigos e plataformas
h = sp.Heroi(10,10)
terra1 = sp.Terra("mainplat.png", 0, 360)
terra2 = sp.Terra("plat2.png", 200, 270)
terra3 = sp.Terra("plat2.png", 20, 200)
terra4 = sp.Terra("plat2.png", 210, 120)
inimigo1 = sp.Inimigo(100,30,1)
inimigo2 = sp.Inimigo(210,30,2)
inimigo3 = sp.Inimigo(320,30,3)

#grupo do heroi
heroi = pg.sprite.GroupSingle()
heroi.add(h)

#grupo de terrenos
plataformas = pg.sprite.Group()
plataformas.add(terra1)
plataformas.add(terra2)
plataformas.add(terra3)
plataformas.add(terra4)

#grupo de inimigos
inimigos = pg.sprite.Group()
inimigos.add(inimigo1)
inimigos.add(inimigo2)
inimigos.add(inimigo3)

relogio = pg.time.Clock()#relogio para FPS

#fonte
pg.font.init()
fontePadrao = pg.font.get_default_font()
fonte = pg.font.SysFont(fontePadrao,30)

fundo = pg.image.load("fundo.png")#fundo da fase

#config da tela
screen = pg.display.set_mode(tamanho)
pg.display.set_caption(titulo)

Jogando = True

while Jogando:
    #_EVENTOS_#
    for event in pg.event.get():
        if event.type == pg.QUIT: Jogando=False

        #verifica as teclas para acoes
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT: h.irDireita()
            if event.key == pg.K_LEFT: h.irEsquerda()
            if event.key == pg.K_UP: h.pular()
            if event.key == pg.K_DOWN: h.descer()
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT: h.pararDireita()
            if event.key == pg.K_LEFT: h.pararEsquerda()
            if event.key == pg.K_DOWN: h.pararDescer()

    h.update()

    #grava aonde heroi estava
    xAnterior = h.rect.x
    yAnterior = h.rect.bottom

    #realoca para verificacao
    h.rect.y+=h.velY
    h.rect.x+=h.velX
    
    objetoColidido=pg.sprite.spritecollide(h, plataformas, False)#verifica colisao
    
    #testes de colisao
    h.noChao=False
    if objetoColidido:
        menorObj=objetoColidido[0]
        for obj in objetoColidido:
            if obj.rect.y > menorObj.rect.y: menorObj = obj
        if not(h.descendo) and yAnterior <= menorObj.rect.top:
            h.rect.bottom=menorObj.rect.top
            h.noChao = True
    if h.rect.bottom > 360: h.rect.bottom = 360
    if h.rect.left < 0: h.rect.left = 0
    if h.rect.right > 600: h.rect.right = 600

    #_DESENHO_#
    screen.fill(black)
    screen.blit(fundo,(0,0))
    plataformas.draw(screen)
    heroi.draw(screen)
    inimigos.draw(screen)
    textoFps = fonte.render(str(int(relogio.get_fps())),True,white)
    screen.blit(textoFps,(10,10))
    pg.display.flip()
    relogio.tick(60)

sys.exit(0)#sai do jogo

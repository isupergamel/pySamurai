import sys
import pygame as pg
import sprites as sp
from configuracoes import *

pg.init()#inicia modulos do pygame

h = sp.Heroi(red,100,30)
terra1 = sp.Terra(red,300,30,20,300)
terra2 = sp.Terra(red,300,30,200,150)

heroi = pg.sprite.GroupSingle()
heroi.add(h)

chaos = pg.sprite.Group()

chaos.add(terra1)
chaos.add(terra2)

relogio = pg.time.Clock()

pg.font.init()
fontePadrao = pg.font.get_default_font()
fonte = pg.font.SysFont(fontePadrao,30)

fundo = pg.image.load("fundo.png")

screen = pg.display.set_mode(tamanho)
pg.display.set_caption(titulo)

Jogando = True

while Jogando:
    #_EVENTOS_#
    for event in pg.event.get():
        if event.type == pg.QUIT: Jogando=False

        #verifica as teclas para acoes
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT: h.direita=True
            if event.key == pg.K_LEFT: h.esquerda=True
            if event.key == pg.K_UP: h.pulando=True
            if event.key == pg.K_DOWN : h.descendo=True
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT: h.direita=False
            if event.key == pg.K_LEFT: h.esquerda=False

    #_PROCESSOS_#
    #acoes da gravidade e velocidade
    h.velX=0
    if h.esquerda: h.velX+=-4
    if h.direita: h.velX+=4
    if h.pulando: 
        h.velY=-15
        h.pulando=False
    
    if h.velY<gravidade:#gravidade, com no maximo ate n de velocidade
        h.velY+=1
    
    #grava aonde heroi esta e coloca o heroi aonde deve estar
    xAnterior = h.rect.x
    yAnterior = h.rect.bottom #em vez do y pego o bottom
    print(yAnterior)

    h.rect.y+=h.velY
    h.rect.x+=h.velX
    
    objetoColidido=pg.sprite.spritecollideany(h,chaos)
    
    #testes de colisao
    if objetoColidido:#se tem um objeto colidido
        if not(h.descendo) and yAnterior <= objetoColidido.rect.top:
            h.rect.bottom=objetoColidido.rect.top
    if not(objetoColidido): h.descendo=False

    #_DESENHO_#
    screen.fill(black)
    screen.blit(fundo,(0,0))
    heroi.draw(screen)
    chaos.draw(screen)
    textoFps = fonte.render("60",True,white)
    screen.blit(textoFps,(10,10))
    pg.display.flip()
    relogio.tick(60)

sys.exit(0)

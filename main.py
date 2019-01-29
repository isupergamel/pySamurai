import sys
import pygame as pg
import sprites as sp
from configuracoes import *

pg.init()#inicia modulos do pygame

h = sp.Heroi(red,100,30)
terra1 = sp.Terra(blue,300,30,20,200)
terra2 = sp.Terra(blue,300,30,100,150)

heroi = pg.sprite.GroupSingle()
heroi.add(h)

chaos = pg.sprite.Group()

chaos.add(terra1)
chaos.add(terra2)

relogio = pg.time.Clock()

screen = pg.display.set_mode(tamanho)
pg.display.set_caption(titulo)

Jogando = True

while Jogando:
    #_EVENTOS_#
    for event in pg.event.get():
        if event.type == pg.QUIT: Jogando=False

        if event.type == pg.KEYDOWN:#verifica as teclas para acoes
            if event.key == pg.K_RIGHT: h.direita=True
            if event.key == pg.K_LEFT: h.esquerda=True
            if event.key == pg.K_UP: h.pulando=True
            if event.key == pg.K_DOWN : h.descendo=True
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT: h.direita=False
            if event.key == pg.K_LEFT: h.esquerda=False
            #if event.key == pg.K_UP:
            #    pass#h.velY=-20

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
    
    #coloca o heroi aonde deve estar
    h.rect.y+=h.velY
    h.rect.x+=h.velX
    
    colid=pg.sprite.spritecollideany(h,chaos)#sprite q colidiu com heroi
    
    if colid and not(h.descendo): h.rect.bottom=colid.rect.top
    if not(colid): h.descendo=False

    #_DESENHO_#
    screen.fill(white)
    heroi.draw(screen)
    chaos.draw(screen)
    pg.display.flip()
    relogio.tick(60)

sys.exit(0)

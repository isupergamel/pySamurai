import pygame as pg
from configuracoes import *

class Heroi(pg.sprite.Sprite):

    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("heroi.png")
        self.rect = self.image.get_rect()
        self.velX = (0)
        self.velY = (0)
        self.rect.x = x
        self.rect.y = y
        self.esquerda = False
        self.direita = False
        self.pulando = False
        self.descendo = False
        self.relogioD = pg.time.Clock()
        self.relogioE = pg.time.Clock()
        self.dashD = False
        self.dashE = False
        self.noChao = False

    #acoes de teclas
    def irEsquerda(self): 
        self.image = pg.image.load("heroiE.png")
        self.esquerda = True
        self.relogioE.tick()
        if self.relogioE.get_time() < 200: self.dashE = True

    def irDireita(self):
        self.image = pg.image.load("heroi.png")
        self.direita = True
        self.relogioD.tick()
        if self.relogioD.get_time() < 200: self.dashD = True
    
    def descer(self):
        self.descendo = True
    
    def pular(self):
        if self.noChao: self.pulando = True
    
    def pararEsquerda(self):
        self.esquerda = False
        self.dashE = False
    
    def pararDireita(self):
        self.direita = False
        self.dashD = False
    
    def pararDescer(self):
        self.descendo = False

    def update(self):
        #ajusta velocidade
        self.velX=0
        if self.esquerda:
            self.velX -= 5
            if self.dashE: self.velX -= 5
        if self.direita:
            self.velX += 5
            if self.dashD: self.velX += 5
        if self.pulando: 
            self.velY = -15
            self.pulando = False
        if self.velY<gravidade: self.velY += 1#velocidade do Y no maximo da gravidade

class Terra(pg.sprite.Sprite):
    def __init__(self, imagem, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(imagem)
        self.rect = self.image.get_rect()
        #self.rect.height -= (self.rect.height-1)
        self.rect.x=x
        self.rect.y=y

class Inimigo(pg.sprite.Sprite):
    def __init__(self,x,y,tipo):
        pg.sprite.Sprite.__init__(self)
        if tipo==1: self.image=pg.image.load("normal.png")
        if tipo==2: self.image=pg.image.load("subchefe.png")
        if tipo==3: self.image=pg.image.load("boss.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.esquerda=False
        self.direita=False
        self.pulando=False

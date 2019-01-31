import pygame as pg
from configuracoes import *

class Heroi(pg.sprite.Sprite):
    def __init__(self,color,width,height):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.image.load("heroi.png")
        self.rect = self.image.get_rect()
        self.velX=(0)
        self.velY=(0)
        self.esquerda=False
        self.direita=False
        self.pulando=False
        self.descendo=False

class Terra(pg.sprite.Sprite):
    def __init__(self,color,width,height,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.height -= (self.rect.height-1)
        print(self.rect.height)
        self.rect.x=x
        self.rect.y=y

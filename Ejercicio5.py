import pygame
from chessPictures import *
from interpreter import draw
pygame.init()
fila = Picture(None)
null = Picture("")
casilleroblanco = Picture(SQUARE)
casilleronegro = Picture(SQUARE).negative()
for x in range(0,4):
    if(x < 1):
        null = null.up(casilleroblanco.join(casilleronegro).negative())
    if(x >= 1):
        null = null.join(casilleroblanco.join(casilleronegro).negative())
draw(null) 
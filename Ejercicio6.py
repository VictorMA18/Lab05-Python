import pygame
from chessPictures import *
from interpreter import draw
pygame.init()
null = Picture("")
casilleroblanco = Picture(SQUARE)
casilleronegro = Picture(SQUARE).negative()
for x in range(0,4):
    if(x < 1):
        null = null.up(casilleroblanco.join(casilleronegro))
    if(x >= 1):
        null = null.join(casilleroblanco.join(casilleronegro))
for i in range(0,2):
    if(i % 2 == 0):
        null = null.up(null.negative())
    else:
        null = null.up(null)
draw(null)
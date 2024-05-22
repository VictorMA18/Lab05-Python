import pygame
from chessPictures import *
from interpreter import draw
pygame.init()
iteraciones = [1,2]
caballoblanco = Picture(KNIGHT)
caballonegro = Picture(KNIGHT).negative()
for x in range(len(iteraciones)):
    if(x % 2 == 0):
        caballoblanco = caballoblanco.join(caballonegro)
    else:
        caballoblanco = caballoblanco.under(caballoblanco.verticalMirror())
draw(caballoblanco) 
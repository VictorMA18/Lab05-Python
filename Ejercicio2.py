import pygame
from chessPictures import *
from interpreter import draw
pygame.init()
iteraciones = [1,2]
null = Picture("")
caballoblanco = Picture(KNIGHT)
caballonegro = Picture(KNIGHT).negative()
for x in range(len(iteraciones)):
    if(x % 2 == 0):
        null = null.up((caballoblanco.join(caballonegro)).verticalMirror())
    else:
        null = null.up(caballoblanco.join(caballonegro))
draw(null)
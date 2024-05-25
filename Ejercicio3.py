import pygame
from chessPictures import *
from interpreter import draw
pygame.init()
reynablanca = Picture(QUEEN)
null = Picture("")
for x in range(0,5):
    if(x < 1):
        null = null.up(reynablanca)
    if(x > 1):
        null = null.join(reynablanca)
draw(null)
import pygame
from chessPictures import *
from interpreter import draw
pygame.init()
iteraciones = [1,2,3,4,5,6,7]
casilleroblanco = Picture(SQUARE)
casilleronegro = Picture(SQUARE).negative()
casilleroblanco = (casilleroblanco.join(casilleronegro).negative()).horizontalRepeat(4)
draw(casilleroblanco) 
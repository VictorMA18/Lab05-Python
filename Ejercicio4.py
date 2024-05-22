import pygame
from chessPictures import *
from interpreter import draw
pygame.init()
iteraciones = [1,2,3,4,5,6,7]
fila = Picture(None)
casilleroblanco = Picture(SQUARE)
casilleronegro = Picture(SQUARE).negative()
fila = (casilleroblanco.join(casilleronegro)).horizontalRepeat(4)
draw(fila) 
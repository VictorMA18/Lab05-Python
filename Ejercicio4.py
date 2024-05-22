import pygame
from chessPictures import *
from interpreter import draw
pygame.init()
fila = Picture(None)
casilleroblanco = Picture(SQUARE)
casilleronegro = Picture(SQUARE).negative()
fila = (casilleroblanco.join(casilleronegro)).horizontalRepeat(4)
draw(fila) 
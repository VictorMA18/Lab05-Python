import pygame
from chessPictures import *
from interpreter import draw
pygame.init()
casilleroblanco = Picture(SQUARE)
casilleronegro = Picture(SQUARE).negative()
casilleroblanco = (casilleroblanco.join(casilleronegro).negative()).horizontalRepeat(4)
draw(casilleroblanco) 
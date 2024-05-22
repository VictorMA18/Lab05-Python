import pygame
from chessPictures import *
from interpreter import draw
pygame.init()
iteraciones = [1,2,3,4]
casilleroblanco = Picture(SQUARE)
casilleronegro = Picture(SQUARE).negative()
filag = Picture(None)
filan = Picture(None)
filag = (casilleroblanco.join(casilleronegro)).horizontalRepeat(4)
filan = (casilleroblanco.join(casilleronegro).negative()).horizontalRepeat(4)
draw(filag.under(filan).verticalRepeat(2)) 
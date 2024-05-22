import pygame
from chessPictures import *
from interpreter import draw
pygame.init()
iteraciones = [1,2]
reynablanca = Picture(QUEEN)
reynablanca = reynablanca.horizontalRepeat(4)
draw(reynablanca)
import pygame
from chessPictures import *
from interpreter import draw
from picture import *
pygame.init()
caballo = Picture(KNIGHT)
cawhite = Picture(SQUARE)

draw(caballo.rotate().rotate().rotate().join(caballo.negative()))

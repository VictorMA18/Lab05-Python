import pygame
from chessPictures import *
from interpreter import draw
from picture import *
pygame.init()
caballo = Picture(KNIGHT)

draw(caballo.negative())

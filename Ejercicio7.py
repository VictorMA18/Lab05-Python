import pygame
from chessPictures import *
from interpreter import draw
pygame.init()

#OBJETOS NULOS
tablabase = Picture("")
board = Picture("")

#FILAS NECESARIAS
white_pawns = pawn.horizontalRepeat(8).up(square.join(square.negative()).horizontalRepeat(4))
black_pawns = pawn.negative().horizontalRepeat(8).up(square.join(square.negative()).horizontalRepeat(4).negative())
white_back_rank = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock).up(square.join(square.negative()).negative().horizontalRepeat(4))
black_back_rank = white_back_rank.negative().up(square.join(square.negative()).horizontalRepeat(4))
tablabase = ((square.join(square.negative()).horizontalRepeat(4)).under(square.join(square.negative()).negative().horizontalRepeat(4))).verticalRepeat(2)

#BOARD 
board = black_back_rank.under(board)
board = board.under(black_pawns)
board = board.under(tablabase)
board = board.under(white_pawns)
board = board.under(white_back_rank)

draw(board)
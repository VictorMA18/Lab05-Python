import pygame
from chessPictures import *
from interpreter import draw
pygame.init()

#OBJETOS NULOS
tablabase = Picture("")
board = Picture("")

#FILAS NECESARIAS
white_pawns = square.join(square.negative()).horizontalRepeat(4).up(pawn.horizontalRepeat(8))
black_pawns = square.join(square.negative()).horizontalRepeat(4).negative().up(pawn.negative().horizontalRepeat(8))
white_back_rank = square.join(square.negative()).negative().horizontalRepeat(4).up(rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock))
black_back_rank = (square.join(square.negative()).horizontalRepeat(4)).up(white_back_rank.negative())
tablabase = ((square.join(square.negative()).horizontalRepeat(4)).under(square.join(square.negative()).negative().horizontalRepeat(4))).verticalRepeat(2)

#BOARD 
board = black_back_rank.under(board)
board = board.under(black_pawns)
board = board.under(tablabase)
board = board.under(white_pawns)
board = board.under(white_back_rank)

draw(board)
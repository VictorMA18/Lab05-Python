import pygame
from chessPictures import *
from interpreter import draw
pygame.init()

tablabase = Picture("")
board = Picture("")

white_pawns = pawn.horizontalRepeat(8).up(square.join(square.negative()).horizontalRepeat(4))
black_pawns = pawn.negative().horizontalRepeat(8).up(square.join(square.negative()).horizontalRepeat(4).negative())

white_back_rank = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock).up(square.join(square.negative()).negative().horizontalRepeat(4))

black_back_rank = white_back_rank.negative().up(square.join(square.negative()).horizontalRepeat(4))

# Unión de filas para crear el tablero completo
board = black_back_rank.under(board)
tablabase = (square.join(square.negative()).horizontalRepeat(4)).under(square.join(square.negative()).negative().horizontalRepeat(4))
board = board.under(black_pawns)
board = board.under(tablabase.verticalRepeat(2))
board = board.under(white_pawns)
board = board.under(white_back_rank)

draw(board)
import pygame
from chessPictures import *
from interpreter import draw
pygame.init()

#OBJETOS NULOS
tabla_total = Picture("")
tabla_base = Picture("")
mitad_tabla = Picture("")
pawns = Picture("")
tabla_base_piezas = Picture("")


#MAIN
Fila_piezas = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock)

for x in range(0,9):
    if(x < 1):
        pawns = pawns.up(pawn)
    if(x > 1):
        pawns = pawns.join(pawn)


for x in range(0,4):
    if(x < 1):
        tabla_base = tabla_base.up(square.negative().join(square))
    if(x >= 1):
        tabla_base = tabla_base.join(square.negative().join(square))
for i in range(0,1):
    if(i % 2 == 0):
        tabla_base = tabla_base.up(tabla_base.negative())
    else:
        tabla_base = tabla_base.up(tabla_base)

tabla_base_piezas_arriba = tabla_base.under(pawns.negative().up(Fila_piezas.negative()))
tabla_base_piezas_abajo = tabla_base.under(Fila_piezas.up(pawns))

for x in range(0,4):
    if(x < 1):
        mitad_tabla = mitad_tabla.up(square.negative().join(square))
    if(x >= 1):
        mitad_tabla = mitad_tabla.join(square.negative().join(square))
for i in range(0,2):
    if(i % 2 == 0):
        mitad_tabla = mitad_tabla.up(mitad_tabla.negative())
    else:
        mitad_tabla = mitad_tabla.up(mitad_tabla)
        
#BOARD 
tabla_total = tabla_total.up(tabla_base_piezas_abajo)
tabla_total = tabla_total.up(mitad_tabla)
tabla_total = tabla_total.up(tabla_base_piezas_arriba)
draw(tabla_total)


'''
Se requiere un Script en python que permita simular el juego de carrera numérica con dos players.
La carrera inicia en la posición CERO y finaliza en la posición 100.
El juego se realiza por default con 2 jugadores.
EL juego que llegue primero a la meta (Posición 100 será el ganador)
Si un jugador genera 3 pares consecutivos en el lanzamiento de los dados será directamente ganador.
Repite tiro si y sólo si saca PAR. 
'''

#randint => Genera valores numéricos enteros [Z] (+,-)
#uniform => Genera valores numéricos reales [R] (+,-)

import os

from random import randint, uniform

os.system("clear")

dice1 = randint(1,6)
dice2 = randint(1,6)

print("Dice 1: ", dice1)
print("Dice 2: ", dice2)
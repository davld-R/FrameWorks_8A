'''
Developer: David Rojas
RETO:
    Requerimiento del Script:

    -> Un solo jugador lanza los dados
    -> Debe recorrer de cero (0) a cien posiciones (100)
    -> El juego termina cuando:
        - Cuando el jugador obtenga dos pares consecutivos
        - Cuando llegue a la meta (+100)
'''
from random import randint

#Functions
def dices() :
    status = True
    c=0

    while status :    
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        a = dice1 + dice2
        c = c + a
        print("D1: ", dice1)
        print("D2: ", dice2)

        if dice1 == dice2 :    
                   
            dice3 = randint(1,5)
            dice4 = randint(1,5)
            print("D1: ", dice3)
            print("D2: ", dice4)
            
            if dice3 == dice4 :
                status = False       
                print("::: WIN por dos números pares :::")
            else :
                print("No has acertado en los pares, intenta de nuevo")
            
        elif c > 100 : 
            status = False
            print("::: WIN por sacar más de > 100 puntos ::: ", c)
        
        else :  
            key = input(".:: Presiona cualquier tecla para lanzar los dados nuevamente ...")

#Main
dices()


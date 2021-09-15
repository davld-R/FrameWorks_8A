'''
Developer: David
Date: 15 sep 2021
Description: Script Python que permite identificar el mayor de dos nùmeros ingresados por consola
'''

import os

os.system("clear")

print("Ingrese primer nùmero: ")
n1 = int(input())
n2 = int(input("Ingrese segundo nùmero: "))

if n1 > n2:
    print("El mayor es: ", n1)
elif n1 < n2:
    print("El mayor es: ", n2)
else :
    print("::: Los números son iguales :::")


# print("a: ", type(n1))
# suma = n1 + n2
# print("La suma es: ", suma)

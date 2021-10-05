#Developer: Skipper
#Date: 17 - Sept- 2021
'''
    Script Description:
    Cree un mini juego en Python que permita a un solo jugador lanzar dos dados en varias 
    oportunidades, y finalice el juego cuando obtenga un par de UNOS [D1:1-D2:2]

'''
#IMPORTAMOS LAS LIBREARIAS DE OS, LA FUNCION RANDINT, UNIFORM, RANDOM
import os
from random import randint #uniform, random

#VARIABLES:
print("::: JUEGO CARRERA NUMERICA :::")
status = True #variable de tipo Boolena

#OPERACION: (BUCLE)
while status: #while status sea == True
    key = input(":::Presiona cualquier tecla para lanzar los dados...")
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    print("Dice 1: ", dice1)
    print("Dice 2: ", dice2)
 
    if dice1 == 1 and dice2 == 1 :
        status = False 
        print("::: Sacaste par de unos, el juego a terminado :::")
        key = input(":::Presiona cualquier tecla para salir...")







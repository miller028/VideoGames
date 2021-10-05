#Date: 20 - Sept - 2021
'''
Description:
este es nuestro primer script python con Python.
Este script genera una ventana en pygame con el titulo "¡Hello world!"
'''
#Importamos librerias ((Inicio):
import pygame
import sys
#Importamos librerias (Fin):

#Inicializar Pygame:
pygame.init()

#Dimenzionar el tamaño (w x h) de la ventana del juego 
width = 800
height = 500
windows = pygame.display.set_mode((width, height))
pygame.display.set_caption("¡Hello world!")

#Metodo para mantener visible la ventana abierta
while True:
    for event in pygame.event.get():#mientras no presione un evento de cierrar, se mantendra abierta
        if event.type == pygame.QUIT : #si preciona x en la ventana sale
            pygame.QUIT #cierra la ventana
            sys.exit()#cierra o destruye todos los procesos 



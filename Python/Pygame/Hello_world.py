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
mywindows = pygame.display.set_mode((width, height))
pygame.display.set_caption("¡Hello world!")#Para poner nombre a la ventana
icon = pygame.image.load('images/cohete.png')#Cargar imagen
pygame.display.set_icon(icon)#setear imagen

'''
   RGB:
   Colores Red, Green, Blue de fondo, trabajados en Hexadecimal que desde
   0 hasta 255
'''
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
x = pygame.Color(210, 180, 140)
y = pygame.Color(70, 130, 180)

#Poner figura (rectangulo, circulo, cuadrado, etc)
rect1 = pygame.Rect(150, 300, 150, 50) #Rectangulo en x, y, w, h
rect2 = pygame.Rect(350, 230, 150, 50) #Rectangulo en x, y, w, h
print(rect2,x)
print(rect2,y)

rect1.center = (width // 2, height // 2)#Punto medio de la ventana 

#Metodo para mantener visible la ventana abierta
while True:
    for event in pygame.event.get():#mientras no presione un evento de cierrar, se mantendra abierta
        if event.type == pygame.QUIT : #si preciona x en la ventana sale
            pygame.QUIT #cierra la ventana
            sys.exit()#cierra o destruye todos los procesos 
    mywindows.fill(y) #color de dondo de ventana  
    pygame.draw.rect(mywindows, red, rect1)#Para dibujar se nesecita el contexto, color, rectangulo
    pygame.draw.rect(mywindows, blue, rect2)
    
    pygame.draw.rect(mywindows, green, (50, 50, 50, 50)) 
    pygame.draw.line(mywindows, red, (10,10), (300,10),5)
    pygame.draw.circle(mywindows, x, (400,200), 100)
    pygame.draw.polygon(mywindows, blue, ((0,300), (100,200), (200,300)))
    pygame.display.update() #para actualizarse




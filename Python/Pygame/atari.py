'''
    Developer: Miller Salas
    Date: 5 - Oct - 2021
    Description:
    Desarrollo de la versión 1.0 de un video juego de atari.
'''

#Importamos librerias ((Inicio):
import sys
import pygame
#Importamos librerias (Fin):

#Inicializar Pygame:
pygame.init()

#Inicia Classe 1 bolita:
class Ball(pygame.sprite.Sprite):#sprite forma de tratar las imagenes
    def __init__(self):#selt es el contexto 
        pygame.sprite.Sprite.__init__(self)#cargamos la imagen como sprite en el contexto
        self.img_ball = pygame.image.load('images/bolita.png')#cargamos la imagen.png
        self.rect = self.img_ball.get_rect()#permite obtener el rectangulo de la imagen
        self.rect.centerx = WIDTH / 2 #Centra el ancho
        self.rect.centery = HEIGHT / 2 #Centra el alto
        self.speed = [5, 5] #Velocidad del movimiento de la bolita con rspecto al marco 
    
    def pibot(self):#hacer rebotar una bolita 
        #Validar el eje Y ↓↑
        if self.rect.bottom >= HEIGHT or self.rect.top <=0:#tottom es por abajo y top por arriba
            self.speed[1] = -self.speed[1]#rebota en base al eje Y
        #Validar X ← X →
        elif self.rect.right >= WIDTH or self.rect.left <=0:
            self.speed[0] = -self.speed[0]#rebota en base al eje x

        self.rect.move_ip(self.speed) 
#Fin de Classe 1 bolita


#Inicia Classe 2:
class Bar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_bar = pygame.image.load('images/paleta.png')
        self.rect = self.img_bar.get_rect()
        self.rect.midbottom = (WIDTH / 2, HEIGHT - 10)
        self.speed = [0, 0]

    def slide(self, listener):
        if listener.key == pygame.K_LEFT and self.rect.left > 0 :
            self.speed = [-5, 0]
        elif listener.key == pygame.K_RIGHT and self.rect.right < WIDTH :
            self.speed = [5, 0]
        else :
            self.speed = [0, 0]     

        self.rect.move_ip(self.speed)
####################################################################################
class Brick(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/ladrillo.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class Wall(pygame.sprite.Group):
    def __init__(self, totalBricks):
        pygame.sprite.Group.__init__(self)
        posX = 0
        posY = 10

        for i in range(totalBricks):
            brick = Brick(( posX, posY ))
            self.add(brick)

            posX += brick.rect.width
            if posX >= WIDTH :
                posX = 0
                posY += brick.rect.height
    
####################################################################################

#Dimenzionar el tamaño (w x h) de la ventana del juego 
WIDTH = 640
HEIGHT = 480

#Configure full-mywindows
#WIDTH = ?
#HEIGHT = ?

mywindows = pygame.display.set_mode((WIDTH,  HEIGHT))
pygame.display.set_caption('Atari')#Para poner nombre a la ventana
icon = pygame.image.load('images/main_icon.png')#Cargar imagen
pygame.display.set_icon(icon)#setear imagen
game_clock = pygame.time.Clock()#
pygame.key.set_repeat(20)

'''
   RGB:
   Colores Red, Green, Blue de fondo, trabajados en Hexadecimal que desde
   0 hasta 255
'''
BG_COLOR = (0, 191, 255) # (Red, Green, Blue)

ball = Ball()#se llama la instancia de la clase bolita (Ball) y nombra una variable(ball)
player = Bar()
wall = Wall(112)

#Loop (Revisión cíclica de los eventos) => Listener esta pendiente del acontecimiento
while True:
    game_clock.tick(60)#frame por segundo
    for event in pygame.event.get():#mientras no presione un evento de cierrar, se mantendra abierta
        if event.type == pygame.QUIT:#si preciona x en la ventana sale
            pygame.quit()#cierra la ventana
            sys.exit()#cierra o destruye todos los procesos 
        elif event.type == pygame.KEYDOWN : #Verificar si el jugador presionó tecla del teclado
            player.slide(event)

    ball.pibot() #Call pibot de la clase 1:     
    mywindows.fill(BG_COLOR)#color de dondo de ventana       
    #Draw de la ball
    mywindows.blit(ball.img_ball, ball.rect)
    #Draw de la bar
    mywindows.blit(player.img_bar, player.rect)
    #Dibujar muro
    wall.draw(mywindows)       
    pygame.display.flip()#Refresh de elementos en mywindows
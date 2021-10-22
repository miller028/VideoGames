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
    
    def pibot(self):#metodo o accion para hacer rebotar una bolita 
        #Validar el eje Y ↓↑
        if self.rect.bottom >= HEIGHT or self.rect.top <=0:#tottom es por abajo y top por arriba
            self.speed[1] = -self.speed[1]#rebota en base al eje Y
        #Validar X ← X →
        elif self.rect.right >= WIDTH or self.rect.left <=0:
            self.speed[0] = -self.speed[0]#rebota en base al eje x

        self.rect.move_ip(self.speed) 
    
    #def saludos(self):#metodo interno
       # print("::::Este es un saludo de prueba ::::")

#Fin de Classe 1 bolita

#Inicia Classe barra que realiza el recorrido de izquierda a derecha:
class Bar(pygame.sprite.Sprite):#
    def __init__(self):#selt es el contexto
        pygame.sprite.Sprite.__init__(self)#cargamos la imagen como sprite en el contexto
        self.img_bar = pygame.image.load('images/paleta.png')#cargamos la imagen.png
        self.rect = self.img_bar.get_rect()#permite obtener el rectangulo de la imagen
        self.rect.midbottom = (WIDTH / 2, HEIGHT - 10)#centramos el objeto en X con midbottom (480 restele -10)
        self.speed = [0, 0]#Velocidad del movimiento de la barra que hace de izquierda a derecha

    def slide(self, listener):#metodo o accion para hacer que se mueva de izquierda a derecha la barrita
                              #listener detecta si fue presionado o no 
        if listener.key == pygame.K_LEFT and self.rect.left > 0 :#para saber si el usuario preciono la tecla izquierda
            self.speed = [-5, 0]
        elif listener.key == pygame.K_RIGHT and self.rect.right < WIDTH :#para saber si el usuario preciono la tecla derecha
            self.speed = [5, 0]
        else :
            self.speed = [0, 0]     

        self.rect.move_ip(self.speed)

#Fin de la  Classe barra que realiza el recorrido de izquierda a derecha

#Inicio de Clase ladrillo
class Brick(pygame.sprite.Sprite):#sprite forma de tratar las imagenes →→→ Ladrillos
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/ladrillo.png')#Cargar la Imagen del ladrillo
        self.rect = self.image.get_rect()#permite obtener el rectangulo de la imagen
        self.rect.topleft = position #Para darle una posicion inicial parte superior izquierda

#Fin de Clase ladrillo

#Inicio de Clase muro
class Wall(pygame.sprite.Group):#
    def __init__(self, totalBricks):#totalBricks, es para el total de ladrillos
        pygame.sprite.Group.__init__(self)#para crear un grupo o replicar el objeto que ingresa
        posX = 0
        posY = 10

        for i in range(totalBricks):#para dibujar la cantidad de ladrillos que se quiere
            brick = Brick(( posX, posY ))
            self.add(brick)#agrega el ladrillo que llegue

            posX += brick.rect.width#+=, quiere decir que incremente o aumente un ladrillo haia el ancho
            if posX >= WIDTH :#validar si llega al limite del ancho 
                posX = 0
                posY += brick.rect.height#+=, quiere decir que incremente o aumente un ladrillo 
    
#Fin de Clase muro 

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
game_clock = pygame.time.Clock()#reloj
pygame.key.set_repeat(20)#para que me acepte la tecla presioar de la barra

'''
   RGB:
   Colores Red, Green, Blue de fondo, trabajados en Hexadecimal que desde
   0 hasta 255
'''
BG_COLOR = (0, 191, 255) # (Red, Green, Blue)

#Inicio de invocaciones
ball = Ball()#se llama la instancia de la clase bolita (Ball) y nombra una variable(ball)
player = Bar()# manipula la barra el jugador
wall = Wall(112)#muro que tiene 112 ladrillos
#Fin de invocaciones

#Loop (Revisión cíclica de los eventos) => Listener esta pendiente del acontecimiento
while True:
    game_clock.tick(60)#frame por segundo
    for event in pygame.event.get():#mientras no presione un evento de cierrar, se mantendra abierta
        if event.type == pygame.QUIT:#si preciona x en la ventana sale
            pygame.quit()#cierra la ventana
            sys.exit()#cierra o destruye todos los procesos 
        elif event.type == pygame.KEYDOWN : #Verificar si el jugador presionó tecla del teclado
            player.slide(event)

   # ball.saludos()  #Saludos por consola
    ball.pibot() #Call pibot de la clase 1:     
    mywindows.fill(BG_COLOR)#color de dondo de ventana       
    #Draw de la ball
    mywindows.blit(ball.img_ball, ball.rect)
    #Draw de la bar
    mywindows.blit(player.img_bar, player.rect)
    #Dibujar muro
    wall.draw(mywindows)       
    pygame.display.flip()#Refresh de elementos en mywindows
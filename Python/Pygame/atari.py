'''
    Developer: Miller Salas
    Date: 5 - Oct - 2021
    Description:
    Desarrollo de la versión 1.0 de un video juego de atari.
'''

#Importamos librerias ((Inicio):
import sys
import pygame
import time
import os #son ejecuciones del sistema operativo
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
                            #[frecuencia del movimiento][amplitud del movimiento]
                            #[0,1]→ hace referencia a la posicion 0 del vector y posicion 1 del vector
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

#Inicio de Funcion o medoto  Game_Over
def Game_Over ():#Metodo o funcion si llega a tocar piso, pierda }
     mensaje = 'Perdiste, Vuelve a intentarlo'
     TextoColor = (0, 0, 139)#color del texto en RGB
     TextoEstilo = pygame.font.SysFont ('Arial', 40)#El tipo de fuente es de la libreria pygame
     txt_windows = TextoEstilo.render (mensaje, True, TextoColor)#Primer parametro → mensaje. Segundo parametro → True. Tercer parametro → color
     txt_windows_rect = txt_windows.get_rect ()#txt_windows_rect se guarda el rectangulo que se genera de txt_windows
     txt_windows_rect.center = [WIDTH/2, HEIGHT/2]#Se divide entre 2, para centrarlo en pantalla
     mywindows.blit (txt_windows, txt_windows_rect)#Setee texto en la pantalla principal. Llevara 2 parametros: parametro 1 → texto del render, parametro 2 → variable del rectangulo 
     pygame.display.flip ()
     print('Perdiste')#Mensaje por consola de pertdiste si toca piso
     time.sleep (3)#Pausa de 2 segundos para mostrar el mensaje 
    # sys.exit ()#cierra la ventana una vez pierda
#Fin de Funcion o medoto  Game_Over

#Inicio FuNCION O metodo Colocar_Puntaje 
def colocar_Puntaje ():
      TextoColor = (255, 255, 255)#color del texto en RGB
      TextoEstilo = pygame.font.SysFont ('Arial', 40)#El tipo de fuente es de la libreria pygame.
                                                     #TextoEstilo → sale en gris porque esta declarada pero que no esta en uso
      txt_windows = TextoEstilo.render (str (puntaje).zfill (5), True, TextoColor)#Primer parametro → puntaje. Segundo parametro → True. Tercer parametro → color  
                                                                                 #str (puntaje) → se lo pasa a string
                                                                                 # zfill (1) →  
      txt_windows_rect = txt_windows.get_rect ()#txt_windows_rect se guarda el rectangulo que se genera de txt_windows
      txt_windows_rect.topleft = [0, 0]
      mywindows.blit (txt_windows, txt_windows_rect)#Setee texto en la pantalla principal. Llevara 2 parametros: parametro 1 → texto del render, parametro 2 → variable del rectangulo 

#Fin FuNCION O metodo Colocar_Puntaje 


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

#Inicio validar la candidad de ladrillos
print('Menu nivel de juego')
print('1. Nivel Normal')
print('2. Nivel Intermedio')
print('3. Nivel Avanzado')
print('4. Salir')

Estado =True
while Estado:#Condicional que nos pide el nivel, siempre que el numero ingresado este dentro del rango.
    total_latrillos = int(input('Seleccione el nivel '))
    if total_latrillos >= 1 and total_latrillos <= 4:#Rango de 1 a 3
        Estado = False
if total_latrillos == 1:
     total_latrillos =20
elif total_latrillos == 2:
     total_latrillos = 10
elif total_latrillos == 3:
     total_latrillos = 200
elif total_latrillos == 4:
     print('Has salido del juego')
     os.system ('Pause')# os probiene de → import os
     sys.exit ()#cierra la ventana
else:
    print('Opcion invalida')
    os.system ('Pause')# os probiene de → import os
    sys.exit ()#cierra la ventana
   
wall = Wall(total_latrillos)#muro que tiene 112 ladrillos
#Fin validar cantidad de ladrillos 

puntaje = 0
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
    colocar_Puntaje ()
    mywindows.blit(ball.img_ball, ball.rect)#Draw de la ball
    mywindows.blit(player.img_bar, player.rect)#Draw de la bar
    wall.draw(mywindows)       #Dibujar muro   
    pygame.display.flip()#Refresh de elementos en mywindows

#Inicio de la programcion de Collisions entre barra y bola
    if pygame.sprite.collide_rect(ball, player):#collide_rect lo que permite es cambiar (trayectoria) la amplitud, solo la afecta
      ball.speed [1] = -ball.speed [1]#rebota en la barra y cambie la trayectoria de la posicion 1 en base al rebote  
#Fin de la programcion de Collisions entre barra y bola

#Inicio de programacion de Collisions entre la bola y el wall(ladrillos) → destruir ladrillos
    ladrillos = pygame.sprite.spritecollide(ball,  wall, False, collided = None) #guardamos en una variable vector→(ladrillos),la canditad de ladrillos
                                            #sprite: Es el objeto que va a chocar, es la bolita. ponemos en la funcion ball
                                            #grop: Son los elementos  que toca la bolita y los destruye los ladrillos. ponemos en la funcion wall
                                            #dokill: quitamos dokill de la funcion por el momento y ponemos false 
    if ladrillos:#Mientras existan ladrillos para chocar
        Brick = ladrillos [0]#ladrillos [0], quiere decir posicion 0 → ball
        centroX = ball.rect.centerx#centerx → es palabra reservada

        if centroX < Brick.rect.left or centroX >Brick.rect.right:#vamos 
            ball.speed[0] = -ball.speed [0]#afectamos el valor de la veolocidad, lo negamos con -
        else:
            ball.speed [1] = ball.speed [1]#Vamos afectar la trayectoria
              
        wall.remove(Brick)#aqui se quitan los ladrillos
        puntaje = puntaje + 1#Primera forma de hacer el incremento
                             #Segunda forma de hacer el incremento → puntaje += 1

    if ball.rect.bottom >= HEIGHT:#llamar la funcion Game_Over solo cuando la bola toca piso
       Game_Over ()#LLamamos a la funcion Game_Over, cuando la pelota toque piso

     #Fin de programacion de Collisions entre la bola y el wall(ladrillos)
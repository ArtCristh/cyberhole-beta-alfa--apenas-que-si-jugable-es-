import pygame,sys
from pygame.locals import*
import random
import math
import time

#inicializamos la libreria pygame
pygame.init()
#y colocamos la pantalla
x_fondo,y_fondo = 0,0
speed_fondo = 8
ancho_fondo, alto_fondo = 1700,1500

ANCHO_W, ALTO_W = 800, 600
#creamos algunas variables necesarias

#mostramos la pantalla
pygame.display.set_caption("dungeon figth prebeta/prealfa/preomega/no llega ni a jugable pero es avance/ solo falta el factor enemigos y colisiones")
pantalla =  pygame.display.set_mode((ANCHO_W,ALTO_W))

#variables de color
blanco = (255,255,255)
negro = (0,0,0)
rojo = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

#hacemos una clase para el jugador
class personajes :
	def __init__(self,x,y,speed,ancho,alto):
		self.x = x 
		self.y = y  
		self.speed = speed 
		self.ancho = ancho 
		self.alto = alto
class enemigos :
	def __init__(self,x,y,speed,ancho,alto):
		self.x = x
		self.y = y 
		self.speed = speed 
		self.ancho = ancho 
		self.alto = alto 
	def perseguir(self,player):
		dx = player.x - self.x
		dy = player.y - self.y
		distancia = math.hypot(dx,dy)
		if distancia != 0:
			dx /= distancia
			dy /= distancia 
		self.x+=dx * self.speed
		self.y+= dy *self.speed 


#hacemos una clase para los proyectiles
class proyectil :
	def __init__(self,bala_speed):
		self.bala_speed = bala_speed
	def trayectoria(self):
		angulo = math.atan2(mouse_posicion[1] - player.y, mouse_posicion[0] - player.x)
			#añadimos lo que este identado en la llave a la lista balas
		balas.append({
				"x":player.x + 10,
				"y":player.y + 10,
				"dx": math.cos(angulo)*bala.bala_speed,
				"dy": math.sin(angulo)*bala.bala_speed
				})
	def forloop(self):
		for disparo in balas:
			disparo["x"]+= disparo["dx"]
			disparo["y"]+= disparo["dy"]
	def mostrar_bala(self):
		for disparo in balas:
			pantalla.blit(shoot,(int(disparo["x"]), int(disparo["y"],)))

#creamos los objetos
player = personajes(400,300,5,20,20)
bala = proyectil(10)
enemigo = enemigos(0,0,1,30,30)


#creamos el relog para medir los fps
relog = pygame.time.Clock()
#cargamos las imagenes del jugador y el fondo
fondo = pygame.image.load("fondo_prueba_de_camara.png")
sprite = pygame.image.load("charles.png")
abajo = pygame.image.load("abajo.png")
arriba = pygame.image.load("arriba.png")
izquierda = pygame.image.load("izquierda.png")
derecha = pygame.image.load("derecha.png")
shoot = pygame.image.load("shoot.png")


#lo centramos

#creamos l
#crearemos un texto en pantalla
font = pygame.font.SysFont("PIXEL.ttf",30)
texto = font.render("DUNGEON", True,(blanco))
texto_recto = texto.get_rect()
#lo centramos
texto_recto.center = (400,15)
#creamos un rectangulo para el textoa variable la cual controlara el bucle
running = True
#creamos una lista donde se guardaran las balas
balas = []


#creamos el bucle principal de el juego

while running :
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
			mouse_posicion = pygame.mouse.get_pos()

			#calculamos la trayectoria
			bala.trayectoria()
			


	#iteracion de las bala
	bala.forloop()
	enemigo.perseguir(player)
	keys= pygame.key.get_pressed()
	if keys[K_w]:
		player.y-=player.speed
	if player.y <100 :
		y_fondo+=speed_fondo
	if keys[K_s]:
		player.y+=player.speed
	if player.y >500 :
		y_fondo-=speed_fondo
	if keys[K_d]:
		player.x+=player.speed
	if player.x <100 :
		x_fondo+=speed_fondo
	if keys[K_a]:
		player.x-=player.speed
	if player.x >700 :
		x_fondo-=speed_fondo


	balas = [x for x in balas if 0 <= x["x"] <= 800 and 0 <= x["y"] <= 600]
	#limitando el movimiento del cuadro
	player.x = max(0,min(800 - player.ancho, player.x))
	player.y= max(0,min(600 - player.alto, player.y))
	x_fondo = min(-8,max( 710 - ancho_fondo,x_fondo))
	y_fondo= min(-8,max(510 - alto_fondo,y_fondo))
	

	#dibujamos al personaje y su entornod
	pantalla.fill(blanco)
	pantalla.blit(fondo,(x_fondo,y_fondo))
	pantalla.blit(texto, texto_recto)
	
	#bucle para  que se generen balas y se creen infinitamente
	

	
	pantalla.blit(sprite,(enemigo.x,enemigo.y,enemigo.ancho,enemigo.alto))
	bala.mostrar_bala()
	pantalla.blit(sprite,(player.x,player.y,player.ancho,player.alto))
		    # Proyectiles  # Proyectiles





	#actualizamos la pantalla
	pygame.display.update()
	pygame.display.flip()
	relog.tick(120)



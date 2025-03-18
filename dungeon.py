import pygame,sys
from pygame.locals import*
import random
import math
import time

#inicializamos la libreria pygame
pygame.init()
#creamos las constantes

#y colocamos la pantalla

ANCHO_W, ALTO_W = 800, 600
pygame.display.set_caption("dungeon figth prebeta/prealfa/preomega/no llega ni a jugable pero es avance")
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
	def moverse_xy(self):
		keys= pygame.key.get_pressed()
		if keys[K_w]:
		  self.y-=self.speed
		if keys[K_s]:
		   self.y+=self.speed
		if keys[K_d]:
		   self.x+=self.speed
		if keys[K_a]:
		   self.x-=self.speed
class proyectil :
	def __init__(self,bala_speed):
		self.bala_speed = bala_speed

player = personajes(400,300,2.50,20,20)
bala = proyectil(10)


#creamos el relog para medir los fps
relog = pygame.time.Clock()
fondo = pygame.image.load("Sprite-0003.png")
sprite = pygame.image.load("charles.png")

#crearemos un texto en pantalla
font = pygame.font.SysFont("PIXEL.ttf",30)
texto = font.render("DUNGEON", True,(blanco))
texto_recto = texto.get_rect()
texto_recto.center = (400,15)

running = True
balas = []

#creamos el bucle principal de el juego


while running :
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
			mouse_posicion = pygame.mouse.get_pos()
			angulo = math.atan2(mouse_posicion[1] - player.y, mouse_posicion[0] - player.x)
			balas.append({
				"x":player.x,
				"y":player.y,
				"dx": math.cos(angulo)*bala.bala_speed,
				"dy": math.sin(angulo)*bala.bala_speed
				})


	#creamos el movimiento del personaje
	player.moverse_xy()

	for disparo in balas:
		disparo["x"]+= disparo["dx"]
		disparo["y"]+= disparo["dy"]

	balas = [x for x in balas if 0 <= x["x"] <= 800 and 0 <= x["y"] <= 600]
	#limitando el movimiento del cuadro
	player.x = max(0,min(800 - player.ancho, player.x))
	player.y= max(0,min(600 - player.alto, player.y))

	#dibujamos al personaje y su entorno
	pantalla.fill(negro)
	pantalla.blit(texto, texto_recto)
	#bucle para  que se generen balas y se creen infinitamente
	for disparo in balas:
		pygame.draw.circle(pantalla, rojo, (int(disparo["x"]), int(disparo["y"],)),10)
		    # Proyectiles  # Proyectiles

	pantalla.blit(sprite,(player.x,player.y,player.ancho,player.alto))





	#actualizamos la pantalla
	pygame.display.update()
	pygame.display.flip()
	relog.tick(60)



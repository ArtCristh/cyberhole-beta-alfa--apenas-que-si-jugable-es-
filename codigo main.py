
import pygame,sys
from pygame.locals import*
import random
import math
import time
from constantes import*
from funciones_y_clases import*


#inicializamos la libreria pygame
pygame.init()
#colocamos pantallas
#mostramos la pantalla
pygame.display.set_caption("dungeon figth prebeta/prealfa/preomega/no llega ni a jugable pero es avance/ solo falta el factor enemigos y colisiones")
pantalla =  pygame.display.set_mode((ANCHO_W,ALTO_W))
# aqui cargamos la imagenes necesarias

#aqui se crean las variables de texto y le daamos primero una fuente y tamaño
font = pygame.font.SysFont("PIXEL.ttf",30)
# aqui lo renderizamos
texto = font.render("DUNGEON", True, (blanco))
# aqui le damos un rectangulo al texto
texto_recto = texto.get_rect()
#lo centramos
texto_recto.center = (400,15)
#creamos el relog para medir los fps
relog = pygame.time.Clock()
#creamos las listas necesarias

#variable de arranque
running = True
#creamos el bucle principal del juego
while running :
	#creamos el for para medir los eventos dentro del juego
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			#aqui creamos una condicional para registrar los clicks del mouse y su posicion para poder hacer proyectiles
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
			mouse_posicion = pygame.mouse.get_pos()

			bala.trayectoria()

	bala.forloop()
	enemigo.perseguir(player)


	keys = pygame.key.get_pressed()
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

	#condicinal de colission pruebasss

	balas = [x for x in balas if 0 <= x["x"] <= 800 and 0 <= x["y"] <= 600]

	player.x = max(0,min(800 - player.ancho, player.x))
	player.y= max(0,min(600 - player.alto, player.y))
	x_fondo = min(-8,max( 710 - ancho_fondo,x_fondo))
	y_fondo= min(-8,max(510 - alto_fondo,y_fondo))

#mostramos las imagenes necesarias 
	pantalla.fill(blanco)
	pantalla.blit(fondo,(x_fondo,y_fondo))
#aqui mostrarmos todos los textos 
	pantalla.blit(texto, texto_recto)
	bala.mostrar_bala()
	pantalla.blit(sprite,(player.x,player.y,player.ancho,player.alto))
	#aqui actualizamos la pantalla y los objetos del juego
	pygame.display.update()
	pygame.display.flip()
	#aqui controlamos los fps(fotogramas por segundo)
	relog.tick(60)
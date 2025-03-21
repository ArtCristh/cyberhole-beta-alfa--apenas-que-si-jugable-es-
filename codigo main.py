
import pygame,sys
from pygame.locals import*
import random
import math
import time
import constantes
from funciones_y_clases import*


#inicializamos la libreria pygame
pygame.init()
#colocamos pantallas
#mostramos la pantalla
pygame.display.set_caption("dungeon figth prebeta/prealfa/preomega/no llega ni a jugable pero es avance/ solo falta el factor enemigos y colisiones")
pantalla =  pygame.display.set_mode((constantes.ANCHO_W,constantes.ALTO_W))
# aqui cargamos la imagenes necesarias
fondo = pygame.image.load("fondo_prueba_de_camara.png")
#aqui se crean las variables de texto y le daamos primero una fuente y tamaño
font = pygame.font.SysFont("PIXEL.ttf",30)
# aqui lo renderizamos
texto = font.render("DUNGEON", True, (constantes.blanco))
# aqui le damos un rectangulo al texto
texto_recto = texto.get_rect()
#lo centramos
texto_recto.center = (400,15)
#creamos el relog para medir los fps
relog = pygame.time.Clock()
#creamos las listas necesarias
balas = []
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





#mostramos las imagenes necesarias 
	pantalla.blit(fondo,(constantes.x_fondo,constantes.y_fondo))
#aqui mostrarmos todos los textos 
	pantalla.blit(texto, texto_recto)
	#aqui actualizamos la pantalla y los objetos del juego
	pygame.display.update()
	pygame.display.flip()
	#aqui controlamos los fps(fotogramas por segundo)
	relog.tick(60)
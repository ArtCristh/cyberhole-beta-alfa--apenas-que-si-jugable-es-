import pygame,sys
from pygame.locals import*
import random
import math
import time
from funciones_y_clases import*
from constantes import*
from enemigos import*


#inicializamos la libreria pygame
pygame.init()
#y colocamos la pantalla
x_fondo,y_fondo = 0,0
speed_fondo = 8
ancho_fondo, alto_fondo = 1700,1500

ANCHO_W, ALTO_W = 800, 600
inicio = time.time()
intervalo_bala =0.3 
ammo = 0
recarga = 5
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
	def __init__(self,vida,x,y,speed,ancho,alto):
		self.vida = vida
		self.x = x 
		self.y = y  
		self.speed = speed 
		self.ancho = ancho 
		self.alto = alto
class enemigos :
	def __init__(self,vida,x,y,speed,ancho,alto):
		self.vida = vida
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

player = personajes(5,400,300,5,20,20)
bala = proyectil(10)
inicio_enemigo = time.time()
intervalo_enemigo = 5
boton = personajes(0,400,300,5,100,100)



#creamos el relog para medir los fps
relog = pygame.time.Clock()
#cargamos las imagenes del jugador y el fondo

#lo centramos

#creamos l
#crearemos un texto en pantalla


font = pygame.font.SysFont("PIXEL.ttf",50)
texto = font.render("dungeon", True,(blanco))
texto_recto = texto.get_rect()
#   lo centramos
texto_recto.center = (400,15)

Font = pygame.font.SysFont("PIXEL.ttf",10000000)
texto_2 = font.render("GAME OVER", True,(blanco))
texto_recto_2 = texto_2.get_rect()
#   lo centramos
texto_recto_2.center = (400,30)

#creamos un rectangulo para el textoa variable la cual controlara el bucle
running = True
nivel = 0

#creamos una lista donde se guardaran las balas
balas = []
#timer no tocar
tiempo_restante = 5*60


ultimo_tick = pygame.time.get_ticks()


#creamos el bucle principal de el juego

while running :
	tiempo_actual = time.time()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if tiempo_actual - inicio>= intervalo_bala:
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
				mouse_posicion = pygame.mouse.get_pos()
				ammo+=1

				bala.trayectoria()
				inicio = tiempo_actual
		if nivel == 0:
			pantalla.fill(negro)
			if event.type == pygame.KEYDOWN and event.key== K_SPACE:
				nivel+=1

			#calculamos la trayectoria
				
	

	
	
	#iteracion de las bala

	balas = [x for x in balas if 0 <= x["x"] <= 800 and 0 <= x["y"] <= 600]
	#limitando el movimiento del cuadro
	player.x = max(5,min(780- player.ancho, player.x))
	player.y= max(5,min(580- player.alto, player.y))
	x_fondo = min(-100,max( 700 - ancho_fondo,x_fondo))
	y_fondo= min(-100,max(500 - alto_fondo,y_fondo))
	

	#dibujamos al personaje y su entornod

	
	#bucle para  que se generen balas y se creen infinitamente
	


	if nivel==1 :
		tiempo_actual = pygame.time.get_ticks()
		pantalla.blit(fondo,(x_fondo,y_fondo))
		pantalla.blit(texto, texto_recto)
		enemy_1(pantalla,enemigo,enemigo2,enemigo3,player)
		enemy_2(pantalla,enemigo4,enemigo5,enemigo6,player)
		bosses(pantalla,enemigo7,player)
		pantalla.blit(sprite2,(player.x,player.y,player.ancho,player.alto))

		

		if tiempo_actual - ultimo_tick >= 1000:

			if tiempo_restante> 0 :
				tiempo_restante -= 1
				ultimo_tick = tiempo_actual
				
				breakpoint

		minutos = tiempo_restante//60
		segundos = tiempo_restante%60
		exto= f"{minutos:02}:{segundos:02}"
		contador =pygame.font.SysFont("PIXEL.tff",10000)
		contador_tex=font.render(exto,True,(blanco))
		contador_rect = contador_tex.get_rect()
		contador_rect.center =(100,30)

		pantalla.blit(contador_tex,contador_rect)

		
		#lopp para la generacion de las balas
	#funcion de perseguir del enemigoç
		
		
		bala.forloop()
		bala.mostrar_bala()
		

		keys= pygame.key.get_pressed()
		if keys[K_w]:
			player.y-=player.speed
		if player.y <100 :
			y_fondo+=speed_fondo
		if keys[K_s]:
			player.y+=player.speed
		if player.y >=500 :
			y_fondo-=speed_fondo
		if keys[K_d]:
			player.x+=player.speed
		if player.x <100 :
			x_fondo+=speed_fondo
		if keys[K_a]:
			player.x-=player.speed
		if player.x >700 :
			x_fondo-=speed_fondo
		if keys[K_g]:
			running = False


		
		colisiones(player,enemigo,enemigo2,enemigo3,enemigo4,enemigo5,enemigo6,enemigo7,speed_colision)
		colision_bala(balas,enemigo,enemigo2,enemigo3,enemigo4,enemigo5,enemigo6,enemigo7)

		

		if player.vida <=0 :
			pantalla.fill(negro)
			pantalla.blit(texto_2,texto_recto_2)
			pantalla.blit(game_over_trans,(200,200))
		elif tiempo_restante <= 0 :
			pantalla.fill(negro)
					
	#actualizamos la pantallaBa
	pygame.display.update()
	pygame.display.flip()
	relog.tick(60)



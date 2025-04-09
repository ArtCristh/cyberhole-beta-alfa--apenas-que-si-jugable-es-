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
intervalo_bala =0.1 
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


font = pygame.font.SysFont("DS-TERM.TTF",50)
texto = font.render("PRACTICE HOLE ", True,(blanco))
texto_recto = texto.get_rect()
#   lo centramos
texto_recto.center = (400,20)

Font = pygame.font.SysFont("DS-TERM.TTF",100)
texto_2 = font.render("GAME OVER", True,(blanco))
texto_recto_2 = texto_2.get_rect()
#   lo centramos
texto_recto_2.center = (400,50)

Lont = pygame.font.SysFont("DS-TERM.TTf",50)
texto_main = font.render("<CYBER_HOLE>", True,(blanco))
texto_recto_main = texto_main.get_rect()
#   lo centramos
texto_recto_main.center = (400,100)

Lont = pygame.font.SysFont("DS-TERM.TTf",100)
texto_LEVEL2 = font.render("<CONTINUE?>", True,(blanco))
texto_recto_LEVEL2 = texto_main.get_rect()
#   lo centramos
texto_recto_LEVEL2.center = (400,200)

#creamos un rectangulo para el textoa variable la cual controlara el bucle
nivel_1= True
nivel_2= False
stage = 0

#creamos una lista donde se guardaran las balas
balas = []
#timer no tocar
tiempo_restante = 5

intentos= 1000


ultimo_tick = pygame.time.get_ticks()


#creamos el bucle principal de el juego

while nivel_1 :
	tiempo_actual = time.time()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			nivel_1= False
		if tiempo_actual - inicio>= intervalo_bala:
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
				mouse_posicion = pygame.mouse.get_pos()
				ammo+=1

				bala.trayectoria()

				inicio = tiempo_actual
		if stage == 0:
			pantalla.fill(negro)
			pantalla.blit(texto_main, texto_recto_main)
			if event.type == pygame.KEYDOWN and event.key== K_SPACE:
				stage+=1


			#calculamos la trayectoria
				
	

	
	
	#iteracion de las bala

	balas = [x for x in balas if 0 <= x["x"] <= 800 and 0 <= x["y"] <= 600]
	#limitando el movimiento del cuadro
	player.x = max(0,min(780- player.ancho, player.x))
	player.y= max(0,min(565- player.alto, player.y))
	x_fondo = min(-100,max( 700 - ancho_fondo,x_fondo))
	y_fondo= min(-100,max(500 - alto_fondo,y_fondo))
	

	#dibujamos al personaje y su entornod

	
	#bucle para  que se generen balas y se creen infinitamente
	


	if stage==1 :
		if player.vida>=1:
		
			tiempo_actual = pygame.time.get_ticks()
			pantalla.blit(fondo,(x_fondo,y_fondo))
			if tiempo_restante <= 250:
				enemy_1(pantalla,enemigo,enemigo2,enemigo3,player)
				enemy_2(pantalla,enemigo4,enemigo5,enemigo6,player)
				bosses(pantalla,enemigo7,player)
				colisiones(player,enemigo,enemigo2,enemigo3,enemigo4,enemigo5,enemigo6,enemigo7,speed_colision)
				colision_bala(balas,enemigo,enemigo2,enemigo3,enemigo4,enemigo5,enemigo6,enemigo7)
			pantalla.blit(sprite2,(player.x,player.y,player.ancho,player.alto))


			pantalla.blit(texto, texto_recto)
			if tiempo_restante <= 200:
				enemy_3(pantalla,enemigo8,enemigo9,enemigo10,player)
				enemy_4(pantalla,enemigo11,enemigo12,enemigo14,player)
				bosses_2(pantalla,enemigo15,player)
				colisiones_2(player,enemigo8,enemigo9,enemigo10,enemigo11,enemigo12,enemigo14,enemigo15,speed_colision)
				colision_bala_2(balas,enemigo8,enemigo9,enemigo10,enemigo11,enemigo12,enemigo14,enemigo15)

			

			
			

			

			if tiempo_actual - ultimo_tick >= 1000:

				if tiempo_restante> 0 :
					tiempo_restante -= 1
					ultimo_tick = tiempo_actual
					
					breakpoint

			minutos = tiempo_restante//60
			segundos = tiempo_restante%60
			exto= f"{minutos:02}:{segundos:02}"
			contador =pygame.font.SysFont("DS-TERM.TTF",100)
			contador_tex=font.render(exto,True,(blanco))
			contador_rect = contador_tex.get_rect()
			contador_rect.center =(400,50)

			pantalla.blit(contador_tex,contador_rect)

			
			#lopp para la generacion de las balas
		#funcion de perseguir del enemigoç
			
			
			bala.forloop()
			bala.mostrar_bala()
			

			keys= pygame.key.get_pressed()
			if keys[K_w]:
				player.y-=player.speed
			if player.y <150 :
				y_fondo+=speed_fondo
			if keys[K_s]:
				player.y+=player.speed
			if player.y >=450 :
				y_fondo-=speed_fondo
			if keys[K_d]:
				player.x+=player.speed
			if player.x <150 :
				x_fondo+=speed_fondo
			if keys[K_a]:
				player.x-=player.speed
			if player.x >650 :
				x_fondo-=speed_fondo
			if keys[K_g]:
				nivel_1 = False


			
			
		


		if tiempo_restante <= 0 :
			stage+=2
			if stage==3:
				pantalla.fill(negro)
				nivel_1 = False
				time.sleep(2)
				nivel_2=True
		elif player.vida <=0 :
			stage+= 1
			if stage==2:
				time.sleep(2)
				pantalla.fill(negro)
				pantalla.blit(texto_2,texto_recto_2)
				pantalla.blit(game_over_trans,(200,200))
				player.vida=5
				tiempo_restante=5*60
				stage=0



	pygame.display.update()
	relog.tick(120)

tiempo_restante= 5*60

stage2=0


while nivel_2 :
	tiempo_actual = time.time()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			nivel_2= False
		if tiempo_actual - inicio>= intervalo_bala:
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
				mouse_posicion = pygame.mouse.get_pos()
				ammo+=1

				bala.trayectoria()
				inicio = tiempo_actual
		if stage2 == 0:
			pantalla.fill(negro)
			pantalla.blit(texto_LEVEL2, texto_recto_LEVEL2)
			if event.type == pygame.KEYDOWN and event.key== K_SPACE:
				stage2+=1

			#calculamos la trayectoria
				
	

	
	
	#iteracion de las bala

	balas = [x for x in balas if 0 <= x["x"] <= 800 and 0 <= x["y"] <= 600]
	#limitando el movimiento del cuadro
	player.x = max(0,min(780- player.ancho, player.x))
	player.y= max(0,min(565- player.alto, player.y))
	x_fondo = min(-100,max( 700 - ancho_fondo,x_fondo))
	y_fondo= min(-100,max(500 - alto_fondo,y_fondo))
	

	#dibujamos al personaje y su entornod

	
	#bucle para  que se generen balas y se creen infinitamente
	


	if stage2==1 :
		
		tiempo_actual = pygame.time.get_ticks()
		pantalla.blit(fondo,(x_fondo,y_fondo))
		if tiempo_restante <= 250:
			enemy_1(pantalla,enemigo,enemigo2,enemigo3,player)
			enemy_2(pantalla,enemigo4,enemigo5,enemigo6,player)
			bosses(pantalla,enemigo7,player)
			colisiones(player,enemigo,enemigo2,enemigo3,enemigo4,enemigo5,enemigo6,enemigo7,speed_colision)
		pantalla.blit(sprite2,(player.x,player.y,player.ancho,player.alto))
		pantalla.blit(texto, texto_recto)
		if tiempo_restante <= 200:
			enemy_3(pantalla,enemigo8,enemigo9,enemigo10,player)
			enemy_4(pantalla,enemigo11,enemigo12,enemigo14,player)
			bosses_2(pantalla,enemigo15,player)
		

		

		if tiempo_actual - ultimo_tick >= 1000:

			if tiempo_restante> 0 :
				tiempo_restante -= 1
				ultimo_tick = tiempo_actual
				
				breakpoint

		minutos = tiempo_restante//60
		segundos = tiempo_restante%60
		exto= f"{minutos:02}:{segundos:02}"
		contador =pygame.font.SysFont("DS-TERM.TTF",100)
		contador_tex=font.render(exto,True,(blanco))
		contador_rect = contador_tex.get_rect()
		contador_rect.center =(400,50)

		pantalla.blit(contador_tex,contador_rect)

		
		#lopp para la generacion de las balas
	#funcion de perseguir del enemigoç
		
		
		bala.forloop()
		bala.mostrar_bala()
		

		keys= pygame.key.get_pressed()
		if keys[K_w]:
			player.y-=player.speed
		if player.y <150 :
			y_fondo+=speed_fondo
		if keys[K_s]:
			player.y+=player.speed
		if player.y >=450 :
			y_fondo-=speed_fondo
		if keys[K_d]:
			player.x+=player.speed
		if player.x <150 :
			x_fondo+=speed_fondo
		if keys[K_a]:
			player.x-=player.speed
		if player.x >650 :
			x_fondo-=speed_fondo
		if keys[K_g]:
			nivel_2 = False


		
		colisiones(player,enemigo,enemigo2,enemigo3,enemigo4,enemigo5,enemigo6,enemigo7,speed_colision)
		colisiones_2(player,enemigo8,enemigo9,enemigo10,enemigo11,enemigo12,enemigo14,enemigo15,speed_colision)
		colision_bala(balas,enemigo,enemigo2,enemigo3,enemigo4,enemigo5,enemigo6,enemigo7)
		colision_bala_2(balas,enemigo8,enemigo9,enemigo10,enemigo11,enemigo12,enemigo14,enemigo15)
		

		if player.vida <=0 :
			stage2+= 1
			if stage==2:
				pantalla.fill(negro)
				pantalla.blit(texto_2,texto_recto_2)
				pantalla.blit(game_over_trans,(200,200))
		elif tiempo_restante == 0 :
			stage2+=2
			if stage2==3:
				pantalla.fill(negro)


					
	#actualizamos la pantallaBa
	pygame.display.flip()
	relog.tick(120)



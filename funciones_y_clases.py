import pygame
from pygame.locals import*
from constantes import*
import math
pantalla =  pygame.display.set_mode((ANCHO_W,ALTO_W))
#cargamos las imagenes del jugador y el fondo
fondo = pygame.image.load("fondo_prueba_de_camara.png")
sprite = pygame.image.load("enemy_base.png")
enemy_sprite = pygame.transform.scale(sprite,(40,40))
boss = pygame.transform.scale(sprite,(60,60))
sprite2 = pygame.image.load("charles.png")
abajo = pygame.image.load("abajo.png")
arriba = pygame.image.load("arriba.png")
izquierda = pygame.image.load("izquierda.png")
derecha = pygame.image.load("derecha.png")
shoot = pygame.image.load("shoot.png")
game_over = pygame.image.load("game_over.jpg")
game_over_trans = pygame.transform.scale(game_over,(400,300))
sombra = pygame.image.load("sombra.png")
vida = pygame.image.load("vida.png")


balas = []

x_fondo,y_fondo = 0,0
speed_fondo = 8
ancho_fondo, alto_fondo = 1700,1500


class personajes :
	def __init__(self,vida,x,y,speed,ancho,alto):
		self.vida = vida
		self.x = x 
		self.y = y  
		self.speed = speed 
		self.ancho = ancho 
		self.alto = alto

	
	def moverse_moverfondo(self,keys):
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
class proyectil :
	def __init__(self,bala_speed):
		self.bala_speed = bala_speed
	def trayectoria(self):
		mouse_posicion = pygame.mouse.get_pos()
		angulo = math.atan2(mouse_posicion[1] - player.y, mouse_posicion[0] - player.x)
			#añadimos lo que este identado en la llave a la lista balas
		balas.append({
				"x":player.x +10,
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
	def quitar_balas(self):
		balas = [x for x in balas if 0 <= x["x"] <= 800 and 0 <= x["y"] <= 600]
class power_up:
	def __init__(self,x,y,ancho,alto):
		self.x = x
		self.y = y
		self.ancho = ancho
		self.alto = alto

player = personajes(5,400,300,5,20,20)
enemigo = enemigos(1,20,400,3.50,20,20)
bala = proyectil(15)


def som(pantalla,sombra):
	pantalla.blit(sombra,(0,0,800,600))





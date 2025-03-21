import pygame
from pygame.locals import*
import constantes



x_fondo,y_fondo = 0,0
speed_fondo = 8
ancho_fondo, alto_fondo = 1700,1500


class personajes(pygame.sprite.Sprite) :
	def __init__(self,x,y,speed,ancho,alto):
		super().__init__()
		self.x = x 
		self.y = y  
		self.speed = speed 
		self.ancho = ancho 
		self.alto = alto

		self.image = pygame.Surface((self.ancho,self.alto))
		self.image.fill((255,0,0))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x,y)
	def moverse_moverfondo(self,keys):
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



class enemigos(pygame.sprite.Sprite) :
	def __init__(self,x,y,speed,ancho,alto):
		super().__init__()
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
		angulo = math.atan2(mouse_posicion[1] - player.y, mouse_posicion[0] - player.x)
			#añadimos lo que este identado en la llave a la lista balas
		balas.append({
				"x":player.x +10,
				"y":player.y + 10,
				"dx": math.cos(angulo)*bala.bala_speed,
				"dy": math.sin(angulo)*bala.bala_speed
				})


player = personajes(400,300,5,20,20)
enemigo = enemigos(20,400,5,20,20)
bala = proyectil(10)




import pygame,sys
from pygame.locals import*
import random
import math
import time
from funciones_y_clases import*
from constantes import*
colision_enemy_to = 50


enemigo = enemigos(
		vida=1,
       	x=800,  # Posición aleatoria en x
        y=-100,  # Posición aleatoria en y
        speed=1,  # Velocidad aleatoria
        ancho=20,
        alto=20,
		)
enemigo2 = enemigos(
		vida=1,
       	x=random.randrange(0-100,800+100,800),  # Posición aleatoria en x
        y=random.randrange(0-100,600+100,600),  # Posición aleatoria en y
        speed=1,  # Velocidad aleatoria
        ancho=20,
        alto=20,
		)
enemigo3 = enemigos(
		vida=1,
       	x= -1000,  # Posición aleatoria en x
        y=0,  # Posición aleatoria en y
        speed=4,  # Velocidad aleatoria
        ancho=20,
        alto=20,
		)
enemigo4 = enemigos(
        vida=1,
        x= -100,  # Posición aleatoria en x
        y=500,  # Posición aleatoria en y
        speed=2,  # Velocidad aleatoria
        ancho=20,
        alto=20,
		)
enemigo5 = enemigos(
		vida=1,
        x= 1000,  # Posición aleatoria en x
        y=600,  # Posición aleatoria en y
        speed=4,  # Velocidad aleatoria
        ancho=20,
        alto=20,
		)
enemigo6 = enemigos(
		vida=1,
       	x=random.randrange(0-100,800+100,800),  # Posición aleatoria en x
        y=random.randrange(0-100,600+100,600),  # Posición aleatoria en y
        speed=random.randrange(1,3),  # Velocidad aleatoria
        ancho=20,
        alto=20,
		)
enemigo7 = enemigos(
		vida=10,
       	x=400,  # Posición aleatoria en x
        y=-200,  # Posición aleatoria en y
        speed=1,  # Velocidad aleatoria
        ancho=60,
        alto=60,
		)
power = power_up(
        x=200,  
        y=200,  
        ancho=30,
        alto=30,
        )

def enemy_1(pantalla,enemigo,enemigo2,enemigo3,player):
	enemigo.perseguir(player)
	enemigo2.perseguir(player)
	enemigo3.perseguir(player)
	pantalla.blit(enemy_sprite,(enemigo.x,enemigo.y))
	pantalla.blit(enemy_sprite,(enemigo2.x,enemigo2.y))
	pantalla.blit(enemy_sprite,(enemigo3.x,enemigo3.y))
def enemy_2(pantalla,enemigo4,enemigo5,enemigo6,player):
    enemigo4.perseguir(player)
    enemigo5.perseguir(player)
    enemigo6.perseguir(player)
    pantalla.blit(enemy_sprite,(enemigo4.x,enemigo4.y))
    pantalla.blit(enemy_sprite,(enemigo5.x,enemigo5.y))
    pantalla.blit(enemy_sprite,(enemigo6.x,enemigo6.y))
def bosses(pantalla,enemigo7,player):
    enemigo7.perseguir(player)
    pantalla.blit(boss,(enemigo7.x,enemigo7.y))
def mostrar_power(pantalla,power):
    pantalla.blit(vida,(power.x,power.y))

def colisiones(player,enemigo,enemigo2,enemigo3,enemigo4,enemigo5,enemigo6,enemigo7,speed_colision):
    if abs(player.x - enemigo.x) ==20 and abs(player.y - enemigo.y) == 20:
        player.x += speed_colision
        player.vida -= 1
        
    if abs(player.x - enemigo2.x) <=20 and abs(player.y - enemigo2.y) <= 20:
        player.x += speed_colision
        player.vida -= 1
        
    if abs(player.x - enemigo3.x) <=20 and abs(player.y - enemigo3.y) <= 20:
        player.x += speed_colision
        player.vida -= 1
        
    if abs(player.x - enemigo4.x) <=20 and abs(player.y - enemigo4.y) <= 20:
        player.x += speed_colision
        player.vida -= 1
        
    if abs(player.x - enemigo5.x) <=20 and abs(player.y - enemigo5.y) <= 20:
        player.x += speed_colision
        player.vida -= 1
        
    if abs(player.x - enemigo6.x) <=20 and abs(player.y - enemigo6.y) <= 20:
        player.x += speed_colision
        player.vida -= 1
    if abs(player.x - enemigo7.x) <=50 and abs(player.y - enemigo7.y) <= 50:
        player.x += speed_colision
        player.vida -= 2
def colision_bala(balas,enemigo,enemigo2,enemigo3,enemigo4,enemigo5,enemigo6,enemigo7):
    for shot in balas:
        distancia = math.sqrt((shot["x"] - enemigo.x)**2+(shot["y"] - enemigo.y)**2)

        if distancia <= colision_enemy_to :
            enemigo.vida-= 1
            for shot in balas :
                balas.remove(shot)        
            enemigo.x = 0
            enemigo.y = 0
            break
    for shot in balas:
        distancia = math.sqrt((shot["x"] - enemigo2.x)**2+(shot["y"] - enemigo2.y)**2)

        if distancia <= colision_enemy_to :
            enemigo2.vida-= 1
            for shot in balas :
                balas.remove(shot)
            enemigo2.x = 800
            enemigo2.y = 0
            break
    for shot in balas:
        distancia = math.sqrt((shot["x"] - enemigo3.x)**2+(shot["y"] - enemigo3.y)**2)

        if distancia <= colision_enemy_to :
            enemigo3.vida-= 1
            for shot in balas :
                balas.remove(shot)
            enemigo3.x = 1500
            enemigo3.y = 600
            break
    for shot in balas:
        distancia = math.sqrt((shot["x"] - enemigo4.x)**2+(shot["y"] - enemigo4.y)**2)

        if distancia <= colision_enemy_to :
            enemigo4.vida-= 1
            for shot in balas :
                balas.remove(shot)
            enemigo4.x = 0
            enemigo4.y = 600
            break
    for shot in balas:
        distancia = math.sqrt((shot["x"] - enemigo5.x)**2+(shot["y"] - enemigo5.y)**2)

        if distancia <= colision_enemy_to :
            enemigo5.vida-= 1
            for shot in balas :
                balas.remove(shot)
            enemigo5.x  = -400
            enemigo5.y = 0
            break
    for shot in balas:
        distancia = math.sqrt((shot["x"] - enemigo6.x)**2+(shot["y"] - enemigo6.y)**2)

        if distancia <= colision_enemy_to :
            enemigo6.vida-= 1
            for shot in balas :
                balas.remove(shot)
            enemigo6.x = 400
            enemigo6.y = 600
            break
    for shot in balas:
        distancia = math.sqrt((shot["x"] - enemigo7.x)**2+(shot["y"] - enemigo7.y)**2)

        if distancia <= colision_enemy_to :
            enemigo7.vida-= 1
            print(enemigo7.vida)
            for shot in balas :
                balas.remove(shot)
            if enemigo7.vida <= 0:
                enemigo7.x = 5000
                enemigo7.y = 5000
                enemigo7.vida+= 10
                break
def colision_power_up(power,player):
    if abs(player.x - power.x) <=30 and abs(player.y - power.y) <= 30:
        player.vida+= 1
        print(player.vida)





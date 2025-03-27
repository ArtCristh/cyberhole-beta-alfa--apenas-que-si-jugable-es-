import pygame,sys
from pygame.locals import*
import random
import math
import time
from funciones_y_clases import*
from constantes import*

enemigo = enemigos(
		vida=1,
       	x=random.randrange(0-100,800+100,800),  # Posición aleatoria en x
        y=random.randrange(0-100,600+100,600),  # Posición aleatoria en y
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
		vida=1,
       	x=random.randrange(0-100,800+100,800),  # Posición aleatoria en x
        y=random.randrange(0-100,600+100,600),  # Posición aleatoria en y
        speed=random.randrange(1,3),  # Velocidad aleatoria
        ancho=20,
        alto=20,
		)
enemigo8 = enemigos(
		vida=1,
       	x=random.randrange(0-100,800+100,800),  # Posición aleatoria en x
        y=random.randrange(0-100,600+100,600),  # Posición aleatoria en y
        speed=random.randrange(1,3),  # Velocidad aleatoria
        ancho=20,
        alto=20,
		)
enemigo9 = enemigos(
		vida=1,
       	x=random.randrange(0-100,800+100,800),  # Posición aleatoria en x
        y=random.randrange(0-100,600+100,600),  # Posición aleatoria en y
        speed=random.randrange(1,3),  # Velocidad aleatoria
        ancho=20,
        alto=20,
		)
enemigo10 = enemigos(
		vida=1,
       	x=random.randrange(0-100,800+100,800),  # Posición aleatoria en x
        y=random.randrange(0-100,600+100,600),  # Posición aleatoria en y
        speed=random.randrange(1,2),  # Velocidad aleatoria
        ancho=20,
        alto=20,
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
def colisiones(player,enemigo,enemigo2,enemigo3,enemigo4,enemigo5,enemigo6,speed_colision):
    if abs(player.x - enemigo.x) <=20 and abs(player.y - enemigo.y) <= 20:
        player.x += speed_colision
        player.vida -= 1
        print(player.vida)
    if abs(player.x - enemigo2.x) <=20 and abs(player.y - enemigo2.y) <= 20:
        player.x += speed_colision
        player.vida -= 1
        print(player.vida)
    if abs(player.x - enemigo3.x) <=20 and abs(player.y - enemigo3.y) <= 20:
        player.x += speed_colision
        player.vida -= 1
        print(player.vida)
    if abs(player.x - enemigo4.x) <=20 and abs(player.y - enemigo4.y) <= 20:
        player.x += speed_colision
        player.vida -= 1
        print(player.vida)
    if abs(player.x - enemigo5.x) <=20 and abs(player.y - enemigo5.y) <= 20:
        player.x += speed_colision
        player.vida -= 1
        print(player.vida)
    if abs(player.x - enemigo6.x) <=20 and abs(player.y - enemigo6.y) <= 20:
        player.x += speed_colision
        player.vida -= 1
        print(player.vida)


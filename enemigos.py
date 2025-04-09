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
        y=-2000,  # Posición aleatoria en y
        speed=1,  # Velocidad aleatoria
        ancho=60,
        alto=60,
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


def colisiones(player,enemigo,enemigo2,enemigo3,enemigo4,enemigo5,enemigo6,enemigo7,speed_colision):
    if abs(player.x - enemigo.x) ==30 and abs(player.y - enemigo.y) == 30:
        player.x += speed_colision
        player.vida -= 1
        
    if abs(player.x - enemigo2.x) <=30 and abs(player.y - enemigo2.y) <=30:
        player.x += speed_colision
        player.vida -= 1
        
    if abs(player.x - enemigo3.x) <=30 and abs(player.y - enemigo3.y) <=30:
        player.x += speed_colision
        player.vida -= 1
        
    if abs(player.x - enemigo4.x) <=30 and abs(player.y - enemigo4.y) <=30:
        player.x += speed_colision
        player.vida -= 1
        
    if abs(player.x - enemigo5.x) <=30 and abs(player.y - enemigo5.y) <=30:
        player.x += speed_colision
        player.vida -= 1
        
    if abs(player.x - enemigo6.x) <=30 and abs(player.y - enemigo6.y) <=30:
        player.x += speed_colision
        player.vida -= 1
    if abs(player.x - enemigo7.x) <=50 and abs(player.y - enemigo7.y) <=50:
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
            enemigo3.x = 800
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
            enemigo5.x  = 0
            enemigo5.y = 300
            break
    for shot in balas:
        distancia = math.sqrt((shot["x"] - enemigo6.x)**2+(shot["y"] - enemigo6.y)**2)

        if distancia <= colision_enemy_to :
            enemigo6.vida-= 1
            for shot in balas :
                balas.remove(shot)
            enemigo6.x = 800
            enemigo6.y = 300
            break
    for shot in balas:
        distancia = math.sqrt((shot["x"] - enemigo7.x)**2+(shot["y"] - enemigo7.y)**2)

        if distancia <= colision_enemy_to :
            enemigo7.vida-= 1
            for shot in balas :
                balas.remove(shot)
            if enemigo7.vida <= 0:
                enemigo7.x = 5000
                enemigo7.y = 5000
                enemigo7.vida+= 10
                break


enemigo8 = enemigos(
        vida=1,
        x=800,  # Posición aleatoria en x
        y=800,  # Posición aleatoria en y
        speed=1,  # Velocidad aleatoria
        ancho=30,
        alto=30,
        )
enemigo9 = enemigos(
        vida=1,
        x=random.randrange(0-100,800+100,800),  # Posición aleatoria en x
        y=random.randrange(0-100,600+100,600),  # Posición aleatoria en y
        speed=2,  # Velocidad aleatoria
        ancho=30,
        alto=30,
        )
enemigo10 = enemigos(
        vida=1,
        x= 1000,  # Posición aleatoria en x
        y=0,  # Posición aleatoria en y
        speed=4,  # Velocidad aleatoria
        ancho=30,
        alto=30,
        )
enemigo11 = enemigos(
        vida=1,
        x= -100,  # Posición aleatoria en x
        y=500,  # Posición aleatoria en y
        speed=2,  # Velocidad aleatoria
        ancho=30,
        alto=30,
        )
enemigo12 = enemigos(
        vida=1,
        x= 1000,  # Posición aleatoria en x
        y=-600,  # Posición aleatoria en y
        speed=4,  # Velocidad aleatoria
        ancho=30,
        alto=30,
        )
enemigo14 = enemigos(
        vida=1,
        x=random.randrange(0-100,800+100,800),  # Posición aleatoria en x
        y=random.randrange(0-100,600+100,600),  # Posición aleatoria en y
        speed=2,  # Velocidad aleatoria
        ancho=30,
        alto=30,
        )
enemigo15 = enemigos(
        vida=10,
        x=400,  # Posición aleatoria en x
        y=2000,  # Posición aleatoria en y
        speed=2,  # Velocidad aleatoria
        ancho=50,
        alto=50,
        )
        

def enemy_3(pantalla,enemigo8,enemigo9,enemigo10,player):
    enemigo8.perseguir(player)
    enemigo9.perseguir(player)
    enemigo10.perseguir(player)
    pantalla.blit(enemy_sprite,(enemigo8.x,enemigo8.y))
    pantalla.blit(enemy_sprite,(enemigo9.x,enemigo9.y))
    pantalla.blit(enemy_sprite,(enemigo10.x,enemigo10.y))
def enemy_4(pantalla,enemigo11,enemigo12,enemigo14,player):
    enemigo11.perseguir(player)
    enemigo12.perseguir(player)
    enemigo14.perseguir(player)
    pantalla.blit(enemy_sprite,(enemigo11.x,enemigo11.y))
    pantalla.blit(enemy_sprite,(enemigo12.x,enemigo12.y))
    pantalla.blit(enemy_sprite,(enemigo14.x,enemigo14.y))
def bosses_2(pantalla,enemigo15,player):
    enemigo15.perseguir(player)
    pantalla.blit(boss,(enemigo15.x,enemigo15.y))


def colisiones_2(player,enemigo8,enemigo9,enemigo10,enemigo11,enemigo12,enemigo14,enemigo15,speed_colision):
    if abs(player.x - enemigo8.x) ==30 and abs(player.y - enemigo8.y) == 30:
        player.x += speed_colision
        player.vida -= 1
        
    if abs(player.x - enemigo9.x) <=30 and abs(player.y - enemigo9.y) <=30:
        player.x += speed_colision
        player.vida -= 1
        
    if abs(player.x - enemigo10.x) <=30 and abs(player.y - enemigo10.y) <=30:
        player.x += speed_colision
        player.vida -= 1
        
    if abs(player.x - enemigo11.x) <=30 and abs(player.y - enemigo11.y) <=30:
        player.x += speed_colision
        player.vida -= 1
        
    if abs(player.x - enemigo12.x) <=30 and abs(player.y - enemigo12.y) <=30:
        player.x += speed_colision
        player.vida -= 1

    if abs(player.x - enemigo14.x) <=30 and abs(player.y - enemigo14.y) <=30:
        player.x += speed_colision
        player.vida -= 1

    if abs(player.x - enemigo15.x) <=50 and abs(player.y - enemigo15.y) <=50:
        player.x += speed_colision
        player.vida -= 2

def colision_bala_2(balas,enemigo8,enemigo9,enemigo10,enemigo11,enemigo12,enemigo14,enemigo15):
    for shot in balas:
        distancia = math.sqrt((shot["x"] - enemigo8.x)**2+(shot["y"] - enemigo8.y)**2)

        if distancia <= colision_enemy_to :
            enemigo8.vida-= 1
            for shot in balas :
                balas.remove(shot)        
            enemigo8.x = 0
            enemigo8.y = 0
            break
    for shot in balas:
        distancia = math.sqrt((shot["x"] - enemigo9.x)**2+(shot["y"] - enemigo9.y)**2)

        if distancia <= colision_enemy_to :
            enemigo9.vida-= 1
            for shot in balas :
                balas.remove(shot)
            enemigo9.x = 800
            enemigo9.y = 0
            break
    for shot in balas:
        distancia = math.sqrt((shot["x"] - enemigo10.x)**2+(shot["y"] - enemigo10.y)**2)

        if distancia <= colision_enemy_to :
            enemigo10.vida-= 1
            for shot in balas :
                balas.remove(shot)
            enemigo10.x = 1500
            enemigo10.y = 600
            break
    for shot in balas:
        distancia = math.sqrt((shot["x"] - enemigo11.x)**2+(shot["y"] - enemigo11.y)**2)

        if distancia <= colision_enemy_to :
            enemigo11.vida-= 1
            for shot in balas :
                balas.remove(shot)
            enemigo11.x = 0
            enemigo11.y = 600
            break
    for shot in balas:
        distancia = math.sqrt((shot["x"] - enemigo12.x)**2+(shot["y"] - enemigo12.y)**2)

        if distancia <= colision_enemy_to :
            enemigo12.vida-= 1
            for shot in balas :
                balas.remove(shot)
            enemigo12.x  = -400
            enemigo12.y = 0
            break
    for shot in balas:
        distancia = math.sqrt((shot["x"] - enemigo14.x)**2+(shot["y"] - enemigo14.y)**2)

        if distancia <= colision_enemy_to :
            enemigo14.vida-= 1
            for shot in balas :
                balas.remove(shot)
            enemigo14.x = 400
            enemigo14.y = 600
            break
    for shot in balas:
        distancia = math.sqrt((shot["x"] - enemigo15.x)**2+(shot["y"] - enemigo15.y)**2)

        if distancia <= colision_enemy_to :
            enemigo15.vida-= 1
            for shot in balas :
                balas.remove(shot)
            if enemigo15.vida <= 0:
                enemigo15.x = 5000
                enemigo15.y = -5000
                enemigo15.vida+= 10
                break





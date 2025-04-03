import pygame,sys
from pygame.locals import*
import random
import math
import time
from funciones_y_clases import*
from constantes import*
from enemigos import*
from codigo_original import*

tiempo_restante = 5*60

ultimo_tick = pygame.time.get_ticks()

def timer(ultimo_tick,pantalla):
    tiempo_actual = pygame.time.get_ticks()

    if tiempo_actual - ultimo_tick >= 1000:
        if tiempo_restante> 0 :
            tiempo_restante -= 1
        ultimo_tick = tiempo_actual

    minutos = tiempo_restante//60
    segundos = tiempo_restante%60
    
    pantalla.blit(texto,texto_recto)





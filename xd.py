import pygame
import random
import math

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Enemigos persiguiendo al jugador")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Jugador
jugador = pygame.Rect(ancho // 2 - 25, alto // 2 - 25, 50, 50)
velocidad_jugador = 5

# Clase enemigo
class Enemigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 2

    def mover_hacia_jugador(self):
        # Calcular dirección hacia el jugador
        dx = jugador.x + jugador.width // 2 - self.x
        dy = jugador.y + jugador.height // 2 - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        if distancia != 0:
            self.x += self.velocidad * dx / distancia
            self.y += self.velocidad * dy / distancia

    def dibujar(self, ventana):
        pygame.draw.circle(ventana, ROJO, (int(self.x), int(self.y)), 15)

# Lista de enemigos
enemigos = []

# Función para generar enemigos aleatoriamente cerca de los límites
def generar_enemigo():
    margen = 50  # Distancia desde el borde
    x = random.choice([random.randint(0, margen), random.randint(ancho - margen, ancho)])
    y = random.choice([random.randint(0, margen), random.randint(alto - margen, alto)])
    enemigos.append(Enemigo(x, y))

# Bucle principal
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    ventana.fill(NEGRO)

    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Movimiento del jugador con las teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and jugador.y > 0:
        jugador.y -= velocidad_jugador
    if keys[pygame.K_DOWN] and jugador.y < alto - jugador.height:
        jugador.y += velocidad_jugador
    if keys[pygame.K_LEFT] and jugador.x > 0:
        jugador.x -= velocidad_jugador
    if keys[pygame.K_RIGHT] and jugador.x < ancho - jugador.width:
        jugador.x += velocidad_jugador

    # Dibujar jugador
    pygame.draw.rect(ventana, AZUL, jugador)

    # Generar enemigos aleatoriamente
    if random.randint(1, 60) == 1:  # Generar aproximadamente un enemigo por segundo
        generar_enemigo()

    # Mover y dibujar enemigos
    for enemigo in enemigos:
        enemigo.mover_hacia_jugador()
        enemigo.dibujar(ventana)

    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(60)

# Cerrar Pygame
pygame.quit()

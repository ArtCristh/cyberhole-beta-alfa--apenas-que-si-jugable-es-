import pygame
import math
import random

# Inicializar Pygame
pygame.init()

# Configurar pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Persecución de enemigos")

# Colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Clase Jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect(center=(ANCHO // 2, ALTO // 2))

    def mover(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            self.rect.y -= 5
        if teclas[pygame.K_DOWN]:
            self.rect.y += 5
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 5
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 5

# Clase Enemigo
class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect(center=(random.randint(0, ANCHO), random.randint(0, ALTO)))
        self.velocidad = 2

    def perseguir(self, jugador):
        dx = jugador.rect.x - self.rect.x
        dy = jugador.rect.y - self.rect.y
        distancia = math.hypot(dx, dy)
        if distancia != 0:
            dx /= distancia
            dy /= distancia

        # Actualizar posición hacia el jugador
        self.rect.x += int(dx * self.velocidad)
        self.rect.y += int(dy * self.velocidad)

# Configurar sprites
jugador = Jugador()
enemigos = pygame.sprite.Group()

for _ in range(5):  # Crear 5 enemigos
    enemigo = Enemigo()
    enemigos.add(enemigo)

todos_sprites = pygame.sprite.Group(jugador, *enemigos)

# Bucle principal
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Actualizar
    jugador.mover()
    for enemigo in enemigos:
        enemigo.perseguir(jugador)

    # Dibujar
    pantalla.fill(NEGRO)
    todos_sprites.draw(pantalla)

    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

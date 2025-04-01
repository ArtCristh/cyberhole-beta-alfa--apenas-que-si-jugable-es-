import pygame
import sys

# Inicializar Pygame
pygame.init()

# Crear ventana
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Texto Actualizable en Pygame")

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Crear fuente
fuente = pygame.font.Font(None, 50)  # None usa la fuente predeterminada de Pygame

# Texto inicial
texto = "¡Hola, Pygame!"
contador = 0

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar el texto
    contador += 1
    texto_actualizado = f"Contador: {contador}"

    # Renderizar texto
    texto_renderizado = fuente.render(texto_actualizado, True, BLANCO)

    # Limpiar pantalla
    pantalla.fill(NEGRO)

    # Dibujar texto en pantalla
    pantalla.blit(texto_renderizado, (50, 50))  # Posición del texto (x, y)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.delay(100)

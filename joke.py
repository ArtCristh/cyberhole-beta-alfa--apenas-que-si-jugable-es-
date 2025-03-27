import pygame

ancho_w,alto_w = 100,700
intentos = 100

pantalla =pygame.display.set_mode((ancho_w,alto_w))

ejecutando = True

xd = pygame.image.load("")

while ejecutando :
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			intentos -= 1





	if intentos == 0 :
		ejecutando = False
	pygame.display.flip()


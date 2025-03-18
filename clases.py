import random
class personajes :
	def __init__ (self,nombre,vida,x,y,velocidad,ancho,alto,exp):
		self.nombre = nombre
		self.vida = vida
		self.x = x    
		self.y = y   
		self.velocidad = velocidad
		self.ancho = ancho
		self.alto = alto
		self.exp = exp
	def decir_vida(self):
		print(f" la vida de {self.nombre}  es :{self.vida}")
	def decir_exp(self):
		print(f"la exp de {self.nombre} es  : {self.exp}")
	def mover_x_y(self):
		print(f"la posicion x es : {self.x} y la posicion y es : {self.y} y es el objeto :{self.nombre}")
	def randomb(self):
		self.vida = random.randrange(5)
		print(self.vida)

enemigo = personajes("slime",50,50,50,5,5,5,False)
player = personajes("player",100,400,300,5.5,10,20,100)


enemigo.randomb()


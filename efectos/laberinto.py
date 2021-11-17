class Laberinto():
	def __init__(self , partida):
		self.laberinto=42

	def __str__(self):
		return "laberinto"


	def incluyeA(self , posicion): 
		return posicion == self.laberinto

	def aplicarEn(self , jugador):
		jugador.posicion=30 

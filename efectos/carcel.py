class Carcel():
	def __init__(self , partida):
		self.carcel =56
		self.partida = partida

	def __str__(self):
		return "carcel"


	def incluyeA(self , posicion): 
		return posicion == self.carcel

	def aplicarEn(self , jugador):
		jugador.turnos-=2

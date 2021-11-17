class Posada():
	def __init__(self , partida):
		self.posada=19

	def __str__(self):
		return "posada"


	def incluyeA(self , posicion): 
		return posicion == self.posada

	def aplicarEn(self , jugador):
		jugador.turnos-=1

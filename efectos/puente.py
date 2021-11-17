class Puente():
	def __init__(self , partida):
		self.puente=[6 , 12]

	def __str__(self):
		return "puente"


	def incluyeA(self , posicion): 
		return posicion in self.puente 

	def aplicarEn(self , jugador):
		jugador.posicion=19
		jugador.turnos-=1

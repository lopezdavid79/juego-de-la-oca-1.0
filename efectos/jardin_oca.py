class Jardin_oca():
	def __init__(self , partida):
		self.fin_oca=63
		self.partida = partida

	def __str__(self):
		return " Gano el juego "

	def incluyeA(self, posicion):
		return  posicion==  self.fin_oca

	def aplicarEn(self,jugador):
    		self.partida.finalizar()


class Oca():
	def __init__(self , partida):
		self.oca=[5,9,14, 18, 23, 27, 32, 36, 41, 45, 50, 54 , 59]

	def __str__(self):
		return "oca"


	def posicion_oca(self, posicion):
		pos=self.oca.index(posicion)
		pos=pos+1 
		return self.oca[pos] 


	def incluyeA(self, posicion):
		return  posicion in self.oca

	def aplicarEn(self,jugador):
		try:
			jugador.posicion = self.posicion_oca(jugador.posicion)
		except IndexError:
			pass
import unittest
from juego import Partida
from jugador import Jugador
from efectos import Oca

class TestJuegoOca(unittest.TestCase):
	def crear_partida(self):
		partida = Partida()
		david = Jugador("david")
		miguel = Jugador("miguel")
		partida.agregarJugador(david)
		partida.agregarJugador(miguel)
		return partida

	def test_UnaPartidaSeCreaConCeroJugadores(self):
		partida = Partida()
		self.assertEquals(partida.cantidadDeJugadores(), 0)

	def test_UnaPartidaAlAgregarunJugadorSeIncrementaElNumeroDeJugadores(self):
		partida = Partida()
		partida.agregarJugador("david")
		self.assertEquals(partida.cantidadDeJugadores(), 1)

	def test_UnaPartidaAlAgregarDosJugadorSeIncrementaElNumeroDeJugadores(self):
		partida = Partida()
		partida.agregarJugador("david")
		partida.agregarJugador("miguel")
		self.assertEquals(partida.cantidadDeJugadores(), 2)

	def test_UnapartidaConDosJugadoresSeBerificaQueElTurnoSeaDelPrimerJugador(self):
		partida = Partida()
		partida.agregarJugador("david")
		partida.agregarJugador("miguel")
		self.assertEquals(partida.jugadorActual(), "david")

	def test_UnaPartidaConDosJugadoresAlPasarElTurnoVerificamosQueElJugadorActualSeaElSegundoJugador(self):
		partida = Partida()
		partida.agregarJugador("david")
		partida.agregarJugador("miguel")
		partida.pasarTurno()
		self.assertEquals(partida.jugadorActual(), "miguel")
	
	def test_UnaPartidaConDosJugadoresSiPasamosElTurnoDosVecesElJugadorActualEsElPrimero(self):
		partida = Partida()
		partida.agregarJugador("david")
		partida.agregarJugador("miguel")
		partida.pasarTurno()
		partida.pasarTurno()
		self.assertEquals(partida.jugadorActual(), "david")
	
	def test_UnNuevoJugadorComienzaEnLaPosixionCero(self):
		jugador=Jugador()
		self.assertEquals(jugador.posicion,0)
	
	def test_UnJugadorNuevoAlLanzarElDadoSeModificaSuPosicion(self):
		partida = self.crear_partida()
		jugador = partida.jugadorActual()
		posicionInicial = jugador.posicion
		dado = partida.lanzarDadoPara(jugador)
		self.assertEquals(jugador.posicion, posicionInicial+dado)
	
	def test_UnJugadorAlCaerEnUnaOcaAvanzaHastaLaProximaOca(self):
		partida = self.crear_partida()
		jugador = partida.jugadorActual()
		jugador.posicion = 5
		partida.activarEfectoPara(jugador)
		self.assertEquals(jugador.posicion, 9)


	def test_UnJugadorAlCaerEnUnaCasillaSinEfectoSeQuedaEnLaMismaPosicion(self):
		partida = self.crear_partida()
		jugador = partida.jugadorActual()
		jugador.posicion = 4
		partida.activarEfectoPara(jugador)
		self.assertEquals(jugador.posicion, 4)

	def test_UnJugadorAlCaerEnElLaverintoCasilla42RetrocedeHastaLaCasilla30(self):
		partida = self.crear_partida()
		jugador = partida.jugadorActual()
		jugador.posicion = 42
		partida.activarEfectoPara(jugador)
		self.assertEquals(jugador.posicion, 30)

	def test_UnJugadorAlCaerEnElInfiernoCasilla58RetrocedeHastaLaCasilla1(self):
		partida = self.crear_partida()
		jugador = partida.jugadorActual()
		jugador.posicion = 58
		partida.activarEfectoPara(jugador)
		self.assertEquals(jugador.posicion, 1)
	
	def test_UnJugadorAlCaerEnLaPosadaPierdeUnTurno(self):
		partida = self.crear_partida()
		jugador = partida.jugadorActual()
		jugador.posicion = 19
		partida.activarEfectoPara(jugador)
		self.assertEquals(jugador.posicion, 19)
		self.assertEquals(jugador.turnos, -1)
#verificar test
	def test_UnJugadorQueNoTieneTurnoVerificarSiPuedeJugar(self):
		partida = self.crear_partida()
		jugador = partida.jugadorActual()
		jugador.turnos = -1
		self.assertFalse(partida.tieneTurno(jugador))

	def test_UnaPartidaCon2JugadoresCuandoElPrimeroTieneMenos1YPasaTurnoQuedaSuTurnoEn0(self):
		partida = self.crear_partida()
		jugador = partida.jugadorActual()
		jugador.turnos = -1
		partida.darTurno(jugador)
		self.assertEquals(jugador.turnos, 0)

	def test_UnJugadorAlCaerEnLaCarcelPierdeDosTurnos(self):
		partida = self.crear_partida()
		jugador = partida.jugadorActual()
		jugador.posicion = 56
		partida.activarEfectoPara(jugador)
		self.assertEquals(jugador.posicion, 56)
		self.assertEquals(jugador.turnos, -2)

	def test_UnJugadorAlCaerEnPuenteAvanzaALaPosadaYPierdeUnTurno(self):
		partida = self.crear_partida()
		jugador = partida.jugadorActual()
		jugador.posicion = 12
		partida.activarEfectoPara(jugador)
		self.assertEquals(jugador.posicion, 19)
		self.assertEquals(jugador.turnos, -1)

	def test_UnJugadorPuedeAvanzarUnaCantidadDePasos(self):
		partida = self.crear_partida()
		jugador = partida.jugadorActual()
		pasos=6
		posicionInicial=1
		jugador.posicion=posicionInicial

		partida.avanzarJugador(jugador,pasos)

		self.assertEquals(jugador.posicion, posicionInicial+pasos)
	
	def test_UnJugadorSiAvanzaMasDeLaCasillaLimiteRetrocede(self):
		partida = self.crear_partida()
		jugador = partida.jugadorActual()
		pasos=6
		posicionInicial=60
		jugador.posicion=posicionInicial

		partida.avanzarJugador(jugador,pasos)
		
		self.assertEquals(jugador.posicion, 57)



	def test_UnJugadorAlCaerEnElJardinDeLaOcaGanaLaPartida(self):
		partida = self.crear_partida()
		jugador = partida.jugadorActual()
		jugador.posicion=63
		partida.activarEfectoPara(jugador)
		self.assertFalse(partida.esta_activa())
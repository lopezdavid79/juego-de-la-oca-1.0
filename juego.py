#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from efectos import *


from random import randint


class Partida():
	def __init__(self,limite=63):
		self.jugadores = []
		self.puntero=0
		self.limite= limite
		self.activa= True
		self.efectos = [Oca(self),
			Laberinto(self),
			Infierno(self),
			Posada(self),
			Puente(self),
			Jardin_oca(self),
			Carcel(self)]


	def listar(self):
		return self.jugadores
	def cantidadDeJugadores(self):
		return len(self.jugadores)


	def agregarJugador(self, jugador):
		self.jugadores.append(jugador)
	
	def jugadorActual(self):
		return self.jugadores[self.puntero]

	def pasarTurno(self):
		self.puntero = (self.puntero+1)%len(self.jugadores)


	def lanzarDadoPara(self , jugador):
		dado=randint(1,6)
		self.avanzarJugador(jugador, dado)
		return dado

	def activarEfectoPara(self , jugador):
		for e in self.efectos:
			if  e.incluyeA(jugador.posicion):
				e.aplicarEn(jugador)
				return e
				break

	def darTurno(self , jugador):
		jugador.turnos+=1

	def tieneTurno(self , jugador): 
			return jugador.turnos>=0

	def avanzarJugador(self ,jugador,pasos):
		pos = jugador.posicion+ pasos
		if pos >self.limite:
			pos=jugador.posicion-(pos-self.limite)
		jugador.posicion = pos
		return jugador.posicion

	def finalizar(self):
		self.activa=False

	def esta_activa(self):
		return self.activa
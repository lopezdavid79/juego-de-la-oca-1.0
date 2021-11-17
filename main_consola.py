import pdb
from sonido import reproducir_sonido
from funciones import configuracion_voces , say
from juego import Partida

dic_efectos={"oca": "el jugador cae en una casilla OCA  gana el derecho avanzar hasta la siguiente casilla OCA  ",
"puente" : "caes en una casilla PUENTE (6 y 12) hay que avanzar hasta la casilla POSADA (19) y se pierde un turno de tirar. La posada es para dormir, por supuesto" ,
"posada" : "Cuando el jugador cae directamente en la POSADA por el tiro del dado igualmente a dormir hasta el próximo turno." ,
"laberinto" : "Si tienes la terrible suerte de caer en la casilla LABERINTO (42) estarás obligado a retroceder hasta la casilla 30. ¡doce pasos de retroceso",
"carcel" : "Puede caer en la casilla CÁRCEL (56), suena mal, pero es una condena cortita, solo dos turnos sin jugar",
"infierno" : "También hay en el tablero una casilla del infierno llamada CALAVERA (58), la que tiene el efecto de hacer regresar a la casilla 1.",
"jardin_oca" : "ENTRAR AL JARDÍN DE LA OCA: (casilla 63) Al llegar aquí hay que esperar a tener el número exacto de pasos que permitan acceder. el exceso hay que retrocederlo" }


from jugador import Jugador


def crear_partida():
	partida = Partida()
	cantidad_jugadores = int(input('ingrese cantidadDeJugadores '))
	partida.cantidadDeJugadores= cantidad_jugadores 
	for c in range (partida.cantidadDeJugadores):
		name = input('ingrese nombre del jugador')
		jugador = Jugador(name)
		partida.agregarJugador(jugador)
	return partida

def jugar(partida):
	while partida.esta_activa():
		jugador = partida.jugadorActual()
		turno_juego= partida.tieneTurno(jugador)
		if   turno_juego:
			print(' Es el turno de {} turno {}'.format(jugador.nombre, jugador.turnos))
			posicion_inicial = jugador.posicion
			print('esta en el casillero ',posicion_inicial)
			dado = partida.lanzarDadoPara(jugador)
			
			# reproducir_sonido(sonido="dado.mp3")
			print('lanzo el dado  y le toco ...',dado)
			# reproducir_sonido(sonido="sonido\pasos.mp3")
			print('avanza  al casillero ',jugador.posicion)
			#depuración con python
			# pdb.set_trace()
			efecto = partida.activarEfectoPara(jugador)
			if efecto:
				print(str(efecto))
				string_efecto =str(efecto) 
				print(dic_efectos.get(string_efecto))
		else:
			print('{}  no puede tirar  '.format(jugador.nombre))
			partida.darTurno( jugador)

		partida.pasarTurno()
		
		input()
	return jugador.nombre 


#main
voice=configuracion_voces()
while True:
	# # reproducir_sonido(sonido="musica_fondo.mp3")
	texto='JUEGO DE LA OCA'
	say(voice ,texto)
	print('J- jugar y S-salir')
	op=input('ingrese opción')

	if op=="j":
		print('Es hora de jugar..')
		partida = crear_partida()		
		ganador=jugar(partida)
		print(f"el ganador es {ganador}")
		# reproducir_sonido(sonido="sonido\ganador.mp3")
		input()

	elif op=="s":
		break
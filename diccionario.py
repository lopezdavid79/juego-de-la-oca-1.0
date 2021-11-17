
dic_efectos={"oca": "el jugador cae en una casilla OCA  gana el derecho avanzar hasta la siguiente casilla OCA, y además puede repetir el tiro " ,
"puente" : "caes en una casilla PUENTE (6 y 12) hay que avanzar hasta la casilla POSADA (19) y se pierde un turno de tirar. La posada es para dormir, por supuesto" ,
"posada" : "Cuando el jugador cae directamente en la POSADA por el tiro del dado igualmente a dormir hasta el próximo turno." ,
"laberinto" : "Si tienes la terrible suerte de caer en la casilla LABERINTO (42) estarás obligado a retroceder hasta la casilla 30. ¡doce pasos de retroceso",
"carcel" : "Puede caer en la casilla CÁRCEL (56), suena mal, pero es una condena cortita, solo dos turnos sin jugar",
"infierno" : "También hay en el tablero una casilla del infierno llamada CALAVERA (58), la que tiene el efecto de hacer regresar a la casilla 1.",
"jardin_oca" : "ENTRAR AL JARDÍN DE LA OCA: (casilla 63) Al llegar aquí hay que esperar a tener el número exacto de pasos que permitan acceder. el exceso hay que retrocederlo" }

"""
for clave, valor in dic_efectos.items():
    print(clave, valor)
"""
# print(dic_efectos.get("puente"))
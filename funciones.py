import pyttsx3 as voz

#  Configuración de la voz 
def configuracion_voces():
	voice=voz.init()
	voices=voice.getProperty('voices')
	voice.setProperty('voice',voices[2].id)
	voice.setProperty('rate',110)
	voice.setProperty("volume",0.9)
	return voice

def say(voice , text):
	voice.say(text)
	voice.runAndWait()

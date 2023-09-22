def retirapontuacao (frase):
    """ literalmente retira a pontuação da frase
    str -> str"""
    frase=frase.replace("."," ")
	frase=frase.replace("/"," ")
	frase=frase.replace(";"," ")
	frase=frase.replace(","," ")
	frase=frase.replace(":"," ")
	frase=frase.replace("-"," ")
	frase=frase.replace("?"," ")
	frase=frase.replace("!"," ")
	return frase
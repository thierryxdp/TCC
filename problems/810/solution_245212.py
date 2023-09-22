def retira_pontuacao (frase):
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
def inverte(frase):
    """ retorna a mesma frase, sem pontuação, sem letras maiúsuculas, só que na ordem inversa
    str -> str"""
    retira_pontuacao(frase)
    str.lower(frase)
    str.split(frase)
    invertida = list(reversed(frase))
    return invertida
def retira_pontuacao (frase):
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
    """ inverte a frase
    str -> str"""
    frase=retira_pontuacao(frase)
    str.split(frase)
	return frase
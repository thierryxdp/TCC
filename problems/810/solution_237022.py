def retira_pontuacao(frase):
	resultado=frase.replace("-", " ").replace(";", " ").replace(",", " ").replace(":", " ").replace(".", " ").replace("!", " ").replace("?"," ")
	return resultado

def inverte(frase):
	fraseSeparada=retira_pontuacao(frase)
	fraseSplit=str.split(fraseSeparada)
	fraseInversa=fraseSplit[::-1]
	stringInversa=str.join(" ",fraseInversa)
	resultado=stringInversa
	return resultado
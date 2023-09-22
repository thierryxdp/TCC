def retira_pontuacao(frase):
	resultado=frase.replace("-", " ").replace(";", " ").replace(",", " ").replace(":", " ").replace(".", " ").replace("!", " ").replace("?"," ")
	return resultado
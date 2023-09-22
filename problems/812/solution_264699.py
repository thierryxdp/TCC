def retira_pontuacao(frase):
	str.join(frase," ")
	return frase.replace("-", " ").replace(",", " ").replace(":", " ").replace(";", " ").replace(".", " ").replace("?", " ").replace(",!", " ")
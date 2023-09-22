def conta_frases(frase):
	str.join(frase," ")
	return frase.replace("-", " ").replace(",", " ").replace(":", " ").replace(";", " ").replace(".", " ").replace("?", " ").replace("!", " ")
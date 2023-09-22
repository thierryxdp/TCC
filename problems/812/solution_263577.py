def retira_pontuacao(frase):
    p = string.punctuation
    for c in p:
    	frase = frase.replace(c, "")
	return s
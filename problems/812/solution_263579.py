def retira_pontuacao(frase):
    import string
    p = string.punctuation
    for c in p:
    	frase = frase.replace(c, "")
	return frase
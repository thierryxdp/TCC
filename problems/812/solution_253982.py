def retira_pontuacao(string):
    pontuacao = string.punctuation
    for i in pontuacao:
		frase = string.replace(i, " ")
		return frase
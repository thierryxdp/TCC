def retira_pontuacao(string):
    pontuacao = string.ponctuation
    for i in pontuacao:
		frase = string.replace(i, " ")
		return frase
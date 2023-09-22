def retira_pontuacao(frase):
    pontuacao = [',', '.', ';', ':', '!', '?', '-', '...']
    if pontuacao[0] in frase:
        frase = frase.replace(pontuacao[0], ' ')
	return frase
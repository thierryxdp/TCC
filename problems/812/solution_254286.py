def retira_pontuacao(frase):
    pontuacao = [',', '.', ';', ':', '!', '?', '-', '...']
    if pontuacao[0] in frase:
        frase = frase.replace(pontuacao[0], ' ')
    if pontuacao[1] in frase:
        frase = frase.replace(pontuacao[1], ' ')
	if pontuacao[2] in frase:
        frase = frase.replace(pontuacao[2], ' ')
	return frase
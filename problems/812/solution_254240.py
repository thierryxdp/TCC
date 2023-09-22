def retira_pontuacao(frase):
    pontuacao = (',', '.', ';', ':', '!', '?', '-', '...')
    for i in range(8):
        frase.replace(pontuacao[i], ' ')
	return frase
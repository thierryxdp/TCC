def retira_pontuacao(frase):
    pontuacao = (',', '.', ';', ':', '!', '?', '-', '...')
    for i in range(8):
        if pontuacao[i] in frase:
        	frase.replace(pontuacao[i], ' ')
	return frase
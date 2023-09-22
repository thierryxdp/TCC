def retira_pontuacao(frase):
    pontuacao = [',', '.', ';', ':', '!', '?', '-', '...']
    frase2 = ''
    if pontuacao[0] in frase:
        	frase2 = frase2 + frase.replace(pontuacao[0], ' ')
	return frase2
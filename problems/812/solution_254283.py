def retira_pontuacao(frase):
    pontuacao = [',', '.', ';', ':', '!', '?', '-', '...']
    if pontuacao[0] in frase:
        frase = frase.replace(pontuacao[0], ' ')
    if pontuacao[1] in frase:
        frase = frase.replace(pontuacao[1], ' ')
    if pontuacao[2] in frase:
        frase = frase.replace(pontuacao[2], ' ')
	if pontuacao[3] in frase:
        frase = frase.replace(pontuacao[3], ' ')
    if pontuacao[4] in frase:
        frase = frase.replace(pontuacao[4], ' ')
    if pontuacao[5] in frase:
        frase = frase.replace(pontuacao[5], ' ')
    if pontuacao[6] in frase:
        frase = frase.replace(pontuacao[6], ' ')
    if pontuacao[7] in frase:
        frase = frase.replace(pontuacao[7], ' ')
	return frase
def retira_pontuacao(frase):
    pont_in_frase = ''
    pontuacao = [',', '.', ';', ':', '!', '?', '-', '...']
    for i in range (8):
        if pontuacao[i] in frase:
            pont_in_frase = pont_in_frase + pontuacao[i]
	frase = frase.replace(pont_in_frase, ' ')
    return frase
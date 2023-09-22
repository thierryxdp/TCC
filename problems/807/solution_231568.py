def conta_frases(texto):
    ''' ;
    str => int'''
    pontuacao = "-,: ; !?."
	for x in range(len(pontuacao)):
        texto = len(texto.split(pontuacao[x]))
    return texto
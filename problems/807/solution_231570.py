def conta_frases(texto):
    ''' ;
    str => int'''
    pontuacao = "...!?."
	for pontuacao in range(len(texto)):
        texto = len(texto.split(str(pontuacao)))
    return texto
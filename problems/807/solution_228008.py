def conta_frases(frases):
    '''Recebe uma quantidade x de frases e retorna
    a quantidade.
    string -> int'''
    l_frases = []
	
    if '.' in frases:
        ponto = frases.index('.')
        ponto_final = frases[:ponto]
        l_frases += [ponto_final]
        return l_frases
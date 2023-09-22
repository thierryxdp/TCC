def conta_frases(frases):
    '''Recebe uma quantidade x de frases e retorna
    a quantidade.
    string -> int'''
    l_frases = []
	
    if '.' in frases:
        ponto = frases.index('.')
        ponto_final = frases[:ponto]
        l_frases += [ponto_final]
    
    if ',' in frases:
        virgula = frases.rindex(',')
        virgula_final = frases[ponto:virgula]
        return virgula_final
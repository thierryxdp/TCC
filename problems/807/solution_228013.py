def conta_frases(frases):
    '''Recebe uma quantidade x de frases e retorna
    a quantidade.
    string -> int'''
    l_frases = []
	qt_frases = []
    if '.' in frases:
        ponto = frases.index('.')
        ponto_final = frases[:ponto]
        l_frases += [ponto_final]
    	qt_frases += [l_frases]
    if ',' in frases:
        virgula = frases.rindex(',')
        virgula_final = frases[ponto:virgula]
        qt_frases += [virgula_final]
	
    return len(qt_frases)
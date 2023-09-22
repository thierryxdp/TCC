def conta_frases(frases):
    '''Recebe uma quantidade x de frases e retorna
    a quantidade.
    string -> int'''
    l_frases = []
    l_frases += [frases]
    qt_frases = []
	if '!?...' or '.' in l_frases:
        qt_frases += l_frases
        return qt_frases
def conta_frases(frases):
    '''Recebe uma quantidade x de frases e retorna
    a quantidade.
    string -> int'''
	qt_frases = []
    
    if '.' in frases:
        qt_frases += [frases]
        del qt_frases[frases-1:]
        return len(qt_frases)
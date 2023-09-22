def conta_frases(frases):
    '''Recebe uma quantidade x de frases e retorna
    a quantidade.
    string -> int'''
    l_frases = []
    l_frases += [frases]
    qt_frases = len(l_frases)
    if '!' or '?' or '...' or '.' in qt_frases:
        return del qt_frases
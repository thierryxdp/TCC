def conta_frases(frases):
    '''Recebe uma quantidade x de frases e retorna
    a quantidade.
    string -> int'''
    l_frases = []
    ponto_final = frases.index('.')
    virgula = frases.rindex(',')
    exclamação = frases.rindex('!')


    if '.' in frases:
        ponto = frases[:ponto_final]
        virgula = frases[ponto_final:]
        exclamação = frases[ponto_final:exclamação]
        l_frases += [ponto]
        return l_frases
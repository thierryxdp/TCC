def freq_palavras(frases):
    ''' 
    '''
    palavras = frases.split()
    dicio = {}
    for palavras in frases:
        dicio[palavras] = frases.count(frases[0])
    return dicio
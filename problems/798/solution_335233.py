def freq_palavras(frases):
    ''' 
    '''
    palavras = frases.split()
    dicio = {}
    for palavra in frases:
        dicio[palavra] = frases.count(frases[0])
    return dicio
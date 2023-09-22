def freq_palavras(frases):
    ''' 
    '''
    palavras = frases.split()
    dicio = {}
    for palavra in palavras:
        dicio[palavra] = frases.count(palavra)
    return dicio
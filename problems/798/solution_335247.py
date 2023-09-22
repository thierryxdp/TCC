def freq_palavras(frases):
    ''' 
    '''
    palavras = frases.split()
    i = 0
    dicio = {}
    for palavra in palavras:
        dicio[palavra] = frases.count(palavra)
        i = i + 1
    return dicio
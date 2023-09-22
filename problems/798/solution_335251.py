def freq_palavras(frases):
    ''' 
    '''
    palavras = frases.split()
    dicio = {}
    for palavra in palavras:
        dicio[palavra] = palavras.count(palavra)
    return dicio
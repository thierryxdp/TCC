def conta_frases(texto):
    '''Essa função retorna o numero de frases de um texto'''
    frase=len(str.join(texto,'.'))+len(str.join(texto,'...'))+len(str.join(texto,'!'))+len(str.join(texto,'?'))
    return frase
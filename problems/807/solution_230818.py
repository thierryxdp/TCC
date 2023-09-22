def conta_frases(texto):
    '''Essa função retorna o numero de frases de um texto'''
    frase=len(str.split(texto,'.'))+len(str.split(texto,'...'))+len(str.split(texto,'!'))+len(str.split(texto,'?'))
    return frase
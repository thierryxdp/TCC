def conta_frases(texto):
    '''Define o número total de frases no texto
    str -> int'''
    return str.count(texto, '. ') + str.count(texto, '!') + str.count(texto, '?') + str.count(texto, '...')
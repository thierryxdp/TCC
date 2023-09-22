def conta_frases(texto):
    '''Dado um texto, conta o número de frases dele
    str -> int'''
    num_frases = str.count(texto, '...') + str.count(texto, '!') + str.count(texto, '?') + str.count(texto, '.')
    return num_frases
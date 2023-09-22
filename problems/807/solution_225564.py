def conta_frases(texto):
    '''Essa função recebe um texto e conta o número de frases contidas nele
    str -> int'''
    pf = str.count(texto, '.')
    pe = str.count(texto, '!')
    pi = str.count(texto, '?')
    re = str.count(texto, '...')
    return pf + pe + pi + re
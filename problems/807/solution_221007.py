def conta_frases(texto):
    '''dado um texto(texto), retorna o numero de frases contidas nele; str -> int'''
    A = str.count(texto, '...')
    B = str.count(texto, '.')
    C = str.count(texto, '!')
    D = str.count(texto, '?')
    T = A + (B - (3*A)) + C + D
    return T
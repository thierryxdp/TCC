def conta_frases (texto):
    '''função que retorna a quantidade de frases na string passada; str -> int'''
    k = '.'
    l = '!'
    m = '?'
    n = '...'
    return str.count(texto, k) + str. count(texto, l) + str.count(texto, m) + str.count(texto, n)
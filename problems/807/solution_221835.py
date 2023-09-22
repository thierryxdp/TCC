def conta_frases (texto):
    '''função que retorna a quantidade de frases na string passada; str -> int'''
    k = '.'
    l = '!'
    m = '?'
    n = '...'
    if 2*n in texto:
        return str.count(texto, k) + str. count(texto, l) + str.count(texto, m) + str.count(texto, n) - 6
    if n in texto:
        return str.count(texto, k) + str. count(texto, l) + str.count(texto, m) + str.count(texto, n) - 3
    else:
        return str.count(texto, k) + str. count(texto, l) + str.count(texto, m)
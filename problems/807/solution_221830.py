def conta_frases (texto):
    '''função que retorna a quantidade de frases na string passada; str -> int'''
    k = '.'
    l = '!'
    m = '?'
    n = '...'
    x = [1,2,3,4,5,6]
    if x*n in texto:
        return str.count(texto, k) + str. count(texto, l) + str.count(texto, m) + str.count(texto, n) - x*3
    else:
        return str.count(texto, k) + str. count(texto, l) + str.count(texto, m)
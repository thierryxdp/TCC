def conta_frases (texto):
    '''função que retorna a quantidade de frases na string passada; str -> int'''
    k = '.'
    l = '!'
    m = '?'
    n = '...' 
    a = str.count(texto, k)
    b = str.count(texto, l)
    c = str.count(texto, m)
    d = str.count(texto, n)
    if n in texto:
        return a + b + c + d - 3*n
    else:
        return a + b + c + d
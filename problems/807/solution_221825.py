def conta_frases (texto):
    '''função que retorna a quantidade de frases na string passada; str -> int'''
    k = '.' or '!' or '?' or '...'
    return str.count(texto, k)
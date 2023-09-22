def conta_frases(texto):
    '''Retorna a quantidade de frases de um determinado texto
    str -> int'''
    return len(str.split(texto,'!'))
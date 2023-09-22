def conta_frases(texto):
    '''Funcao que dado determinado texto, retornará a quantidade de frases que o texto tem. str -> int'''
    t=texto
    return t.count('.')+t.count('!')+t.count('?')
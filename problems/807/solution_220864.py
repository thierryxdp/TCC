def conta_frases(texto):
    '''Funcao que dado determinado texto, retornará a quantidade de frases que o texto tem. str -> int'''
    t=texto
    x=t.replace("..", "/")
    return x.count('.')+x.count('!')+x.count('?')
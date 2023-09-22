def conta_frases(x):
    '''Retorna a quantidade de frases de um período definido por uma string. str->int'''
    return (x.count('.')+x.count('!')+x.count('...')+x.count('?'))
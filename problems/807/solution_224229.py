def conta_frases(x):
    '''Retorna a quantidade de frases de um período definido por uma string. str->int'''
    y=(x.count('.')+x.count('!')+x.count('...')+x.count('?'))
    if x.count('...')==1:
        y=y-3
    else:
        return y
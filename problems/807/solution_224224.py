def conta_frases(x):
    '''Retorna a quantidade de frases de um período definido por uma string. str->int'''
    y=(x.count('.')+x.count('!')+x.count('...')+x.count('?'))
    if x.count('...')=1:
        y=y-1
    if x.count('...')=2:
        y=y-2
    else:
        return y
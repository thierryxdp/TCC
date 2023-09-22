def fatorial(n):
    '''Funcao que calcula e retorna o fatorial de n.
    int->int'''
    x=list(range(1,n+1))
    y=1
    z=x[0]
    while y<len(x):
        z=z*x[y]
        y=y+1
    return z
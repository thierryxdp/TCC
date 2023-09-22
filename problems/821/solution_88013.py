def fatorial(x):
    '''Retorna o fatorial de um número.
    int -> int'''
    while x!=1:
        x=x*(x-1)
    return x
def fatorial(n):
    '''Dado um número n, retorna o seu fatorial'''
    '''int->int'''
    fatorial=n
    while n>1:
        fatorial=fatorial*(n-1)
        n=n-1
    return fatorial
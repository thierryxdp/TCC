def fatorial(n):
    '''Essa função calcula o fatorial de um número n,
    int->int'''
    fatorial=1
    while n>1:
        fatorial*=n
        n-=1
    return fatorial
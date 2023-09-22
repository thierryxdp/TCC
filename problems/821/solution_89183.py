def fatorial(n):
    '''Funcao que calcula o fatorial de um dado
    numero n; int -> int'''
    f = 0
    i = n-1
    while i>0:
        f += n * i
        n -= 1
        i -= 1
    return f
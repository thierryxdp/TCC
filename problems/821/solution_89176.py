def fatorial(n):
    '''Funcao que calcula o fatorial de um dado
    numero n; int -> int'''
    f = 0
    i = n
    while i>0:
        f += n * i
        i -= 1
    return f
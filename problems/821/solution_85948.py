def fatorial(n):
    '''Dado um número n retorna seu fatorial
    int -> int'''
    p = 1
    f = 1
    while p <= n:
        f *= p
        p += 1
    return f
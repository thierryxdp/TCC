def fatorial(n):
    '''Dado um número, retorna o fatorial desse número.
    int --> int'''
    a = 0
    b = 1
    c = 1
    proximo = 0
    while proximo < n:
        a = b*c
        b = b+1
        c = a
        proximo = proximo + 1
    return a
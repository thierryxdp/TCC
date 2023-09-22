def fatorial(n):
    '''Dado um número, calcula sua fatorial.
    int -> int'''
    i = 1
    fator = 1
    while i <= n:
        fator *= i
        i = i + 1
    return fator
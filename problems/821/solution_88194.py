def fatorial(n):
    '''Dado um numero(n), calcula o fatorial do mesmo. int->int'''
    i = 1
    while n > 0:
        i = i * n
        n = n - 1
    return i
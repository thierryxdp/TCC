def fatorial(n):
    '''retorna o fatorial de n
    int->int'''
    numero = 1
    while n >= 1:
        numero = numero * n
        n = n - 1
    return numero
def fatorial(n):
    ''' retorna o fatorial do numero n informado
    int -> int'''
    numero = 1
    while n >= 1:
        numero = numero * n
        n = n - 1
    return numero
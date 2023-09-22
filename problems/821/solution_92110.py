def fatorial(n):
    ''' funcao que calcula o fatorial desse numero. int -> int'''
    fatorial = 0
    while n >= 1:
        fatorial += n*(n-1)
        n -= 1
    return fatorial
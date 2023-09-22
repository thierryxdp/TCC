def fatorial (n):
    """ Insira um numero para que a função retorne o fatorial desse numero"""
    N = n-1
    while N>0:
        n = n*N
        N += -1
    return n
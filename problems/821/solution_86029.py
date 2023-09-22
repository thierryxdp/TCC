def fatorial(n):
    '''dado um numero n, calcula o fatorial desse número'''
    produto = 1
    while n-1 != 0:
        produto = produto * n
        n = n - 1
    return produto
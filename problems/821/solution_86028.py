def fatorial(n):
    '''dado um numero n, calcula o fatorial desse número'''
    fatorial = 1
    while n-1 != 0:
        fatorial = fatorial * (n*(n-1))
        n-1 = n-2
    return fatorial
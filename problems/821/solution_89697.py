def fatorial(n):
    '''recebe um numero e retorna seu fatorial'''
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
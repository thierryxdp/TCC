def fatorial(n):
    '''funcao que dado um numero, retorne o fatorial do mesmo. Int->int.'''
    m = 1
    while n >= 1:
        m = m * n
        n = n - 1
    return m
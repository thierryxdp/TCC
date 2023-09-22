def fatorial(n):
    ''' Retorna o fatorial de um numero'''
    if n < 2:
        return 1
    else:
        return n * fatorial(n-1)
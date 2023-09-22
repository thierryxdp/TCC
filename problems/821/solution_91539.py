def fatorial(n):
    '''Caalcula o fatorial de um número.
    int->int'''
    i=n
    while n>=0:
        result = result*(n-1)
        i=i-1
    return result
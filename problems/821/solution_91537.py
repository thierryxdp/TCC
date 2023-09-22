def fatorial(n):
    '''Caalcula o fatorial de um número.
    int->int'''
    result=n
    while n>0:
        result = result*(n-1)
        n=n-1
    return result
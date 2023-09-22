def fatorial(n):
    '''Caalcula o fatorial de um número.
    int->int'''
    i=n
    result=n
    while n>0:
        result = result*(i-1)
        n=n-1
    return result
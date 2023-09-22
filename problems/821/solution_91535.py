def fatorial(n):
    '''Caalcula o fatorial de um número.
    int->int'''
    result=n
    i=n
    while n>0:
        result = result*(i-1)
        i=n-1
    return result
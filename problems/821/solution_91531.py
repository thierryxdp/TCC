def fatorial(n):
    '''Caalcula o fatorial de um número.
    int->int'''
    result=0
    i=n
    while i>0:
        result = i*i-1
        i=n-1
    return result
def fatorial(n):
    '''Calcula o fatorial de um número.
    int->int'''
    i=n
    result=n
    while n>0:
        result=result*(n-i)
        i=i-1
    return result
def fatorial(n):
    '''Calcula o fatorial de um número.
    int->int'''
    i=0
    result=n
    while i<n:
        result=result*(n-1)
        n=n+1
    return result
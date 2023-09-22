def fatorial(n):
    '''Calcula o fatorial de um número.
    int->int'''
    i=0
    result=1
    while i<=n:
        result=result*(n-1)*(n-2)
        i=i+1
    return result
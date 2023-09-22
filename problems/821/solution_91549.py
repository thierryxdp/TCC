def fatorial(n):
    '''Calcula o fatorial de um número.
    int->int'''
    i=0
    result=1
    while i<=n:
        result=result*(i+1)
        i=i+1
    return result
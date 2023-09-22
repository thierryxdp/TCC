def fatorial(numero):
    '''Dado um número, retorna o fatorial desse número
    int->int'''
    n=numero
    fat=0
    while n>1:
        fat=fat+(n*(n-1))
    n=n-1    
    return fat
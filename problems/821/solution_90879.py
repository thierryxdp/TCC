def fatorial(numero):
    '''Dado um número, retorna o fatorial desse número
    int->int'''
    n=numero
    fat=0
    while n>1:
        a=n*(n-1)
        fatorial=fatorial+a
    n=n-1    
    return fatorial
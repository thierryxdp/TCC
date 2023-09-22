def fatorial(numero):
    '''Dado um número, retorna o fatorial desse número
    int->int'''
    n=numero
    fat=0
    while n!=1:
        mult=n*(n-1)
        fat=fat+mult
    n=n-1    
    return fat
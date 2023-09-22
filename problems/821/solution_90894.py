def fatorial(n):
    '''Dado um número, retorna o fatorial desse número
    int->int'''
    fat=1
    while n!=1:
        fat=fat*n
        n=n-1    
    return fat
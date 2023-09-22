def fatorial(n):
    '''
    função que dado um número n, calcula o fatorial desse número
    int->
    '''  
    fatorial = None
    while n >= 2:
    anterior = n-1    
        fatorial = n*anterior
    n -= 1
    return n
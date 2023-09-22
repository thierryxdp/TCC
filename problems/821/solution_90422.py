def fatorial(n):
    '''
    função que dado um número n, calcula o fatorial desse número
    int->
    '''  
    fatorial = None
    anterior = n-1 
    while n >= 1:
        fatorial = n*anterior
    n -= 1
    anterior -= 1
    return n
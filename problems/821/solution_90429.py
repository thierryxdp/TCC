def fatorial(n):
    '''
    função que dado um número n, calcula o fatorial desse número
    int->
    '''  
    mult= None
    
    while n >= 1:
        mult = n*(n-1)
        fato = mult*n*(n-1)
        n -= 1
    
    return fato
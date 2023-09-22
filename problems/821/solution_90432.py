def fatorial(n):
    '''
    função que dado um número n, calcula o fatorial desse número
    int->
    '''  
    mult= 1
    numero = n
    
    while n >= 1:
        mult *= mult*n
        n -= 1
        
    
    
    return mult
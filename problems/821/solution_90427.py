def fatorial(n):
    '''
    função que dado um número n, calcula o fatorial desse número
    int->
    '''  
    mult= None
    anterior = n-1 
    while n >= 1:
        mult = n*anterior
        n -= 1
        anterior -= 1
    mult = mult*n*anterior
    
    return mult
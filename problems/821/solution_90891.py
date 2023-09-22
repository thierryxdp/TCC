def fatorial (numero):
    ''' função que calcula e retorna o fatorial do número dado
    int->int'''
    
    n = 1
    
    while n > 0:
        n = numero *n
        n= n-1
        
    return n
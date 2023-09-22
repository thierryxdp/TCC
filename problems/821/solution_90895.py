def fatorial (numero):
    ''' função que calcula e retorna o fatorial do número dado
    int->int'''
    
    n = 1
    
    while n >= 1:
        n = numero *n
        numero= numero-1
        
    return n
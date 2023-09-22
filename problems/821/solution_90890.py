def fatorial (numero):
    ''' função que calcula e retorna o fatorial do número dado
    int->int'''
    
    n = numero
    
    while n > 0:
        numero = numero *n
        n= n-1
        
    return n
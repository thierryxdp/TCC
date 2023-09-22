def fatorial (numero):
    ''' função que calcula e retorna o fatorial do número dado
    int->int'''
    
    n = numero
    resultado = 1
    
    while n > 0:
        resultado = numero *n*resultado
        n= n-1
        
    return resultado
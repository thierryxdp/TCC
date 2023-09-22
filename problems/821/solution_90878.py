def fatorial (numero):
    ''' função que calcula e retorna o fatorial do número dado
    int->int'''
    
    n = numero
    resultado = 1
    
    while n > 0:
        resultado = resultado + (numero *n)
        n= n-1
        
    return resultado
def fatorial(x):
    '''retorna o fatorial do número dado como entrada;
    int -> int'''
    
    resultado = 1
    proximo = 1
    
    while proximo < x:
        resultado += resultado * proximo
        proximo += 1
        
    return resultado
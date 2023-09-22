def fatorial(n):
    '''Funcao que dado um numero, calcula o fatorial deste numero.
    int -> int'''
    
    i = 1
    resultado = 1
    
    while i <= n:
        resultado = resultado * i
        
        i += 1
        
    return resultado
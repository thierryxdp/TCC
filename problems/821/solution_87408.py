def fatorial(num):
    '''Esta função calcula o fatorial do número (num)
    inserido.
    int -> int'''
    
    multiplicador=1
    resultado=1
    
    while multiplicador<=num:
        resultado=multiplicador*resultado
        
        multiplicador=multiplicador + 1
    
    return resultado
def fatorial(numero):
    """recebe um numero inteiro e retorna seu fatorial
    int -> int"""
    
    i = 1
    fatorial = numero
    
    while i != numero:
        fatorial *= numero - i
        i += 1
        
    return fatorial
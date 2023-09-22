def fatorial(numero):
    
    valor = 1
    
    while numero != 0:
        
        valor *= numero
        numero -= 1
        
    return valor
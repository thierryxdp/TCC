def fatorial(num):
    ''' funçao que dada um número inteiro retorna seu fatorial;
    int --> float'''
    i = 0
    resultado = 1
    
    while i<num:
        i = i + 1
        resultado = resultado * i 
    
    return resultado
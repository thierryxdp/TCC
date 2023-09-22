def fatorial(numero):
    '''Calcula o fatorial de um número dado;
    int -> int'''
    
    fator = 1
    resultado = 1
    
    while fator < numero:
        if numero == 0:
            return 1
        
        resultado *= fator
        fator += 1
    return resultado
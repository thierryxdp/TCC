def fatorial(n):
    ''' Calcula o fatorial do numero n dado como entrada;
    int -> int '''
    
    fator = 1
    fatorial = 1
    
    while fator < n: 
    
        fatorial = fatorial * (fator + 1)
        fator = fator + 1
        
    return fatorial
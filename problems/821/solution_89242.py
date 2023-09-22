def fatorial(n):
    ''' Função que calcula fatorial de um dado número
        int -> int '''
    
    fatorial = 1
    antes = n-1 
    
    while (antes) != 0: 
        fatorial = n*antes
        antes = antes - 1
        
    return fatorial
def fatorial(numero):
    ''' Entrada: numero -> numero o qual terá seu fatorial 
    			 calculado, int
        
        Saída: retorna o fatorial do número indicado, int
        
        int-> int'''
    i = 0
    fatorial = 1
    numero2 = numero
    while i < numero:
        fatorial = fatorial*numero2
        numero2 = numero2 - 1
        i = i+ 1
    return fatorial
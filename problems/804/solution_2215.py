def filtra_pares(t):
    
    """ função que retorna uma tupla apenas com os números pares da tupla de entrada 
    
    Parâmetros:
    	tipo tupla(int)
        Tupla com quatro elementos inteiros
        
        
    Retorna:
    	tupla 
        Números pares da tupla original
        
    """

    
    s = int(t[0])
    b = int(t[1])
    p = int(t[2])
    c = int(t[3])
    tupla = ()

    if s%2 ==0:
        tupla = tupla + (s,)

    if b%2 ==0:
        tupla = tupla + (b,)

    if p%2 ==0:
        tupla = tupla + (p,)

    if c%2 ==0:
        tupla = tupla + (c,)

    return tupla
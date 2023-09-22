def filtra_pares(x):
    """Funçao que recebe uma tupla com quatro elementos inteiros como parametro e retorna uma nova tupla contendo apenas os elementos pares da tupla original"""
    y = ()
    
    if ( x[0] % 2 ) == 0:
        y = y + (x[0],)
        
    if ( x[1] % 2 ) == 0:
        y = y + (x[1],)
        
    if ( x[2] % 2 ) == 0:
        y = y + (x[2],)
       
    if ( x[3] % 2) == 0:
        y = y + (x[3],)
        
    return y
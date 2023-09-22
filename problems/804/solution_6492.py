def filtra_pares(x):
    '''Função que recebe uma tupla com 4 elementos inteiros e retorna uma nova tupla contendo apenas elementos pares'''
   
    y = ()
    
    if ( x[0] % 2 )  == 0:
        y = y + (x[0],)
    
    if ( x[1] % 2 ) == 0:
        y = y + (x[1],) 
        
    if ( x[2] % 2 ) == 0:
        y = y + (x[2],)
        
    if ( x[3] % 2 ) == 0:
        y = y + (x[3],)
        
    return y
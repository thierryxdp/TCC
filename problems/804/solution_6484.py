def filtra_pares(x):
    '''Função que recebe uma tupla com 4 elementos inteiros e retorna uma nova tupla contendo apenas elementos pares'''
   
	x1,x2,x3,x4 = x
    
    if ( x1 % 2 )  == 0:
        y = (x1,)
        
    if ( x2 % 2 ) == 0:
        y = y[1:] + (x2,) 
        
    if ( x3 % 2 ) == 0:
        y = y[1:] + (x3,)
        
    if ( x4 % 2 ) == 0:
        y = y[1:] + (x4,)
        
        
    return y
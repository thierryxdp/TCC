def eh_quadrada(matriz):
    '''Verifica e retorna em booleano se uma matriz é
       quadrada ou não;
       list -> bool'''
    
    if len(matriz) == 0:
        
        return True
    
    elif len(matriz) == len(matriz[0]):
        
        return True
    
    else:
        
        return False
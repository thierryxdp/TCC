def eh_quadrada(m):
    '''Função que identifica se uma matriz(entrada) é quadrada. Retornando 
um booleano'''
    
    if len(m) == 0:
        
        return True

      
    if len(m) == len(m[0]):
       
        return True
    
    
    return False
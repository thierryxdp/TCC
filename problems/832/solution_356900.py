def eh_quadrada(matriz:list)->bool:

    """ Função que receb uma matriz como entrada matriz e retorna
        se é quadrada ou não. """
    
 
    if matriz == []:
        
        return True
        
    elif len(matriz) == len(matriz[0]):
        
        return True
    
    else:
        
        return False
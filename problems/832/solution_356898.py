def eh_quadrada(matriz:list)->bool:

    """ Função que receb uma matriz como entrada matriz e retorna
        se é quadrada ou não. """
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    if matriz == []:
        
        return True
    
    
    elif nlinhas == ncolunas:
        
        return True
    
    else:
        
        return False
def eh_quadrada(matriz: list):
    """ recebe uma matriz no formate de lista, identifica e retorna se ela é quadrada
    em booleano """
    
    if matriz == []:
        return True
    
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False
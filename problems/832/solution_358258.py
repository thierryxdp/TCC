def eh_quadrada(matriz):
    """ Funcao que recebe uma matriz.
    	Retorna se uma matriz é quadrada;
        list -> bool
    """
    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    
    return False
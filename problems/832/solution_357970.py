def eh_quadrada(matriz):
    """ Identifica se a matriz é quadrada.
    	list -> bool
        
        Parameter:
        matriz: Matriz em formato de uma lista de listas.
        
        Returns:
        True se a matriz for quadrada e False caso contrário.
    """
    if len(matriz) == len(matriz[0]) or matriz == []:
        return True
    else:
        return False
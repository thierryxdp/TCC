def eh_quadrada(matriz):
    """Calcula e retorna se uma matriz é quadrada""" 
    if matriz == [] or len(matriz) == len(matriz[0]):
        return True 
    else: 
        return False
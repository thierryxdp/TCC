def eh_quadrada(matriz:list) ->bool:
    """Recebe uma matriz e informa se ela é quadrada ou não."""
    if matriz == [] or len(matriz) == len(matriz[0]):
        return True
    else:
        return False
def eh_quadrada (matriz):
    """idetifica se a matriz é quadrada. matriz -> bool"""
    if matriz == []:
        return True
    if len(matriz) < len(matriz[0]) or len(matriz) > len(matriz[0]):
        return False
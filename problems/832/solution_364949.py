def eh_quadrada (matriz):
    """idetifica se a matriz é quadrada. matriz -> bool"""
    if matriz == []:
        return true
    if len(matriz) != len(matriz[0]):
        return false
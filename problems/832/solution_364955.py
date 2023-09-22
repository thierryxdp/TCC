def eh_quadrada (matriz):
    """idetifica se a matriz é quadrada. matriz -> bool"""
    if len(matriz) == len(matriz[0]):
        return True
    if len(matriz) > len(matriz[0]) or len(matriz) < len(matriz[0]):
        return False
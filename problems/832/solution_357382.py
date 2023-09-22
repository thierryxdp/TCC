def eh_quadrada(matriz):
    """Função booleana que identifica se uma matriz é quadrada.
    list -> bool"""
    if len(matriz) == 0:
        return True
    
    return len(matriz) == len(matriz[0])
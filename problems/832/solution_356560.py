def eh_quadrada(matriz):
    """Essa função retoena true se é uma matriz quadrada ou false se não for"""
    """list->bool"""
    if len(matriz) == 0 or len(matriz[0]) == len(matriz):
        return True
    else:
        return False
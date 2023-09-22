def eh_quadrada(matriz):
    """funcao que identifica se uma matriz eh quadrada ou nao. list->bool"""
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False
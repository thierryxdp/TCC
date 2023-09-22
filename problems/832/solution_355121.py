def eh_quadrada(matriz):
    """função que retorna True se a matriz de entrada é quadrada e False caso contrário
    list->bool"""
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False
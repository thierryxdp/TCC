def eh_quadrada(matriz):
    """retorna se a matriz é quadrada ou nao
    list->bool"""
    if len(matriz)==0:
        return True
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False
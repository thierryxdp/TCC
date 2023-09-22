def eh_quadrada(matriz):
    """Recebe uma matriz e retorna True se for quadrada ou False senão for/list->bool"""
    if len(matriz)==0:
        return True
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False
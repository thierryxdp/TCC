def eh_quadrada(matriz):
    """Funcao que retorna se uma matriz é quadrada"""
    x = len(matriz)
    y = list.pop(matriz, 0)
    z = len(y)
    if x == z:
        return True
    if x == 0:
        return True
    else:
        return False
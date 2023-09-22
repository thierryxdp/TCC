def eh_quadrada(matriz):
    """Funcao que retorna se uma matriz é quadrada"""
    x = len(matriz)
    y = matriz[0:1]
    z = len(y)
    if x == z:
        return True
    else:
        return False
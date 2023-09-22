def eh_quadrada(matriz):
    """Funcao que retorna se uma matriz é quadrada"""
    y = matriz[0:1]
    x = len(matriz)
    z = len(y)
    if x == z:
        return True
    else:
        return False
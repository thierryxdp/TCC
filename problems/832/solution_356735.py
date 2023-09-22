def eh_quadrada(matriz):
    """ retorna se a matriz e quadrada
    list --> str"""
    quadrada = True
    if len(matriz) != 0:
        if len(matriz) != len(matriz[0]):
            quadrada = False
    return qudrada
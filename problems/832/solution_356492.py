def eh_quadrada(matriz):
    """ retorna se a matriz e quadrada
    list --> str"""
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False
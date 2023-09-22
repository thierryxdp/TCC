def eh_quadrada(matriz):
    """ Essa função retorna um valor booleano para matrizes que são quadradas.
    Como entrada temos uma matriz e como saída temos um valor booleano;
    list->bool"""
    if matriz==[]:
        return True
    else:
        if len(matriz)==len(matriz[0]):
            return True
        else:
            return False
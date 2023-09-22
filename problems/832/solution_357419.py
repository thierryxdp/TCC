def eh_quadrada(matriz):
    """Dada uma matriz retorna um valor booleano
    se essa matriz é uma matriz quadrada."""
    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False
def eh_quadrada (matriz):
    """Função que dado uma matriz retorne se ela é quadrada ou não.
    lista -> bool"""

    if matriz == []:
        return True

    return len(matriz) == len(matriz[0])
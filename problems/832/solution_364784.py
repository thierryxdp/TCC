def eh_quadrada(matriz):
    """
    função que recebe uma matriz e veriifica se é uma matriz 
    quadrada, ou seja, uma matriz vazia, sem nenhuma linha ou 
    coluna.
    :param matriz: list
    :return: bool 
    """
    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz[linha])):
            if len(matriz) == len(matriz[linha]) and len(matriz[coluna]):
                return True

            else:
                return False

    return True
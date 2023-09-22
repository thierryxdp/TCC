def eh_quadrada(matriz):
    """
    lista->bool
    :param matriz: Recebe uma matriz 
    :param return: Retorna se ela é quadrada
    """
    if coluna == 0:
        return True
    linha = len(matriz)
    coluna = len(matriz[0])
    elif linha == coluna:
        return True
    else:
        return False
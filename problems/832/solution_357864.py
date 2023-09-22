def eh_quadrada(matriz):
    """
    lista->bool
    :param matriz: Recebe uma matriz 
    :param return: Retorna se ela é quadrada
    """
    linha = len(matriz)
    coluna = len(matriz[0])
    if linha == coluna:
        return True
    elif linha == 0:
    	return True
    else:
        return False
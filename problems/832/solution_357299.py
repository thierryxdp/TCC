def eh_quadrada(matriz):
    """Esta funcao identificar se uma matriz é quadrada."""
    linha = len(matriz)
    coluna = len(matriz[])
    for i in matriz:
        if linha == coluna:
            return True
        else:
            return False
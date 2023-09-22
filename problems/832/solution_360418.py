def eh_quadrada(matriz):
    """retorna se uma matriz é quadrada ou não
    list->bool"""
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in matriz:
        if linha == coluna:
            return True
        else:
            return False
    else matriz[][]:
        return True
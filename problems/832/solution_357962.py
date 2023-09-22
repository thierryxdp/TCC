def eh_quadrada(matriz):
    if len(matriz) == 0:
        return True
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in matriz:
        if linha == coluna:
            return True
        else:
            return False
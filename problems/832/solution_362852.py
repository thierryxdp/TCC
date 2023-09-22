def eh_quadrada(matriz):
    linha = len(matriz)
    coluna = len(matriz[0])
    if linha == coluna:
        return True
    elif linha != coluna:
        return False
    elif matriz == []:
        return True
def eh_quadrada(matriz):
    linha = len(matriz)
    coluna = len(matriz[0])
    if matriz==[]:
        return True
    if linha==coluna:
        return True
    else:
        return False
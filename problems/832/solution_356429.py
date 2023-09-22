def eh_quadrada(matriz):
    linha = len(matriz)
    coluna = len(matriz[0])
    if (linha+coluna)==0:
        return True
    if linha==coluna:
        return True
    else:
        return False
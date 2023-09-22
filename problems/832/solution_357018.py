def eh_quadrada(matriz):
    linha = len(matriz)
    coluna = len(matriz[0])
    if linha == coluna or coluna == 0:
        return True
    else:
        return False
def eh_quadrada(matriz):

    linha = len(matriz)
    coluna = len(matriz[0])
    for i in matriz:
        if linha == coluna or linha == coluna == 0:
            return True
        else:
            return False
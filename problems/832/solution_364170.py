def eh_quadrada(matriz):
    '''função que identifica se uma matriz é
    quadrada ou não'''

    linha = len(matriz)
    coluna = len(matriz[0])
    for i in matriz:
        if linha == coluna:
            return True
        else:
            return False
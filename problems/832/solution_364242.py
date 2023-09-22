def eh_quadrada(matriz):
    '''
    '''
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in matriz:
        if linha == coluna:
            return True
        elif matriz == []:
            return True
        else:
            return False
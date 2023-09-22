def eh_quadrada(matriz):
    '''identifica se uma matriz é quadrada'''
    '''list(list) -> bool'''
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in matriz:
        if linha == coluna:
            return True
        elif linha == []:
            return True
        else:
            return False
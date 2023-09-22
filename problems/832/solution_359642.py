def eh_quadrada(matriz):
    '''Função que inidca se uma matriz e quadrada ou não.list->bool'''
    for i,linha in enumerate(matriz):
        if len(linha) != len(matriz):
            return False
        for j in range(i):
            if linha[j] != mat[j][i]:
                return False
    return  True
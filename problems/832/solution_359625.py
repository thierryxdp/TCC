def eh_quadrada(matriz):
    '''Função que inidca se uma matriz e quadrada ou não.list->bool'''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]!= matriz[j][i]:
                return False
    return True
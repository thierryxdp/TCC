def eh_quadrada (matriz):
    '''função que identifica se uma matriz é quadrada,retorna
    True se for e False se não;list->bool'''
    linha=(len(matriz))
    col=(len(matriz[0]))
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]!=matriz[j][i]:
                return False
    return True
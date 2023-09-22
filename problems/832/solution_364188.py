def eh_quadrada (matriz):
    '''função que identifica se uma matriz é quadrada,retorna
    True se for e False se não;list->bool'''
    linha=(len(matriz))
    col=(len(matriz[0]))
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]!=mat[j][i]:
                return False
    return True
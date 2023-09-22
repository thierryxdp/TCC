def eh_quadrada(matriz):
    '''essa funçao verifica se uma matriz e quadrada ou nao
    list->bool'''
    i=0
    for i in range(len(matriz)):
        linhas=len(matriz)
        for j in range(len(matriz)):
            colunas=len(matriz[i])
    if linhas==colunas:
        return True
    elif linhas and colunas == 0:
        return True
    else:
        return False
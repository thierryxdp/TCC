def eh_quadrada(matriz):
    '''Esta função identifica se uma matriz é quadrada ou não.
list->bool'''
    if matriz==[]:
        return True
    for i in range(len(matriz)):
        linhas=len(matriz)
        for j in range(len(matriz[i])):
            colunas=len(matriz[i])
            if linhas==colunas:
                return True
    return False
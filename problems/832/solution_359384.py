def eh_quadrada(matriz):
    '''calcular e retornar uma função para identificar se
    a matriz é quadrada
    parametros:
    list-> bool'''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]!=matriz[j][i]:
                return False
    else:
        return True
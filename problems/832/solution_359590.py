def eh_quadrada(matriz):
    ''' retorna um true caso a matriz seja quadrada ou false caso nao
    matriz -> bool'''
    for i in range(len(matriz)):
        for j  in range(len(matriz[0])):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True
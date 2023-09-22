def eh_quadrada(matriz):
    for i in range(len(matriz)):
        for j  in range(len(matriz[0])):
            if matriz[i][j] == matriz[j][i]:
                return True
            if matriz[i][j] != matriz[j][i]:
                return False
def eh_quadrada(matriz):
    if any(len(linha) != len(matriz) for linha in matriz):
        return False
    for i in range(len(matriz)):
        for j in range(i): 
            if matriz[i][j] != matriz[j][i]:
                return False
    return True
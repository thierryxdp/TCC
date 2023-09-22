def eh_quadrada(matriz):
    for i in range (matriz):
        if len(linha) != len(matriz):
            return False
        for j in range(i):
            if linha[j] != matriz[j][i]:
                return False
    return True
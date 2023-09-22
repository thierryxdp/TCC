def eh_quadrada(matriz):
    for i, linha in enumerate(matriz):
        if len(linha) != len(matriz):
            return False
        for j in range(i):
            if linha[j][i] != matriz[j][i]:
                return False
    return True
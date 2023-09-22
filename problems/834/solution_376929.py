def media_matriz(matriz):
    soma = 0
    for linha in matriz:
        for aij in linha:
                soma += aij
    return soma/len(matriz)
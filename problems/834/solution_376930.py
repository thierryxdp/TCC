def media_matriz(matriz):
    soma = 0
    tamanho=0
    for linha in matriz:
        for aij in linha:
                soma += aij
                tamanho += len(linha)
    return soma/len(matriz)
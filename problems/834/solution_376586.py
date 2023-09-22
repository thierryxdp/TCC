def media_matriz(matriz):
    soma = 0
    for linhas in matriz:
        for colunas in linhas:
            soma = colunas + soma
    return soma / (len(matriz)*len(matriz[0]))
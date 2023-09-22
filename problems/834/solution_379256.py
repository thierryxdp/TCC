def media_matriz(matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    soma = 0
    for i in range(len(matriz)):
        for j in (matriz[i]):
            soma = soma + j
    resultado = soma/(nlin * ncol)
    return resultado %
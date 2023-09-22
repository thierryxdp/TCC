def media_matriz(matriz):
    soma=0
    for i in len(matriz):
        for j in len(matriz[i]):
            linha = i + j 
            soma += matriz[i][j]
    return round(soma / (len(matriz)*len(matriz[0])),2)
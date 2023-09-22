def busca(informacao, matriz):
    setor = []
    for i in range(len(matriz)):
        for j in range(len(matriz)[i]):
            if informacao in matriz[i][j] == True:
                setor += matriz[i][j]
    return setor
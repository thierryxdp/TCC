def busca(informacao, matriz):
    for i in range(len(matriz)):
        setor = []
        for j in range(len(matriz[i])):
            if informacao in matriz[i][j] == True:
                setor += matriz[i][j]
    return setor
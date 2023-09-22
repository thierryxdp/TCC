def busca(informacao, matriz):
    pos = 0
    setor = []
    for pos in range(len(matriz)):
        for pos in range(len(matriz)[pos][pos]):
            if informacao in matriz[pos][pos] == True:
                setor += matriz[pos][pos]
    return setor
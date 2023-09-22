def busca(setor,matriz):
    encontra = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            encontra+=[matriz[i][j]]
    return encontra
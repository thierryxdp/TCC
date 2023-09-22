def busca(setor, matriz):
    for i in range(len(matriz)):
        for k in range(len(matriz[0])):
            if setor in matriz[i][k]:
                return matriz[i][k]
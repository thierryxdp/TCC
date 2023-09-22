def busca(setor,matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == setor:
                return matriz[i][j]
            else:
                return []
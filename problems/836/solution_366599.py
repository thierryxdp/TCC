def busca(matriz,setor):
    doSetor = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == setor:
                doSetor.append(matriz[i])
    for k in range(len(doSetor)):
        del[k][2]
    return doSetor
def busca(matriz,setor):
    doSetor = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            doSetor += matriz[i]
    return doSetor
def busca(nome,matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    C = []
    for i in range(nlin):
        for j in range(ncol):
            if nome == matriz[i][j]:
                C.append(matriz[i])
                C.pop(j)
    return C
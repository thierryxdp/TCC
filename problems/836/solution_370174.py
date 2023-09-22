def busca(nome,matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    C = []
    for i in range(nlin):
        for j in range(ncol):
            if nome == matriz[i][j]:
                x = C.index(nome)
                C.append(matriz[i])
                del(C[x])
                
    return C
def busca(nome,matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    C = []
    i = 0
    for i in range(nlin):
        for j in range(ncol):
            if nome == matriz[i][j]:
                C.append(matriz[i])
                
                
                        
    return C
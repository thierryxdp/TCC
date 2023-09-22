def busca(nome,matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    C = []
    for i in range(nlin):
        for j in range(ncol):
            if nome == matriz[i][j]:
                C.append(matriz[i])
            i = 0
            while i < len C:
                C[i].remove[3]
                
                        
    return C
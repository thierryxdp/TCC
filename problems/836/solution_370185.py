def busca(nome,matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    C = []
    for i in range(nlin):
        for j in range(ncol):
            if nome == matriz[i][j]:
                C.append(matriz[i])
            if C[0][0] == nome:
                del(C[0])
            elif nome == C[0][1]:
                del(C[1])
            elif nome == C[0][2]:
                del(C[2])
            elif nome == C[0][3]:
                del(C[3])
               
                
    return C
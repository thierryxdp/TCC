def melhor_volta(matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    C =[]
    tupla = ()
    for i in range(nlin):
        for j in range(ncol):
            C.append(matriz[i][j])
            menor = min(C)
            if matriz[i][j] == menor:
                x = matriz[i][j]
            
    return x
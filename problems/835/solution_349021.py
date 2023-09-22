def melhor_volta(matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    C =[]
    tupla = ()
    for i in range(nlin):
        linha = []
        for j in range(ncol):
            C.append(matriz[i][j])
            menor = min(C)
            if matriz[i][j] == menor:
                linha.append(matriz[i][j])
    return (linha)
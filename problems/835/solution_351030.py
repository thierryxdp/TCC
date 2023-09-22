def melhor_volta(matriz):
    value = 1000
    for x in range(len(matriz)):
        minMat = min(matriz[x])
        if(minMat < value):
            col = x
            pos = matriz.index(minMat)
            value = minMat
    return (col, pos, value)
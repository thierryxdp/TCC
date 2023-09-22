def melhor_volta(matriz):
    col = 0
    pos = 0
    value = 1000
    for x in range(len(matriz)):
        minMat = min(matriz[x])
        if(minMat < value):
            col = x
            pos = matriz.index(minMat)
            value = minMat
    return (col, pos, value)
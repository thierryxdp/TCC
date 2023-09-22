def melhor_volta(matriz):
    col = 0
    pos = 1000
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            if(y < pos):
                pos = y
                col = x
    return (col, pos, matriz[col][pos])
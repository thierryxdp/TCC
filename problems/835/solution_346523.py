def melhor_volta(matriz):
    ''''''
    tupla = ()
    minimo = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            minimo += [min(matriz[i][:])]
            indice = matriz[i].index(matriz[i][j])
    return matriz.index(i),min(minimo),indice
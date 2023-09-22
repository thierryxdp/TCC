def melhor_volta(matriz):
    ''''''
    tupla = ()
    minimo = []
    indice = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            minimo += [min(matriz[i][:])]
            indice += [i]
    return indice,min(minimo),matriz.index[matriz[i][j]]
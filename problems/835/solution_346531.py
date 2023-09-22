def melhor_volta(matriz):
    ''''''
    tupla = ()
    minimo = []
    indice = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            minimo += [min(matriz[i][:])]
            indice += [i]
            ind = matriz.index(matriz[i][j])
    return indice,min(minimo),ind
def melhor_volta(matriz):
    ''''''
    tupla = ()
    minimo = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            minimo += [min(matriz[i][:])]
            indice = i
    return i,min(minimo),indice
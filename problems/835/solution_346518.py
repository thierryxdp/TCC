def melhor_volta(matriz):
    ''''''
    tupla = ()
    minimo = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            minimo += [min(matriz[i][:])]
    return matriz[i].index(),min(minimo),matriz[i].index(min(minimo))
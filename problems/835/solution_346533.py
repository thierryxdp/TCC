def melhor_volta(matriz):
    ''''''
    tupla = ()
    minimo = []
    indice = []
    corredores = len(matriz)
    voltas = len(matriz[0])
    for i in range(corredores):
        for j in range(voltas):
            minimo += [min(matriz[i][:])]
            indice += [i]
            if matriz[i][j] in minimo:
                ind = matriz.index(matriz[i][j])
    return corredores,min(minimo)
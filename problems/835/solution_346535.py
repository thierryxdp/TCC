def melhor_volta(matriz):
    ''''''
    corred = 0
    tupla = ()
    minimo = []
    corredores = len(matriz)
    voltas = len(matriz[0])
    for i in range(corredores):
        for j in range(voltas):
            corred = corredores
            minimo += [min(matriz[i][:])]
            indice += [i]
            
    return corred,min(minimo)
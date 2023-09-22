def melhor_volta(matriz):
    ''''''
    corred = 0
    tupla = ()
    minimo = []
    corredores = len(matriz)
    voltas = len(matriz[0])
    for i in range(corredores):
        for j in range(voltas):
            minimo += [min(matriz[i][:])]
            corred = i +1
            
    return corred,min(minimo)
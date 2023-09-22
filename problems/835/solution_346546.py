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
            if min(minimo) in matriz[i]:
                corred = i +1
                indice = matriz[corred -1].index(minimo)
            
    return corred,min(minimo),indice
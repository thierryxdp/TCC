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
            if minimo in matriz[i]:
                corred = i +1
            else:
                pass
           
            
    return corred,min(minimo)
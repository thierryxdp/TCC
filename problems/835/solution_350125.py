def melhor_volta(matriz):
    minimo = []
    for i in matriz:
        minimo = minimo + [min(i)]
   		tempo1 = min(minimo)
        x = list.index(minimo, tempo1)
        melhorVolta = list.index(matriz[x], tempo1)
    return (x+1,tempo1,melhorVolta+1)
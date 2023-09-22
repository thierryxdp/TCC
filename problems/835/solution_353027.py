def melhor_volta(matriz):
    ''''''
    corredormin=0
    tmin=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            	tmin= min(matriz[i][j])
    return tmin
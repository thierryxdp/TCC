def melhor_volta(matriz):
    tempo = []
    volta = []
    corredores = [] 
    for i in range(len(matriz)):
        tempo.append(min(matriz[i]))
        corredores.append(i)
        for j in range(len(matriz)[i]):
            if matriz[i][j]==min(matriz[i]):
                volta.append(j)
    return (min(tempo),volta,corredores)
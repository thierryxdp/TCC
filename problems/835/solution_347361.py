def melhor_volta(matriz):
    lista=[]
    melhor=min(matriz[0])
    for i in range(len(matriz)):
        if melhor>=min(matriz[i]):
            melhor=min(matriz[i])
        for j in range(len(matriz[0])):
            if melhor==matriz[i][j]:
                corredor=i
                volta=j
    return "corredor:" + str(i+1) + " volta:" + str(j+1) + " tempo:" + str(melhor)
def melhor_volta(matriz):
   
    melhor=matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]<melhor:
                melhor=matriz[i][j]
                melhor_corredor=i
                melhor_volta=j
    return (melhor_corredor+1,melhor,melhor_volta+1)
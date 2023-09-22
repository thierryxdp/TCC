def melhor_volta(matriz):
    melhor=[0,0]
    tempo=matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]<tempo:
                tempo=matriz[i][j]
                melhor[0]=i
                melhor[1]=j
    return (j+1,i+1,tempo)
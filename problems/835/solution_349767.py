def melhor_volta(matriz):
    melhor = (0, 0)
    menor = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] < matriz[melhor[0]][melhor[1]]:
                menor = matriz[i][j]
                melhor = (i,j)
    return (j+1,menor,melhor,i+1)
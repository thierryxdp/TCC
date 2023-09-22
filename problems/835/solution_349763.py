def melhor_volta(matriz):
    melhor = (0, 0)
    menor = matriz[0][0]
    for i in range(6):
        for j in range(10):
            if matriz[i][j] < matriz[melhor[0]][melhor[1]]:
                menor = matriz[i][j]
                melhor = (i,j)
    return (melhor,menor)
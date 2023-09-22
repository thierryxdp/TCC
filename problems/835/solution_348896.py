def melhor_volta(matriz):
    for i in range(6):
        for j in range(10):
            x = min(matriz[i][j])
    return (i+1,x,j+1)
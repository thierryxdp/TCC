def melhor_volta(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == 0:
                s0 += matriz[i][j]
            if j == 1:
                s1 += matriz[i][j]
            if j == 2:
                s2 += matriz[i][j]
            if j == 3:
                s3 += matriz[i][j]
            if j == 4:
                s4 += matriz[i][j]
            if j == 5:
                s5 += matriz[i][j]
            if j>=0 or j<=5:
                t = min(matriz[i][j])
    return (min(s0,s1,s2,s3,s4,s5),t)
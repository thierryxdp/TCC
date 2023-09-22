def melhor_volta(matriz):
    s0 = 0
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
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
            t = min(matriz[i][j])
    return (min(s0,s1,s2,s3,s4,s5),t)
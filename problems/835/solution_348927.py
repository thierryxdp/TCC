def malhor_volta(matriz):
    a=min(min(matriz))
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if a==matriz[i][j]:
                c=i
                d=j
    return (a,c,d)
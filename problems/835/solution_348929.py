def melhor_volta(matriz):
    a=min(matriz)
    a=min(a)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if a==matriz[i][j]:
                c=i
                d=j
    return (a,c,d)
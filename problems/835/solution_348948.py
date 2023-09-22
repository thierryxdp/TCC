def melhor_volta(matriz):
    a=min(matriz)
    f=min(a)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if f==matriz[i][j]:
                c=i
                d=j
    return (c,f,d)
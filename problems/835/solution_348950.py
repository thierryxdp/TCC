def melhor_volta(matriz):
    a=[]
    for I in range(len(matriz)):
        a=a+min(matriz[I])
    f=min(a)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if f==matriz[i][j]:
                c=i
                d=j+1
    return (c,f,d)
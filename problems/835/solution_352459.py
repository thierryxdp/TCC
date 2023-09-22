def melhor(matriz):
    C=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            list.append(C,matriz[i][j])
    menor=min(C)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==menor:
                quem=i+1
                volta=j+1
    return(quem,menor,volta)
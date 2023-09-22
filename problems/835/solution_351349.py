def melhor_volta(matriz):
    nlin=len(matriz)
    ncol=len(matriz[0])
    menor=matriz[0][0]
    volta=0
    posicao=0
    for i in range(nlin):
        for j in range(ncol):
            if menor>matriz[i][j]:
                menor=matriz[i][j]
                volta=j+1
                posicao=i+1
    return (posicao,menor,volta)
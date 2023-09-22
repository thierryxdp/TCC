def melhor_volta(matriz):
    menor=100
    for L in range(len(matriz)):
        for C in range(len(matriz[L])):
            if matriz[L][C]<menor:
                menor=matriz[L][C]
                linha=L
                coluna=C
    return linha+1,menor,coluna+1
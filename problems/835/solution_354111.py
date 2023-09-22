def melhor_volta(matriz):
    """essa funcao recebe como entrada uma matriz com os tempos em segundos dos corredores em cada volta e retorna uma tupla informando de quem foi a melhor volta, qual o tempo e em que volta
    list->tuple"""
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
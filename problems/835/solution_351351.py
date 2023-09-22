def melhor_volta(matriz):
    """função que recebe uma matriz de linha 6 e coluna 10
    e retorna uma tupla com quem foi a melhor volta,tempo e
    em que volta
    list->tuple"""
    nlin=len(matriz)
    ncol=len(matriz[0])
    tempo=matriz[0][0]
    N_v=0
    volta=0
    for i in range(nlin):
        for j in range(ncol):
            if tempo>matriz[i][j]:
                tempo=matriz[i][j]
                N_v=j+1
                volta=i+1
    return (volta,tempo,N_v)
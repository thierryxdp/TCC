def melhor_volta(matriz):
    """ oi """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if min(min(matriz)) in [matriz[i][j]]:
                return i,j,min(min(matriz))
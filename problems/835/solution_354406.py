def melhor_volta(matriz):
    s = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            s += [matriz[i][j],]
            t = list.index(s,min(s))
    return s
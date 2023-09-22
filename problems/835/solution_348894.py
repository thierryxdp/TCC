def melhor_volta(matriz):
    voltas = []
    for i in range(6):
        volta = 0
        for j in range(10):
            volta += matriz[i][j]
        list.append(voltas,volta)
    menor = min(voltas)
    pos = list.index(voltas,menor)
    return matriz[pos],menor
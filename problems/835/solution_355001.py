def melhor_volta(matriz):
    menorT = volta = vencedor = 1000
    for x in range(0, len(matriz)):
        for y in range(0, len(matriz[x])):
            if min(matriz[x][y], menorT) == matriz[x][y]:
                menorT = min(matriz[x][y], menorT)
                vencedor = x + 1
                volta = y + 1
    return vencedor, menorT, volta
def melhor_volta (matriz):
    menor= volta = vencedor = 1000
    for v in range(0, len(matriz)):
        for t in range(0, len(matriz[v])):
            if min(matriz[v][t], menor) == matriz[v][t]:
                menor = min(matriz[v][t], menor)
                vencedor = v + 1
                volta = t + 1

    return vencedor, menor, volta
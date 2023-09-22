def melhor_volta(matriz):

    menor= coluna = piloto = 1000
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if min(matriz[i][j], menor) == matriz[i][j]:
                menor = min(matriz[i][j], menor)
                piloto = i + 1
                coluna = j + 1

    return piloto, menor, coluna
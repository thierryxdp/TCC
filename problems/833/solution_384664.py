def conta_numero(numero, matriz):
    q = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero == matriz[i][j]:
                q += 1

    return q
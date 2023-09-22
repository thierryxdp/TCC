def conta_numero(matriz, numero):
    ocorrencias = 0
    for n in range(len(matriz)):
        for i in range(len(matriz[n])):
            if matriz[n][i] == numero:
                ocorrencias += 1
    return ocorrencias
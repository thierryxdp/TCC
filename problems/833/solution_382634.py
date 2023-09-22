def conta_numero(numero,matriz):
    qtd = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                qtd += 1
    return qtd
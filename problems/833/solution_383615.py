def conta_numero(numero,matriz):
    contar = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            contar += int(matriz[i][j] == numero)
    return contar
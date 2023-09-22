def conta_numero(numero,matriz):
    count = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
            	count = count + 1
    return count
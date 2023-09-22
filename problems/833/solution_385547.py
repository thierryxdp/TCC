def conta_numero(numero,matriz):
    cont = 0
    for i in len(matriz):
        for j in len(matriz[i][j]):
            if numero == j:
                cont = cont + 1
    return cont
def conta_numero(numero,matriz):
    cont = 0
    linhas = len(matriz)
    for i in linhas:
        for j in len(matriz[i][j]):
            if numero == j:
                cont = cont + 1
    return cont
def conta_numero(numero,matriz):
    conta = 0
    for i in matriz:
        for j in matriz[i]:
            if matriz[i][j] == numero:
                conta += 1
    return conta
def conta_numero(numero, matriz):
    qtde = 0
    for a in matriz:
        for b in matriz[a]:
            if matriz[a][b] == numero:
                qtde += 1
    return qtde
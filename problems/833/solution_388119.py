def conta_numero(numero,matriz):
    conta=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                conta=conta+list.count(matriz[i][j],numero)
    return conta
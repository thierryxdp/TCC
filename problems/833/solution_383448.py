def conta_numero(numero,matriz):
    y = 0
    for i in range(len(matriz)):
        y += matriz[i].count(numero)
    return y
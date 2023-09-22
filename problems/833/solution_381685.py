def conta_numero(numero,matriz):
    pos = 0
    conta = 0
    for pos in range(len(matriz)):
        conta += list.count(matriz[pos],numero)
    return conta
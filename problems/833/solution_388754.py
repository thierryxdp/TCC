def conta_numero(numero,matriz):
    conta = 0
    for linha in matriz:
        conta += list.count(matriz[linha],numero)
    return conta
def conta_numero(numero,matriz):
    """ retorna quantas vezes um numero aparece na matriz
    int, list -> int"""
    quant = 0
    for i in range(len(matriz)):
        quant += matriz[i].count(numero)
    return quant
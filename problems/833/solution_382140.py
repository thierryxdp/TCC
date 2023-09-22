def conta_numero(numero,matriz):
    vezes = 0
    proximo = 0
    while proximo<((len(matriz))*(len(matriz[0]))):
        if numero in matriz[proximo][proximo]:
            vezes += 1
        proximo += 1
    return vezes
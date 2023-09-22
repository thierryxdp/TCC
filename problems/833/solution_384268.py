def conta_numero(numero,matriz):
    vezes = 0
    for linha in matriz:
        vezes = vezes + linha.count(numero)
    return vezes
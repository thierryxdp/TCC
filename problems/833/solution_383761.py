def conta_numero(num,matriz):
    vezes = 0
    for num in matriz:
        vezes = vezes + 1
        for num in matriz[0]:
            vezes = vezes + 1
    return vezes
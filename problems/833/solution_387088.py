def conta_numero(numero, matriz):
    conta = 0
    for numero in matriz[:]:
        conta = conta + 1
        for numero in matriz:
            conta = conta + 1
    return conta
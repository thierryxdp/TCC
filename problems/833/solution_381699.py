def conta_numero(numero,matriz):
    conta = 0
    for linha in matriz:
        for item in linha:
            if item == numero:
                conta = conta + 1
    return conta
def conta_numero(numero, matriz):
    vezes = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == numero:
                vezes += 1
    return vezes
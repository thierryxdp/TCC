def conta_numero(numero, matriz):
    qtd = 0
    for linha in matriz:
        for el in linha:
            if el == numero:
                qtd += 1

    return qtd
def conta_numero(numero, matriz):
    contador = 0
    for elemento in matriz:
        for number in elemento:
            if number == numero:
                contador += 1
    return contador
def conta_numero(numero,matriz):
    contador = 0
    for i in matriz:
        for i2 in i:
            if i2 == numero:
                contador += 1
    return contador
def conta_numero(numero,matriz):
    contador=0
    for termo in len(matriz):
        for elemento in termo:
            if elemento == numero:
                contador += 1
    return contador
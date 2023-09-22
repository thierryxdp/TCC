def conta_numero(numero,matriz):
    i = 0
    repetiu = 0
    while i < len(matriz):
        if numero in matriz[i]:
            repetiu += 1
            i += 1
        else:
            i += 1
    return repetiu
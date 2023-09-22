def conta_numero(numero,matriz):
    cont = 0
    repetiu = 0
    i = 0
    while cont < len(matriz):
        if numero in matriz[i]:
            repetiu += 1
            cont += 1
            i += 1
        else:
            cont += 1
            i += 1
    return repetiu
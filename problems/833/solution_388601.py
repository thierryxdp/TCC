def conta_numero(numero,matriz):
    cont = 0
    i = 0
    repetiu = 0
    while cont < len(matriz):
        if numero in matriz[i]:
            repetiu += 1
            cont += 1
            i += 1
        else:
            i += 1
            cont += 1
    return repetiu
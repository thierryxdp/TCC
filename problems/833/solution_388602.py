def conta_numero(numero,matriz):
    cont = 0
    i = 0
    repetiu = 0
    while cont < len(matriz):
        for elemento in matriz[i]:
            if numero in elemento:
                repetiu += 1
                cont += 1
                i += 1
            else:
                cont += 1
                i += 1
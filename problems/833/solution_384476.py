def conta_numero(numero,matriz):
    if numero in matriz[0]:
        return len(matriz[0]-numero)
    else:
        return 0
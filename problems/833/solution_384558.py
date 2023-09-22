def conta_numero(numero,matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    contador = 0
    for numero in range(nlin):
        for numero in range(ncol):
            contador += 1
    return contador
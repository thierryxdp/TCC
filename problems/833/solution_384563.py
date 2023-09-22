def conta_numero(numero,matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    contador = 0
    for i in range(nlin):
        for j in range(ncol):
            if matriz[i] != numero:
                contador+=1
    return contador
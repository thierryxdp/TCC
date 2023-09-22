def conta_numero(numero, matriz):
    contador = 0
    for x in matriz:
        for y, z in enumerate(matriz[x]):
            if z == numero:
                contador = contador + 1
    return contador
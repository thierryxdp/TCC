def conta_numero(numero, matriz):
    contador = 0
    for x in matriz:
        for y, z in enumerate(matriz):
            if z == numero:
                contador = contador + 1
    return contador
def conta_numero(numero, matriz):
    contador = 0
    for x, y in enumerate(matriz):
        for z in matriz[x]:
            if z == numero:
                contador = contador + 1
    return contador
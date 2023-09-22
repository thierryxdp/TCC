def conta_numero(numero,matriz):
    contador = 0
    for x in matriz:
        for y in matriz[0]:
            if y == numero:
                contador = contador + 1
    return contador
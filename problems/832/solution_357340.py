def eh_quadrada(matriz):
    proximo = 0
    acumulador = []
    while proximo < len(matriz):
        if len(matriz[proximo]) == len(matriz):
            acumulador = acumulador + [1]
        proximo = proximo + 1
    if len(acumulador) == len(matriz):
        return True
    else:
        return False
def repetidos(numeros):
    prox = 1
    repet = 0
    while prox < len(numeros):
        if numeros[prox] == numeros[prox-1]:
            repet = repet + 1
        prox = prox + 1
    return repet
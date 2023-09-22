def repetidos(numeros):
    prox = 1
    repet = 1
    while prox < len(numeros):
        if numeros[prox] == numeros[prox-1]:
            repet = repet + 1
        prox = prox + 1
    return repet
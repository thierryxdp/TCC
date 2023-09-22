def faltante(lista):
    contador = 1
    indice = 0
    acumulador = 0
    while contador<=len(lista):
        if contador != lista[indice]:
            acumulador = acumulador + contador - 1
        contador = contador + 1
        indice = indice + 1
    return acumulador
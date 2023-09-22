def faltante(lista):
    contador = 1
    acumulador = 0
    while contador<=len(lista):
        if contador != lista[contador]:
            acumulador = acumulador + contador - 1
        contador = contador + 1
    return acumulador
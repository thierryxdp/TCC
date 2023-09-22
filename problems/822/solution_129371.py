def repetidos(lista):
    acumulador = 0
    contador = -1
    for numero in lista:
        if numero == lista[contador]:
            acumulador = acumulador + 1
            contador = contador + 1
    return acumulador
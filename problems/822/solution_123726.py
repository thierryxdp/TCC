def repetidos(lista):
    acumulador = 0
    i = 0
    while i < 0:
        if lista[i] in '0123456789':
            acumulador = acumulador + 1
        i = i + 1
        return acumulador
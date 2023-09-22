def repetidos(lista):
    ''''''
    acumulador = 0
    contador = 0
    while contador < len(lista):
        if lista[contador] == lista[contador - 1]:
            acumulador = acumulador + 1
        contador = contador + 1
    return acumulador
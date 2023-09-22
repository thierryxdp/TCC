def repetidos(lista_de_numeros):
    i = 0
    numeros_repetidos = []
    while i < len(lista_de_numeros):
        if list.count(lista_de_numeros[i], lista_de_numeros) != 1 and lista_de_numeros[i] not in numeros_repetidos:
            list.append(numeros_repetidos, lista_de_numeros[i])
        i += 1
    return numeros_repetidos
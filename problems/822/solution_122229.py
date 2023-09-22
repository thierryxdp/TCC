def repetidos(lista):
    """ """
    atual = []
    proximo = []
    cont = 1
    repetido = 0
    for i in lista:
        proximo = lista[cont]
        if proximo == i:
            repetido += 1
        cont += 1
    return repetido
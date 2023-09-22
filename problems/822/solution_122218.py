def repetidos (lista):
    """ """
    proximo = []
    atual = []
    repetido = 0
    cont = 0
    for i in lista:
        atual = i
        proximo = lista[cont]
        if proximo[0] == atual[0]:
            repetido += 1
        cont += 1
    return repetido
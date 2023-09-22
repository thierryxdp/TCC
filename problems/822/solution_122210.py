def repetidos (lista):
    """ """
    proximo = ""
    atual = ""
    repetido = 0
    cont = 1
    for i in lista:
        atual = i
        proximo = lista[cont]
        if proximo == atual:
            repetido += 1
        cont += 1
    return repetido
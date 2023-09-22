def repetidos (lista):
    """ """
    proximo = ""
    atual = ""
    repetido = 0
    cont = 0
    for i in lista:
        atual = i
        proximo = lista[cont+1]
        if proximo == atual:
            repetido += 1
        cont += 1
    return repetido
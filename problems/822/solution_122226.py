def repetidos (lista):
    """ """
    proximo = []
    atual = []
    repetido = 0
    cont = 0
    i = 0
    while i < len(lista):
        atual = lista[i]
        i += 1
        proximo = lista[i]
        if proximo == atual:
            repetido += 1
        cont += 1
    return repetido
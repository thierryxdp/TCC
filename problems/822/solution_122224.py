def repetidos (lista):
    """ """
    proximo = []
    atual = []
    repetido = 0
    cont = 0
    i = 0
    while i < len(lista):
        atual = lista[i]
        proximo = lista[i+1]
        if proximo == atual:
            repetido += 1
        cont += 1
        i += 1
    return repetido
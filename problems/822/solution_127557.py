def repetidos(lista):
    vezes = 0
    lastEl = None
    for el in lista:
        if lastEl == el:
            vezes += 1
        lastEl = el
    return vezes
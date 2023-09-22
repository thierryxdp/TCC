def total(lista, produtos):
    i = 0
    j = 0
    while i < len(lista):
        if lista[i] in produtos:
            j += produtos[lista[i]]
        i += 1
    return j
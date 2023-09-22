def total(lista, dicionario):
    i = 0
    j = 0
    while i < len(dicionario):
        if dicionario[i] in lista:
            j += dicionario[i]
        i += 1
    return j
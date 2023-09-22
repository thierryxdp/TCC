def total(lista, dicionario):
    i = 0
    j = 0
     while i < len(lista):
        for lista[i] in dicionario:
            j += dicionario[lista[i]]
            i += 1
    return j
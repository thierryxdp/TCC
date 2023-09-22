def total(lista, dicionario):
    n = 0
    for n in lista:
        if n in dicionario:
            n = n + float(dict.get(dicionario, n))
    return n
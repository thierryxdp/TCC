def total(lista, dicionario):
    n = ()
    for n in lista:
        if n in dicionario:
            n = (n) + (dict.get(dicionario, n),)
    return n
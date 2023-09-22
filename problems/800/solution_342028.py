def total(lista, dicionario):
    total = 0
    for n in lista:
        if n in dicionario:
             total = total + dict.get(dicionario, n)
    return total
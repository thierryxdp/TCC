def total(lista, dicionario):
    subtotal = 0
    for i in lista:
        subtotal += dicionario[i]
    return round(subtotal, 2)
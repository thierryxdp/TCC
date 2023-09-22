def total(lista, dicionario):
    subtotal = 0
    for i in lista:
        subtotal += dicionario[i]
    round(subtotal, 2)
    return subtotal
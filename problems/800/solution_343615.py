def total(lista, produtos):
    valor = 0
    for item in compras:
        valor = valor + produtos[item]

    return round(valor, 2)
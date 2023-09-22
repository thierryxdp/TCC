def total(lista, produtos):
    valor = 0
    listap = list(produtos)
    for item in lista:
        if item in produtos:
            valor = valor + listap
    return round(valor,2)
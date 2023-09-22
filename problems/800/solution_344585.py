def total(lista, produtos):
    valores = []
    for x in lista:
        valores.append(produtos[x])
    return round(sum(valores), 2)
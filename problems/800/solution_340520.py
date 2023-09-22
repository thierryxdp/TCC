def total(lista, relation):
    listprod = list(dict.keys(relation))
    valor = 0
    for n in listprod:
        if n in lista:
            valor += dict.get(relation, n)
    return round(valor, 2)
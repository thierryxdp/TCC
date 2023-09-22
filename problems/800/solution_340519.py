def total(lista, relation):
    listprod = list(dict.keys(relation))
    precos = []
    valor = 0
    for n in listprod:
        if n in lista:
            valor += dict.get(relation, n)
    return round(valor, 2)
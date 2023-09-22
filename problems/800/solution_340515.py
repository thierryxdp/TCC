def total(lista, relation):
    listprod = list(dict.keys(relation))
    precos = []
    for n in listprod:
        if n in lista:
            valor = dict.get(relation, n)
        return valor
def total(lista, relation):
    listprod = list(dict.keys(relation))
    for n in listprod if n in lista:
        return n
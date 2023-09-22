def total(lista, relation):
    listprod = list(dict.keys(relation))
    for n in relation if n in lista:
        return n
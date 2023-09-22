def intercala(lista1, lista2):
    """ dada duas listas como entrada, retorna uma nova lista intercalando esses valores. str->str."""
    a = str(lista1[0])
    b = str(lista1[1])
    c = str(lista1[2])
    d = str(lista1[0])
    e = str(lista2[1])
    f = str(lista1[2])
    return ([a]+[d]+[b]+[e]+[c]+[f])